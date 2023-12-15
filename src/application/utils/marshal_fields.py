from flask_restful import fields

from application.model import *

def get_theatre(show):
    theatre_id = Screen.query.filter_by(screen_id=show.screen_id).first().theatre_id
    theatre = Theatre.query.filter_by(theatre_id=theatre_id).first()
    return theatre


screen_fields = {
    "screen_id": fields.Integer,
    "tier_1": fields.Integer,
    "tier_2": fields.Integer,
    "tier_3": fields.Integer,
    "sound": fields.String,
    "is_recliner": fields.Boolean,
    "theatre_id": fields.Integer,
}


theatre_fields = {
    "theatre_id": fields.Integer,
    "name": fields.String,
    "address": fields.String,
    "city": fields.String,
    "state": fields.String,
    "zip_code": fields.String,
    "location": fields.String,
    "facilities": fields.String,
    "created_at": fields.DateTime,
    "modified_at": fields.DateTime,
    "screens": fields.Nested(screen_fields),
    # 'screen': fields.Nested(screen_fields)
}


booking_fields = {
    "booking_id": fields.Integer,
    "status" : fields.String,
    "seat_class": fields.String,
    "seat_no": fields.Integer,
    "amount_paid": fields.Integer,
    "show_id": fields.Integer,
    "user_id": fields.Integer,
}

show_fields = {
    "show_id": fields.Integer,
    "start_time": fields.DateTime,
    "language": fields.String,
    "price_1": fields.Integer,
    "price_2": fields.Integer,
    "price_3": fields.Integer,
    "screen_id": fields.Integer,
    "movie_id": fields.Integer,
    "theatre": fields.Nested(theatre_fields, attribute=get_theatre),
    "bookings": fields.Nested(booking_fields)
}

movie_for_show = {
    "movie_id": fields.Integer,
    "name": fields.String,
    # "poster": fields.String,
    "language": fields.String,
    "genres": fields.String,
    "type_d": fields.String,
    "runtime_min": fields.Integer,
    "release_date": fields.DateTime,

}

theatre_for_show = {
    "theatre_id": fields.Integer,
    "name": fields.String,
    "address": fields.String,
    "city": fields.String,
    "state": fields.String,
    "zip_code": fields.String,
    "location": fields.String,
    "facilities": fields.String,
}

show_for_show  = {
    "show_id": fields.Integer,
    "start_time": fields.DateTime,
    "price_1": fields.Integer,
    "price_2": fields.Integer,
    "price_3": fields.Integer,
    "screen_id": fields.Integer,
    "movie_id": fields.Integer,
}

booking_for_show = {
    "booking_id": fields.Integer,
    "status" : fields.String,
    "seat_class": fields.String,
    "seat_no": fields.Integer,
}

show_by_id_fields = {
    "show": fields.Nested(show_for_show),
    "theatre": fields.Nested(theatre_for_show),
    "movie": fields.Nested(movie_for_show),
    "screen": fields.Nested(screen_fields),
}

like_fields = {
    "like_id": fields.Integer,
    "user_id": fields.Integer,
    "movie_id": fields.Integer,
    "liked": fields.Boolean,
}

rating_review_fields = {
    "rating_review_id": fields.Integer,
    "rating": fields.Integer,
    "review": fields.String,
    "movie_id": fields.Integer,
    "user_id": fields.Integer,
}

user_fields = {
    "id": fields.Integer,
    "first_name": fields.String,
    "last_name": fields.String,
    "email": fields.String,
    # "password": fields.String,
    # "preferred_genres": fields.String,
    "bookings": fields.Nested(booking_fields),
    "likes": fields.Nested(like_fields),
    "rating_reviews": fields.Nested(rating_review_fields),
    "created_at": fields.DateTime,
    "modified_at": fields.DateTime,
}


screen_fields = {
    "screen_id": fields.Integer,
    "tier_1": fields.Integer,
    "tier_2": fields.Integer,
    "tier_3": fields.Integer,
    "sound": fields.String,
    "is_recliner": fields.Boolean,
    "theatre_id": fields.Integer,
}


theatre_fields = {
    "theatre_id": fields.Integer,
    "name": fields.String,
    "address": fields.String,
    "city": fields.String,
    "state": fields.String,
    "zip_code": fields.String,
    "location": fields.String,
    "facilities": fields.String,
    "created_at": fields.DateTime,
    "modified_at": fields.DateTime,
    "screens": fields.Nested(screen_fields),
    # 'screen': fields.Nested(screen_fields)
}


movie_fields = {
    "movie_id": fields.Integer,
    "name": fields.String,
    "poster": fields.String,
    "language": fields.String,
    "genres": fields.String,
    "runtime_min": fields.Integer,
    "release_date": fields.DateTime,
    "plot": fields.String,
    "cast": fields.String,
    "director": fields.String,
    "writer": fields.String,
    "certificate": fields.String,
    "type_d": fields.String,
    "created_at": fields.DateTime,
    "modified_at": fields.DateTime,

    "shows": fields.Nested(show_fields),
    "rating_reviews": fields.Nested(rating_review_fields),
    "likes": fields.Nested(like_fields),
}
#

movie_show_fields = {
    "movie_id": fields.Integer,
    "name": fields.String,
    "language": fields.String,
    "runtime_min": fields.Integer,
    "type_d": fields.String,
    "shows": fields.Nested(show_fields)
}
#
#
user_comp_fields = {
    "name": fields.String,
    
}
movie_rating_review_fields = {
    "rating_review_id": fields.Integer,
    "rating": fields.Integer,
    "review": fields.String,
    "name": fields.String,
}
