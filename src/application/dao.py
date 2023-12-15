from typing import List, Literal, Union

from flask_restful import marshal_with
import re

import datetime

from sqlalchemy import text

from application.model import *

from werkzeug.security import generate_password_hash, check_password_hash

from application.utils import cache

from application.utils import user_fields


class AdminDAO:
    @classmethod
    def get_admin(cls):
        return Admin.query.first()

    @classmethod
    def create_admin(cls, data: dict):
        data["password"] = generate_password_hash(data["password"])
        admin = Admin(**data)
        db.session.add(admin)
        db.session.commit()
        return admin
    
    @classmethod
    def get_admin_by_email(cls, email):
        admin = Admin.query.filter_by(email=email).first()
        if admin:
            return admin
        else:
            return False

    @classmethod
    def update_admin(cls, admin: Admin, data: dict):
        try:
            data["password"] = generate_password_hash(data["password"])
        except:
            pass
        for key, value in data.items():
            setattr(admin, key, value)
        db.session.add(admin)
        db.session.commit()
        return admin


class PasswordResetDAO:
    @classmethod
    def reset_password(cls, user: Union[User, Admin], password):
        password = generate_password_hash(password)
        user.password = password
        db.session.commit()
        return True

class LoginDAO:
    @classmethod
    def check_password(cls, user: User, password):
        return check_password_hash(user.password, password)

class UserDAO:
    @classmethod
    def get_users(cls):
        return User.query.all()

    @classmethod
    def create_user(cls, data: dict):  # data is dictionary
        data["password"] = generate_password_hash(data["password"])
        user = User(**data)
        db.session.add(user)
        db.session.commit()
        return user

    @classmethod
    def get_user_by_email(cls, email: str):
        user = User.query.filter_by(email=email).first()
        if user:
            return user
        else:
            return False

    @classmethod
    def get_user_by_username(cls, username: str):
        user = User.query.filter_by(username=username).first()
        if user:
            return user
        else:
            return False

    @classmethod
    def get_user(cls, id: int):
        user = User.query.filter_by(id=id).first()
        if user:
            return user
        else:
            return False

    @classmethod
    def update_user(cls, user: User, data: dict):
        try:
            data["password"] = generate_password_hash(data["password"])
        except:
            pass
        for key, value in data.items():
            setattr(user, key, value)
        db.session.add(user)
        db.session.commit()
        return user

    @classmethod
    def delete_user(cls, user: User):
        try:
            db.session.delete(user)
            db.session.commit()
            return True
        except:
            return False

class TheatreDAO:
    
    @classmethod
    def get_theatres(cls):
        return Theatre.query.all()

    @classmethod
    def create_theatre(cls, data: dict):
        theatre = Theatre(**data)
        db.session.add(theatre)
        db.session.commit()
        cache.clear()
        return theatre

    
    @classmethod
    def get_theatre(cls, theatre_id):
        theatre = Theatre.query.filter_by(theatre_id=theatre_id).first()
        if theatre:
            return theatre
        else:
            return False



    @classmethod
    def filter_theatre(cls, **kwargs):
        if "name" in kwargs:
            theatres = Theatre.filter(name.ilike(f"%{kwargs['name']}%"))
        if "city" in kwargs:
            theatres = Theatre.filter(city.ilike(f"%{kwargs['city']}%"))
        if "facilities" in kwargs:
            facilities = kwargs["facilities"]
            theatres = Theatre.filter(facilities.op("~*")(rf"{facilities}"))
        if theatres:
            return theatres
        else:
            return False

    @classmethod
    def update_theatre(cls, theatre: Theatre, data: dict):
        for key, value in data.items():
            if value is not None:  # Check if the value is not None or null
                setattr(theatre, key, value)
        db.session.add(theatre)
        db.session.commit()
        cache.clear()
        return theatre

    @classmethod
    def delete_theatre(cls, theatre: Theatre):
        try:
            db.session.delete(theatre)
            db.session.commit()
            cache.clear()
            return True
        except:
            return False

    
    @classmethod
    def get_theatre_screens(cls, theatre: Theatre):
        return theatre.screens


class ScreenDAO:
    
    @classmethod
    def get_screens(cls):
        screens = Screen.query.all()
        return screens
    
    @classmethod
    def get_screen(cls, screen_id):
        screen = Screen.query.filter_by(screen_id=screen_id).first()
        if screen:
            return screen
        else:
            return False
    
    
    @classmethod
    def create_screen(cls, data: dict):
        screen = Screen(**data)
        db.session.add(screen)
        db.session.commit()
        cache.clear()
        return screen

    @classmethod
    def update_screen(cls, screen: Screen, data: dict):
        for key, value in data.items():
            if value is not None:  # Check if the value is not None or null
                setattr(screen, key, value)
        db.session.add(screen)
        db.session.commit()
        cache.clear()
        return screen

    @classmethod
    def delete_screen(cls, screen: Screen):
        try:
            db.session.delete(screen)
            db.session.commit()
            cache.clear()
            return True
        except:
            return False


class MovieDAO:
    
    @classmethod
    def get_movies(cls):
        movies = Movie.query.all()
        return movies

    @classmethod
    def create_movie(cls, data: dict):
        movie = Movie(**data)
        db.session.add(movie)
        db.session.commit()
        cache.clear()
        return movie

    
    @classmethod
    def get_movie(cls, movie_id):
        movie = Movie.query.filter_by(movie_id=movie_id).first()
        if movie:
            return movie
        else:
            return False

    @classmethod
    def update_movie(cls, movie: Movie, data: dict):
        for key, value in data.items():
            if value is not None:  # Check if the value is not None or null
                setattr(movie, key, value)
        db.session.add(movie)
        db.session.commit()
        cache.clear()
        return movie

    @classmethod
    def delete_movie(cls, movie: Movie):
        try:
            db.session.delete(movie)
            db.session.commit()
            cache.clear()
            return True
        except:
            return False

    @classmethod
    def get_movies_by_cast(cls, cast):
        movies = Movie.query.filter(cast.ilike(f"%{cast}%"))
        return movies

    @classmethod
    def get_movie_by_name(cls, name):
        movies = Movie.query.filter(name.ilike(f"%{name}%"))
        return movies

    @classmethod
    def get_movies_by_language(cls, language):
        movies = Movie.query.filter(language.ilike(f"%{language}%"))
        return movies

    @classmethod
    def get_movies_by_genre(cls, genre):
        movies = Movie.query.filter(language.ilike(f"%{genre}%"))
        return movies

    @classmethod
    def get_movies_by_date(cls, date):
        movies = Movie.query.filter_by(release_date=date).all()
        return movies

class JoinDAO:
    @classmethod
    def get_show(cls, show_id):
        result = db.session.query(Show, Theatre, Movie, Screen).filter(Show.show_id == show_id, Show.screen_id == Screen.screen_id, Theatre.theatre_id == Screen.theatre_id, Show.movie_id == Movie.movie_id
                                                                       ).first()
        return result
    
    @classmethod
    def get_rating_reviews(cls, movie_id):
        result = db.session.query(Movie, RatingReview).filter(
            Movie.movie_id == RatingReview.movie_id
        ).all();
        return result;


class ShowDAO:
    @classmethod
    def get_shows(cls):
        shows = Show.query.all()
        return shows

    @classmethod
    def create_show(cls, data: dict):
        show = Show(**data)
        db.session.add(show)
        db.session.commit()
        cache.clear()
        return show

    
    @classmethod
    def get_show(cls, show_id):
        show = Show.query.filter_by(show_id=show_id).first()
        if show:
            return show
        else:
            return False

    @classmethod
    def update_show(cls, show: Show, data: dict):
        for key, value in data.items():
            if value is not None:  # Check if the value is not None or null
                setattr(show, key, value)
        db.session.add(show)
        db.session.commit()
        cache.clear()
        return show

    @classmethod
    def delete_show(cls, show: Show):
        try:
            db.session.delete(show)
            db.session.commit()
            cache.clear()
            return True
        except:
            return False

    @classmethod
    def get_show_by_language(cls, language):
        show = Show.query.filter(language.ilike(f"%{language}%"))
        return show
    
    @classmethod
    def get_shows_by_theatre(cls):
        theatres = Theatre.query.all();
        data = {}
        for t in theatres:
            data[t.theatre_id] = {"theatre_name": t.name, 
                                  "address": t.address, 
                                  "city": t.city, 
                                  "facilities": t.facilities, 
                                  "state": t.state,
                                  "zip_code": t.zip_code,
                                  "shows": []
                                  }
            screens = Screen.query.filter_by(theatre_id = t.theatre_id).all()
            for s in screens:
                shows = Show.query.filter_by(show_id = s.screen_id).all()
                for sh in shows:
                    movie = Movie.query.filter_by(movie_id = sh.movie_id).first()
                    data[t.theatre_id]["shows"].append({
                        "show_id": sh.show_id,
                        "start_time": sh.start_time.strftime('%A, %d/%m/%Y %H:%M:%S'),
                        "movie_name": movie.name,
                        "movie_id": movie.movie_id,
                        "language": sh.language,
                        "is_recliner": s.is_recliner,
                        "sound": s.sound,
                        "screen_id": sh.screen_id,
                    })
        return data

# booking model
class BookingDAO:
    @classmethod
    def get_booking(cls, booking_id):
        booking = Booking.query.filter_by(booking_id=booking_id).first()
        if booking:
            return booking
        else:
            return False

    
    @classmethod
    def get_bookings_by_user(cls, user_id):
        query = text("""SELECT booking_id, show.show_id, show.movie_id, show.screen_id, screen.theatre_id, booking.seat_class, no_of_seats, price, start_time, show.language, movie.name,  runtime_min, sound, theatre.name, address, zip_code, facilities, booking.created_at
                        FROM Booking
                        JOIN Show ON Booking.show_id = Show.show_id
                        JOIN Movie ON Show.movie_id = Movie.movie_id
                        JOIN Screen ON Show.screen_id = Screen.screen_id
                        JOIN Theatre ON Screen.theatre_id = Theatre.theatre_id
                        WHERE Booking.user_id = :user_id """)
        bookings = db.session.execute(query, {"user_id": user_id}).all()
        bookings_ = []
        for booking in bookings:
            booking_ = {"booking_id": booking[0],
                        "show_id": booking[1],
                        "movie_id": booking[2],
                        "screen_id": booking[3],
                        "theatre_id": booking[4],
                        "seat_class": booking[5],
                        "no_of_seats": booking[6],
                        "price": booking[7],
                        "start_time": booking[8],
                        "language": booking[9],
                        "movie_name": booking[10],
                        "runtime_min": booking[11],
                        "sound": booking[12],
                        "theatre_name": booking[13],
                        "address": booking[14],
                        "zip_code": booking[15],
                        "facilities": booking[16],
                        "booked_on": booking[17]
                    }
            bookings_.append(booking_)
        return bookings_;

    @classmethod
    def get_bookings_by_show(cls, show_id):
        bookings = Booking.query.filter_by(show_id=show_id);
        return bookings;

    @classmethod
    def get_available_bookings_per_class(cls, show_id):
        show = ShowDAO.get_show(show_id)
        screen = ScreenDAO.get_screen(show.screen_id)
        bookings = cls.get_bookings_by_show(show_id)
        avail_seats = {"silver": screen.tier_1 , "gold": screen.tier_2, "platinum": screen.tier_3}
        for booking in bookings:
            avail_seats[booking.seat_class] = avail_seats[booking.seat_class] - booking.no_of_seats
        return avail_seats

    @classmethod
    def get_available_bookings_for_class(cls, show_id, class_):
        show = ShowDAO.get_show(show_id)
        screen = ScreenDAO.get_screen(show.screen_id)
        bookings = cls.get_bookings_by_show(show_id)
        class_seats = {"silver": screen.tier_1 , "gold": screen.tier_2, "platinum": screen.tier_3}
        data = {class_ : 0}
        for booking in bookings:
            if booking.seat_class == class_:
                data[class_] += booking.no_of_seats # later change it to no_of_seats
        data["capacity"] = class_seats[class_]
    
        return data



    @classmethod
    def create_booking(cls, data: dict):
        booking = Booking(**data)
        db.session.add(booking)
        db.session.commit()
        cache.clear()
        return booking

    @classmethod
    def update_booking(cls, booking: Booking, data: dict):
        for key, value in data.items():
            if value is not None:  # Check if the value is not None or null
                setattr(booking, key, value)
        db.session.add(booking)
        db.session.commit()
        cache.clear()
        return booking

    @classmethod
    def delete_booking(cls, booking: Booking):
        try:
            db.session.delete(booking)
            db.session.commit()
            cache.clear()
            return True
        except:
            return False

    @classmethod
    def generate_report(cls):
        bookings = Booking.query.all()
        data = []
        for booking in bookings:
            show = ShowDAO.get_show(booking.show_id)
            movie = MovieDAO.get_movie(show.movie_id)
            screen = ScreenDAO.get_screen(show.screen_id)
            theatre = TheatreDAO.get_theatre(screen.theatre_id)
            d = {"booking_id": booking.booking_id,
                 "booked_at": booking.created_at.strftime('%a, %d %b %Y %H:%M:%S'),
                 "movie": movie.name,
                 "start_time": show.start_time.strftime('%a, %d %b %Y %H:%M:%S'),
                 "venue": theatre.name,
                 "class": booking.seat_class,
                 "no_of_seats": booking.no_of_seats,
                 "price": booking.price,
                 "theatre_id": theatre.theatre_id
            }
            data.append(d)
        return data

# Likes
class LikesDAO:
    @classmethod
    def create_like(cls, data: dict):
        like = Like(**data)
        db.session.add(like)
        db.session.commit()
        cache.clear()
        return like

    @classmethod
    def update_like(cls, like: Like, data: dict):
        for key, value in data.items():
            if value is not None:  # Check if the value is not None or null
                setattr(like, key, value)
        db.session.add(like)
        db.session.commit()
        cache.clear()
        return like

    @classmethod
    def get_like(cls, like_id):
        like = like.query.filter_by(like_id=like_id).first()
        if like:
            return like
        else:
            return False

    @classmethod
    def delete_like(cls, like):
        try:
            db.session.delete(like)
            db.session.commit()
            cache.clear()
            return True
        except:
            return False


class RatingReviewDAO:
    @classmethod
    def create_rating_review(cls, data: dict):
        rating_review = RatingReview(**data)
        db.session.add(rating_review)
        db.session.commit()
        cache.clear()
        return rating_review

    @classmethod
    def update_rating_review(cls, rating_review: RatingReview, data: dict):
        for key, value in data.items():
            if value is not None:  # Check if the value is not None or null
                setattr(rating_review, key, value)
        db.session.add(rating_review)
        db.session.commit()
        cache.clear()
        return rating_review

    @classmethod
    def get_rating_review(cls, rating_review_id):
        rating_review = RatingReview.query.filter_by(
            rating_review_id=rating_review_id
        ).first()
        if rating_review:
            return rating_review
        else:
            return False

    @classmethod
    def get_rating_reviews_by_movie(cls, movie_id):
        rating_review = db.session.query(RatingReview, User.first_name).\
            join(User, User.id == RatingReview.user_id).\
            filter(RatingReview.movie_id == movie_id).all()
        if rating_review:
            res = []
            for (rr, name) in rating_review:
                res.append({
                    "rating_review_id": rr.rating_review_id,
                    "rating": rr.rating,
                    "review": rr.review,
                    "name": name,
                    "created_at": rr.created_at,
                    "modified_at": rr.modified_at
                })
            return res
        else:
            return False

    def delete_rating_review(cls, rating_review: RatingReview):
        try:
            db.session.delete(rating_review)
            db.session.commit()
            cache.clear()
            return True
        except:
            return False
