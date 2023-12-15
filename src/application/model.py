from flask_sqlalchemy import SQLAlchemy
import datetime

db = SQLAlchemy()


class BaseModel(object):
    created_at = db.Column(
        db.DateTime(), default=(datetime.datetime.now), nullable=False
    )
    modified_at = db.Column(
        db.DateTime(),
        default=(datetime.datetime.now),
        onupdate=(datetime.datetime.now),
        nullable=False,
    )


class User(BaseModel, db.Model):  # type: ignore
    id = db.Column(db.Integer, primary_key=True)
    first_name = db.Column(db.String(30), nullable=False)
    last_name = db.Column(db.String(30), nullable=False)
    email = db.Column(db.String(50), nullable=False, unique=True)
    password = db.Column(db.String(255), nullable=False)
    bookings = db.relationship(
        "Booking", backref="user", cascade="all, delete"
    )  # user has multiple bookings
    likes = db.relationship("Like", backref="user", cascade="all, delete")
    rating_reviews = db.relationship(
        "RatingReview", backref="user", cascade="all, delete"
    )

    def __init__(
        self, first_name, last_name, email, password
    ):
        self.first_name = first_name
        self.last_name = last_name
        self.email = email
        self.password = password

class Admin(BaseModel, db.Model):
    id = db.Column(db.Integer, primary_key=True)
    first_name = db.Column(db.String(30), nullable=False)
    last_name = db.Column(db.String(30), nullable=False)
    email = db.Column(db.String(50), nullable=False, unique=True)
    password = db.Column(db.String(255), nullable=False)
    # report_frequency

    def __init__(
        self, first_name, last_name, email, password
    ):
        self.first_name = first_name
        self.last_name = last_name
        self.email = email
        self.password = password

class Theatre(BaseModel, db.Model):  # type: ignore
    theatre_id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), nullable=False)
    address = db.Column(db.String(100), nullable=False)
    city = db.Column(db.String(30), nullable=False)
    state = db.Column(db.String(30), nullable=False)
    zip_code = db.Column(db.String(6), nullable=False)
    location = db.Column(db.String(42))  # google map link
    facilities = db.Column(db.String(100))
    screens = db.relationship("Screen", backref="theatre", cascade="all, delete")

    def __init__(
        self, name, address, city, state, zip_code, location, facilities
    ):
        self.name = name
        self.address = address
        self.city = city
        self.state = state
        self.zip_code = zip_code
        self.location = location
        self.facilities = facilities

  
class Screen(BaseModel, db.Model):  # type: ignore
    screen_id = db.Column(db.Integer, primary_key=True)
    tier_1 = db.Column(db.Integer, nullable=False)
    tier_2 = db.Column(db.Integer, nullable=False)
    tier_3 = db.Column(db.Integer, nullable=False)
    sound = db.Column(db.String(10), default="Dolby 7.1")
    is_recliner = db.Column(db.Boolean, default=False)  # type of tier_3 seats
    theatre_id = db.Column(
        db.Integer, db.ForeignKey("theatre.theatre_id"), nullable=False
    )

    def __init__(self, tier_1, tier_2, tier_3, sound, is_recliner, theatre_id):
        self.tier_1 = tier_1
        self.tier_2 = tier_2
        self.tier_3 = tier_3
        self.sound = sound
        self.is_recliner = is_recliner
        self.theatre_id = theatre_id


class Movie(BaseModel, db.Model):  # type: ignore
    movie_id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(120), nullable=False)
    poster = db.Column(db.String())
    language = db.Column(db.String(20), nullable=False)
    genres = db.Column(db.String(50), nullable=False)  # comma separated string
    runtime_min = db.Column(db.Integer, nullable=False)
    release_date = db.Column(db.DateTime(), nullable=False)
    plot = db.Column(db.String(5000))
    cast = db.Column(db.String(120), nullable=False)  # comma separated String
    director = db.Column(db.String(120), nullable=False)
    writer = db.Column(db.String(120))
    certificate = db.Column(db.String(6), nullable=False)
    shows = db.relationship("Show", backref="movie", cascade="all, delete")
    rating_reviews = db.relationship(
        "RatingReview", backref="movie", cascade="all, delete"
    )
    likes = db.relationship("Like", backref="movie", cascade="all, delete")

    def __init__(
        self,
        name,
        poster,
        language,
        genres,
        runtime_min,
        release_date,
        plot,
        cast,
        director,
        writer,
        certificate,
    ):
        self.name = name
        self.poster = poster
        self.language = language
        self.genres = genres
        self.runtime_min = runtime_min
        self.release_date = datetime.datetime.strptime(release_date, "%Y-%m-%d")
        self.plot = plot
        self.cast = cast
        self.director = director
        self.writer = writer
        self.certificate = certificate


class Show(BaseModel, db.Model):  # type: ignore
    show_id = db.Column(db.Integer, primary_key=True)
    start_time = db.Column(db.DateTime(), nullable=False)
    price_1 = db.Column(db.Integer, nullable=False)  # price for tier 1
    price_2 = db.Column(db.Integer, nullable=False)  # price for tier 2
    price_3 = db.Column(db.Integer, nullable=False)  # price for tier 3
    language = db.Column(db.String(30))
    screen_id = db.Column(db.Integer, db.ForeignKey("screen.screen_id"), nullable=False)
    movie_id = db.Column(db.Integer, db.ForeignKey("movie.movie_id"), nullable=False)
    bookings = db.relationship("Booking", backref="show", cascade="all, delete")

    def __init__(
        self, start_time, price_1, price_2, price_3, language, screen_id, movie_id
    ):
        self.start_time = start_time
        self.price_1 = price_1
        self.price_2 = price_2
        self.price_3 = price_3
        self.language = language
        self.screen_id = screen_id
        self.movie_id = movie_id


class Booking(BaseModel, db.Model):  # type: ignore
    booking_id = db.Column(db.Integer, primary_key=True)
    seat_class = db.Column(db.String(10), nullable=False)
    no_of_seats = db.Column(db.Integer, nullable=False)
    price = db.Column(db.Integer, nullable=False) 
    show_id = db.Column(db.Integer, db.ForeignKey("show.show_id"))
    user_id = db.Column(db.Integer, db.ForeignKey("user.id"), nullable=False)

    def __init__(self, seat_class, no_of_seats, price, show_id, user_id):
        self.seat_class = seat_class
        self.no_of_seats = no_of_seats
        self.price = price
        self.show_id = show_id
        self.user_id = user_id


class Like(BaseModel, db.Model):  # type: ignore
    like_id = db.Column(db.Integer, primary_key=True)
    user_id = db.Column(db.Integer, db.ForeignKey("user.id"), nullable=False)
    movie_id = db.Column(db.Integer, db.ForeignKey("movie.movie_id"), nullable=False)
    liked = db.Column(db.Boolean, nullable=False)

    def __init__(self, user_id, movie_id, liked):
        self.user_id = user_id
        self.movie_id = movie_id
        self.liked = liked


class RatingReview(BaseModel, db.Model):  # type: ignore
    rating_review_id = db.Column(db.Integer, primary_key=True)
    rating = db.Column(db.Integer, nullable=False)
    review = db.Column(db.String(20000))
    movie_id = db.Column(db.Integer, db.ForeignKey("movie.movie_id"), nullable=False)
    user_id = db.Column(db.Integer, db.ForeignKey("user.id"), nullable=False)

    def __init__(self, rating, movie_id, user_id, review=""):
        self.rating = rating
        self.review = review
        self.movie_id = movie_id
        self.user_id = user_id


# Register event listeners to update the timestamps
@db.event.listens_for(BaseModel, "before_insert")
def set_created_at(mapper, connection, target):
    target.created_at = datetime.datetime.now()


@db.event.listens_for(BaseModel, "before_update")
def set_updated_at(mapper, connection, target):
    target.modified_at = datetime.datetime.now()
