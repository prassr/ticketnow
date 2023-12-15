import datetime
import json
from functools import wraps
from flask import request, jsonify, make_response
from flask_restful import Resource, reqparse, marshal_with, fields
from flask_jwt_extended import (
    JWTManager,
    jwt_required,
    create_access_token,
    get_jwt_identity,
    get_jwt,
    current_user
)

jwt = JWTManager()

import redis

## Celery

from celery.result import AsyncResult
from application import tasks

from application.dao import *
from application.model import *
from application.utils import cache
from application.utils import (
    user_fields,
    theatre_fields,
    screen_fields,
    booking_for_show,
    movie_fields,
    movie_show_fields,
    show_fields,
    booking_fields,
    like_fields,
    movie_rating_review_fields,
    rating_review_fields,
    show_by_id_fields,
    BusinessValidationError,
    generate_otp,
    send_login_otp_mail,
    send_password_reset_otp_mail,
    send_signup_otp_mail,
    send_ticket_details,
    send_report,
    filter_bookings_by_date_range,
)

redis_otp = redis.Redis(host='localhost', port=6379, db=0, decode_responses=True)
redis_jwt = redis.Redis(host='localhost', port=6379, db=1, decode_responses=True)
redis_report = redis.Redis(host="localhost", port=6379, db=2, decode_responses=True)
redis_theatres = redis.Redis(host="localhost", port=6379, db=3, decode_responses=True)

@jwt.user_identity_loader
def user_identity_lookup(user):
    return user.email

@jwt.expired_token_loader
def expired_token(jwt_header, jwt_body):
    return make_response(jsonify({"error_code": "SESSION101", "error_message": "Session timed out kindly log in again"}), 401)


@jwt.invalid_token_loader
def invalid_token(message):
    return make_response(jsonify({"error_code": "TOKEN101", "error_message": "UNAUTHORISED"}), 401)


@jwt.user_lookup_loader
def user_lookup_callback(_jwt_header, jwt_data):
    identity = jwt_data["sub"]
    return UserDAO.get_user_by_email(identity) or AdminDAO.get_admin_by_email(identity) 

@jwt.token_in_blocklist_loader
def is_blocklisted_token(_jwt_header, jwt_payload):
    jti = jwt_payload["jti"]
    return redis_jwt.get(jti)

def admin_required():
    def decorator(fn):
        @wraps(fn)
        def wrapper(*args, **kwargs):
            if AdminDAO.get_admin_by_email(current_user.email):
                return fn(*args, **kwargs)
            else:
                raise BusinessValidationError(401, "ADMIN101")
        return wrapper
    return decorator

class OTPResetPasswordResource(Resource):
    def post(self):
        d = request.get_json()
        user = UserDAO.get_user_by_email(d["email"]) or AdminDAO.get_admin_by_email(d["email"])
        if user:
            if redis_otp.get(user.email): # check email in redis otp database
                message = {'message':'OTP_VALID_15'}
                return  make_response(jsonify(message), 201)

            otp = generate_otp()
            if send_password_reset_otp_mail.delay(user.first_name +" "+user.last_name, otp, d["email"]):
                redis_otp.setex(d["email"], datetime.timedelta(minutes=15), otp)
                message = {'message':'OTP_SENT'}
                return make_response(jsonify(message), 201)
        else:
            raise BusinessValidationError(404, "EMAIL102")

class ResetPasswordResource(Resource):
    def post(self):
        d = request.get_json();
        user = UserDAO.get_user_by_email(email=d["email"]) or AdminDAO.get_admin_by_email(email=d["email"])
        if user:
            PasswordResetDAO.reset_password(user, d["password"])
            message = {'message':'PASSWORD_RESET_SUCCESSFUL'}
            return make_response(jsonify(message), 201)
        raise BusinessValidationError(400, "ACCESS101")
 

class OTPSignupResource(Resource):
    def post(self):
        d = request.get_json()
        user = UserDAO.get_user_by_email(d["email"]) # check if user exist
        if user:
            raise BusinessValidationError(400, "USER102")
        otp_in_store = redis_otp.get(d["email"]) 
        if otp_in_store:
            message = {'message':'OTP_VALID_15'}
            return  make_response(jsonify(message), 201)
        # otherwise sent otp
        otp = generate_otp()
        is_sent = send_signup_otp_mail.delay(otp, d["email"])
        if is_sent:
            redis_otp.setex(d["email"], datetime.timedelta(minutes=15), otp)
            message = {'message':'OTP_SENT'}
            return make_response(jsonify(message), 201)
        else:
            raise BusinessValidationError(404, "OTP104")

class OTPVerifyResource(Resource):
    def post(self):
        d = request.get_json()
        otp_in_store = redis_otp.get(d["email"]) # check email in redis otp database
        if int(d["OTP"]) == int(otp_in_store):
            message = {"message":"OTP_VERIFIED"},
            return make_response(jsonify(message), 200)
        raise BusinessValidationError(401,"OTP102")


class OTPLoginResource(Resource):
    def post(self):
        auth=request.get_json()
        if auth["as"] == "user":
            user = UserDAO.get_user_by_email(auth["email"])
        elif auth["as"] == "admin":
            user = AdminDAO.get_admin_by_email(auth["email"])

        if user:
            otp_in_store = redis_otp.get(user.email) # check email in redis otp database
            if otp_in_store:
                message = {'message':'OTP_VALID_15'}
                return  make_response(jsonify(message), 201)
            # otherwise sent otp
            otp = generate_otp(user.id)
            is_sent = send_login_otp_mail.delay(user.first_name+" "+user.last_name, otp, user.email)
            if is_sent:
                redis_otp.setex(user.email, datetime.timedelta(minutes=15), otp)
                message = {'message':'OTP_SENT'}
                return make_response(jsonify(message), 201)
        else:
            raise BusinessValidationError(404, "USER101")

class LoginResource(Resource):
    # @marshal_with(user_fields)
    def post(self):
        flag = False
        auth = request.get_json()
        login_as = request.args.get("as")
        user = None
        if login_as == "user":
            user = UserDAO.get_user_by_email(auth["email"])
            if not user:
                raise BusinessValidationError(404, "USER101")
    
        elif login_as == "admin":
            admin = AdminDAO.get_admin_by_email(auth["email"])
            if not admin:
                raise BusinessValidationError(404, "ADMIN101")
        user = user or admin
        if user:
            is_valid = False
            if auth["OTP"]:
                opt = redis_otp.get(user.email)
                is_valid = auth["OTP"] == otp
                if not is_valid:
                    raise BusinessValidationError(404, "OTP102")
            elif auth["password"]:
                is_valid = LoginDAO.check_password(user, auth["password"]) # auth["as"] // which table to user_lookup            if is_valid:
                if not is_valid:
                    raise BusinessValidationError(404, "PASS102")
                x_access_token = create_access_token(identity=user)
                return jsonify({'x-access-token':x_access_token})

class LogOut(Resource):
    @jwt_required()
    def get(self):
        if current_user:
            jti = get_jwt()["jti"]
            redis_jwt.setex(jti, datetime.timedelta(days=7), "blocked")
            return jsonify({"message":"LOGOUT_SUCCESSFUL"})
        else:
            return jsonify({"message":"SESSION_EXPIRED"})


class UserResource(Resource):
    @jwt_required()
    @admin_required()
    @marshal_with(user_fields)
    def get(self):
        users = UserDAO.get_users()
        return users

    @marshal_with(user_fields)
    def post(self):
        d = request.get_json()
        if UserDAO.get_user_by_email(d["email"]):
            raise BusinessValidationError(404, "USER102")
        user = UserDAO.create_user(d)
        return user


class UserIdResource(Resource):
    @jwt_required()
    @marshal_with(user_fields)
    def get(self):
        email = current_user.email
        user = UserDAO.get_user_by_email(email)
        return user

    @jwt_required()
    @marshal_with(user_fields)
    def put(self):
        email = current_user.email
        user = UserDAO.get_user_by_email(email)
        d = request.get_json()
        if user:
            user = UserDAO.update_user(d)
        return user

    @jwt_required()
    def delete(self):
        email = current_user.email
        user = UserDAO.get_user_by_email(email)
        auth = request.get_json()
        is_valid = LoginDAO.check_password(user, auth["password"])
        if is_valid:
            db.session.delete(user)
            db.session.commit()
            return "", 200
        else:
            return "", 401


class TheatreResource(Resource):
    @jwt_required()
    @marshal_with(theatre_fields)
    @cache.memoize()
    def get(self):
        return TheatreDAO.get_theatres()

    @jwt_required()
    @admin_required()
    @marshal_with(theatre_fields)
    def post(self):
        d = request.get_json()
        theatre = TheatreDAO.create_theatre(d)
        return theatre


class TheatreIdResource(Resource):
    @jwt_required()
    @marshal_with(theatre_fields)
    def get(self, theatre_id):
        theatre = TheatreDAO.get_theatre(theatre_id)
        if theatre:
            return theatre
        else:
            raise BusinessValidationError(404, "THEATRE101")
    
    @jwt_required()
    @admin_required()
    @marshal_with(theatre_fields)
    def put(self, theatre_id):
        theatre = TheatreDAO.get_theatre(theatre_id)
        if theatre:
            d = request.get_json()
            theatre = TheatreDAO.update_theatre(theatre, d)
            return theatre
        raise BusinessValidationError(404, "THEATRE101")
    
    @jwt_required()
    @admin_required()
    def delete(self, theatre_id):
        theatre = TheatreDAO.get_theatre(theatre_id)
        is_deleted = TheatreDAO.delete_theatre(theatre)
        if is_deleted:
            return jsonify({"message":"DELETED"})
        raise BusinessValidationError(404, "THEATRE101")


class MovieResource(Resource):
    @jwt_required()
    @marshal_with(movie_fields)
    def get(self):
        movies = MovieDAO.get_movies()
        return movies

    @jwt_required()
    @admin_required()
    @marshal_with(movie_fields)
    def post(self):
        d = request.get_json()
        movie = MovieDAO.create_movie(d)
        if movie:
            return movie
        # handle errors


class MovieIdResource(Resource):
    @jwt_required()
    @marshal_with(movie_fields)
    def get(self, movie_id):
        movie = MovieDAO.get_movie(movie_id)
        return movie


    @jwt_required()
    @admin_required()
    @marshal_with(movie_fields)
    def put(self, movie_id):
        d = request.get_json()
        format_string = "%Y-%m-%d"
        d["release_date"] = datetime.datetime.strptime(d["release_date"], format_string)
        movie = MovieDAO.get_movie(movie_id)
        if movie:
            movie = MovieDAO.update_movie(movie, d)
            return movie
        raise BusinessValidationError(404, "MOVIE101")

    @jwt_required()
    @admin_required()
    def delete(self, movie_id):
        movie = MovieDAO.get_movie(movie_id)
        is_deleted = MovieDAO.delete_movie(movie)
        if is_deleted:
            return jsonify({"message":"DELETED"})
        raise BusinessValidationError(404, "MOVIE101")

class MovieShowResource(Resource):
    @jwt_required()
    @marshal_with(movie_show_fields)
    @cache.memoize()
    def get(self):
        movies = MovieDAO.get_movies()
        return movies


class ShowResource(Resource):
    @jwt_required()
    @marshal_with(show_fields)
    @cache.memoize()
    def get(self):
        shows = ShowDAO.get_shows()
        if UserDAO.get_user_by_email(current_user.email):
            shows.bookings = BookingDAO.get_booking_by_user(current_user.id)
        return shows

    @jwt_required()
    @admin_required()
    @marshal_with(show_fields)
    def post(self):
        d = request.get_json()
        format_string = "%d/%m/%Y, %H:%M:%S"
        d["start_time"] = datetime.datetime.strptime(d["start_time"], format_string)
        show = ShowDAO.create_show(d)
        if show:
            return show

class ShowIdResource(Resource):
    @jwt_required()
    @marshal_with(show_by_id_fields)
    def get(self, show_id):
        show = JoinDAO.get_show(show_id)
        response = {}
        if show:
            response = {
                'show': show[0],
                'theatre': show[1],
                'movie': show[2],
                'screen': show[3],
        }
        return response

    @jwt_required()
    @admin_required()
    @marshal_with(show_fields)
    def put(self, show_id):
        show = ShowDAO.get_show(show_id)
        if show:
            d = request.get_json()
            format_string = "%d/%m/%Y, %H:%M:%S"
            try:
                d["start_time"] = datetime.datetime.strptime(d["start_time"], format_string)
            except:
                d["start_time"] = datetime.datetime.strptime(d["start_time"], '%a, %d %b %Y %H:%M:%S %z')
            show = ShowDAO.update_show(show, d)
            return show
        raise BusinessValidationError(404, "SHOW101")

    @jwt_required()
    @admin_required()
    def delete(self, show_id):
        show = ShowDAO.get_show(show_id)
        is_deleted = ShowDAO.delete_show(show)
        if is_deleted:
            return jsonify({"message":"DELETED"})
        raise BusinessValidationError(404, "SHOW101")

class ScreenResource(Resource):
    @marshal_with(screen_fields)
    @cache.memoize()
    def get(self):
        screens = ScreenDAO.get_screens()
        return screens

    @jwt_required()
    @admin_required()
    @marshal_with(screen_fields)
    def post(self):
        d = request.get_json()
        num_screens = len(TheatreDAO.get_theatre(d["theatre_id"]).screens)
        if num_screens == 2:
            raise BusinessValidationError(404, "SCREEN102")
        screen = ScreenDAO.create_screen(data=d)
        return screen



class ScreenIdResource(Resource):
    @marshal_with(screen_fields)
    def get(self, screen_id):
        screen = ScreenDAO.get_screen(screen_id)
        if screen:
            return screen
        raise BusinessValidationError(404, "SCREEN101")

    @jwt_required()
    @admin_required()
    @marshal_with(screen_fields)
    def put(self, screen_id):
        screen = ScreenDAO.get_screen(screen_id)
        if screen:
            d = request.get_json()
            screen = ScreenDAO.update_screen(screen, d)
            return screen
        raise BusinessValidationError(404, "SCREEN101")

    @jwt_required()
    @admin_required()
    def delete(self, screen_id):
        screen = ScreenDAO.get_screen(screen_id)
        is_deleted = ScreenDAO.delete_screen(screen)
        if is_deleted:
            return jsonify({"message":"DELETED"})
        raise BusinessValidationError(404, "SCREEN101")


class BookingsByShowIdResource(Resource):
    @jwt_required()
    @marshal_with(booking_for_show)
    def get(self, show_id):
        bookings = BookingDAO.get_bookings_by_show(show_id)
        return bookings

class SeatsAvailableResource(Resource):
    @jwt_required()
    def get(self, show_id):
        available_bookings_per_class = BookingDAO.get_available_bookings_per_class(show_id)
        return available_bookings_per_class

class ShowByTheatreIdResource(Resource):
    def get(self):
        shows = ShowDAO.get_shows_by_theatre()
        return shows

class BookingResource(Resource):
    @jwt_required()
    @marshal_with(booking_fields)
    @cache.memoize()
    def get(self):
        bookings = BookingDAO.get_bookings()
        return bookings

    @jwt_required()
    @marshal_with(booking_fields)
    def post(self):
        d = request.get_json()
        seat_stats = BookingDAO.get_available_bookings_for_class(d["show_id"], d["seat_class"])
        avail_seats = seat_stats["capacity"] - seat_stats[d["seat_class"]]
        if avail_seats > d["no_of_seats"]:
            data = {}
            data["seat_class"] = d["seat_class"]
            data["no_of_seats"] = d["no_of_seats"]
            data["price"] = d["price"]
            data["show_id"] = d["show_id"]
            data["user_id"] = current_user.id
            booking = BookingDAO.create_booking(data)
            if booking:
                tdetails = [
                    d["movie_name"],
                    d["start_time"],
                    d["no_of_seats"],
                    d["seat_class"], 
                    d["price"],
                    d["venue"]
                ]
                is_sent = send_ticket_details.delay(current_user.first_name+" "+current_user.last_name, 
                                                    current_user.email, 
                                                    tdetails)
                return booking


class UserBookingResource(Resource):
    @jwt_required()
    def get(self):
        bookings = BookingDAO.get_bookings_by_user(current_user.id)
        return bookings

class AdminReportResource(Resource):
    @jwt_required()
    @admin_required()
    def get(self):
        start_date = request.args.get('start_date')
        end_date = request.args.get('end_date')
        sm = request.args.get("sm")
        tid = request.args.get("tid")
        report_data = BookingDAO.generate_report()
        user = current_user
        if start_date and end_date:
            report_data = filter_bookings_by_date_range(report_data, start_date, end_date)
        if tid:
            rp = []
            for d in report_data:
                if d.theatre_id == tid:
                    rp.append(d)
            report_data = rp
        if sm == "1":
            report = send_report.delay(user.first_name +" "+user.last_name, user.email, report_data)
        return jsonify(report_data)

class BookingIdResource(Resource):
    @jwt_required()
    @marshal_with(booking_fields)
    def get(self, booking_id):
        booking = BookingDAO.get_booking(booking_id)
        if booking:
            return booking
        raise BusinessValidationError(404, "BOOKING101")

    @jwt_required()
    @marshal_with(booking_fields)
    def put(self, booking_id):
        booking = BookingDAO.get_booking(booking_id)
        if booking:
            d = request.get_json()
            booking = BookingDAO.update_booking(booking, d)
            return booking
        raise BusinessValidationError(404, "BOOKING101")

    @jwt_required()
    def delete(self, booking_id):
        booking = BookingDAO.get_booking(booking_id)
        is_deleted = BookingDAO.delete_booking(booking)
        if is_deleted:
            return jsonify({"message":"DELETED"})
        raise BusinessValidationError(404, "BOOKING101")

class LikeResource(Resource):
    @jwt_required()
    @marshal_with(like_fields)
    @cache.memoize()
    def get(self):
        likes = LikeDAO.get_likes()
        return likes

    @jwt_required()
    @marshal_with(like_fields)
    def post(self):
        d = request.get_json()
        like = LikeDAO.create_like(d)
        if like:
            return like

class LikeIdResource(Resource):
    @jwt_required()
    @marshal_with(like_fields)
    def get(self, like_id):
        like = LikeDAO.get_like(like_id)
        if like:
            return like
        raise BusinessValidationError(404, "LIKE101")

    @jwt_required()
    @marshal_with(like_fields)
    def put(self, like_id):
        like = LikeDAO.get_like(like_id)
        if like:
            d = request.get_json()
            like = LikeDAO.update_like(like, d)
            return like
        raise BusinessValidationError(404, "LIKE101")

    @jwt_required()
    def delete(self, like_id):
        like = LikeDAO.get_like(like_id)
        is_deleted = LikeDAO.delete_like(like)
        if is_deleted:
            return "Deleted Successfully", 200
        raise BusinessValidationError(404, "LIKE101")


class RatingReviewResource(Resource):
    @jwt_required()
    @marshal_with(rating_review_fields)
    @cache.memoize()
    def get(self):
        rating_reviews = RatingReviewDAO.get_rating_reviews()
        return rating_reviews

    @jwt_required()
    @marshal_with(rating_review_fields)
    def post(self):
        d = request.get_json()
        rating_review = RatingReviewDAO.create_rating_review(d)
        if rating_review:
            return rating_review
        else:
            raise BusinessValidationError(404, "RATING_REVIEW101")

class RatingReviewByMovieIdResource(Resource):
    # @jwt_required()
    @marshal_with(movie_rating_review_fields)
    @cache.memoize()
    def get(self, movie_id):
        rating_review = RatingReviewDAO.get_rating_reviews_by_movie(movie_id)
        return rating_review



class RatingReviewIdResource(Resource):
    @jwt_required()
    @marshal_with(movie_rating_review_fields)
    @cache.memoize()
    def get(self, rating_review_id):
        breakpoint()
        rating_review = RatingReviewDAO.get_rating_review(rating_review_id)
        if rating_review:
            return rating_review
        raise BusinessValidationError(404, "RATING_REVIEW101")

    @jwt_required()
    @marshal_with(rating_review_fields)
    def put(self, rating_review_id):
        rating_review = RatingReviewDAO.get_rating_review(rating_review_id)
        if rating_review:
            d = request.get_json()
            rating_review = RatingReviewDAO.update_rating_review(rating_review, d)
            return rating_review
        raise BusinessValidationError(404, "RATING_REVIEW101")

    @jwt_required()
    def delete(self, rating_review_id):
        rating_review = RatingReviewDAO.get_rating_review(rating_review_id)
        is_deleted = RatingReviewDAO.delete_rating_review(rating_review)
        if is_deleted:
            return jsonify({"message":"DELETED"})
        raise BusinessValidationError(404, "RATING_REVIEW101")
