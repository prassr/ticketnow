from dataclasses import dataclass
from flask_restful import Api, Resource
from application.resources import *


def get_api_routing():
    api_routing = {
        "api": {
            "v1": {
                "GET": "get_api_info",
                "RESOURCE": ApiInfo,
                "login": {
                    "POST": "check_user", 
                    "RESOURCE": LoginResource,
                    "otp": {
                        "POST": "",
                        "RESOURCE": OTPLoginResource
                    }
                },
                "signup": {
                    "otp": {
                        "POST": "",
                        "RESOURCE": OTPSignupResource
                    },
                },
                "password-reset-otp": {
                    "POST":"",
                    "RESOURCE": OTPResetPasswordResource
                },
                "password-reset": {
                    "POST": "",
                    "RESOURCE": ResetPasswordResource
                },
                "verify-otp" : {
                    "POST":"",
                    "RESOURCE": OTPVerifyResource
                },
                'logout': {
                    "GET": "",
                    "RESOURCE": LogOut
                },
                "admin": {
                    "generate-report": {
                        "GET": "",
                        "RESOURCE": AdminReportResource
                    },
                },
                "user": {
                    "GET": "get_users",
                    "POST": "create_user",
                    "RESOURCE": UserResource,
                    "u": {
                        "GET": "get_user",
                        "PUT": "update_user",
                        "DELETE": "delete_user",
                        "RESOURCE": UserIdResource,
                    },
                    "bookings": {
                        "GET": "",
                        "RESOURCE": UserBookingResource,
                    },
                },
                "theatre": {
                    "GET": "get_theatres",
                    "POST": "create_theatre",
                    "RESOURCE": TheatreResource,
                    "<int:theatre_id>": {
                        "GET": "get_theatre",
                        "PUT": "update_theatre",
                        "DELETE": "delete_theatre",
                        "RESOURCE": TheatreIdResource,
                    },
                    "shows": {
                            "GET": "",
                            "RESOURCE": ShowByTheatreIdResource
                    }
                },
                "screen": {
                    "GET": "get_screens",
                    "POST": "create_screen",
                    "RESOURCE": ScreenResource,
                    "<int:screen_id>": {
                        "GET": "get_screen",
                        "PUT": "update_screen",
                        "DELETE": "delete_screen",
                        "RESOURCE": ScreenIdResource,
                    },
                },
                "movie": {
                    "GET": "get_movies",
                    "POST": "create_movie",
                    "RESOURCE": MovieResource,
                    "<int:movie_id>": {
                        "GET": "get_movie",
                        "PUT": "update_movie",
                        "DELETE": "delete_movie",
                        "RESOURCE": MovieIdResource,
                        "rating_reviews": {
                            "GET": "",
                            "RESOURCE": RatingReviewByMovieIdResource,
                        },
                    },
                },
                "movie_show": { # fetch_movie for show
                    "GET": "get_movies",
                    "RESOURCE": MovieShowResource
                },
                "show": {
                    "GET": "get_shows",
                    "POST": "create_show",
                    "RESOURCE": ShowResource,
                    "<int:show_id>": {
                        "GET": "get_show",
                        "PUT": "update_show",
                        "DELETE": "delete_show",
                        "RESOURCE": ShowIdResource,
                    },
                },
                "booking": {
                    "GET": "get_bookings",
                    "POST": "create_booking",
                    "RESOURCE": BookingResource,
                    "<int:booking_id>": {
                        "GET": "get_booking",
                        "PUT": "update_booking",
                        "DELETE": "delete_booking",
                        "RESOURCE": BookingIdResource,
                    },
                    "show": {
                        "<int:show_id>": {
                            "GET": "",
                            "RESOURCE": BookingsByShowIdResource,
                            "seats_available": {
                                "GET": "",
                                "RESOURCE": SeatsAvailableResource,
                            },
                        },
                    },
                        
                },
                "like": {
                    "GET": "get_likes",
                    "POST": "create_like",
                    "RESOURCE": LikeResource,
                    "<int:like_id>": {
                        "GET": "get_like",
                        "PUT": "update_like",
                        "DELETE": "delete_like",
                        "RESOURCE": LikeIdResource,
                    },
                },
                "rating-review": {
                    "GET": "get_rating_reviews",
                    "POST": "create_rating_review",
                    "RESOURCE": RatingReviewResource,
                    "<int:rating_review_id>": {
                        "GET": "get_rating_review",
                        "PUT": "update_rating_review",
                        "DELETE": "delete_rating_review",
                        "RESOURCE": RatingReviewIdResource,
                    },
                },
            },
        },
    }
    return api_routing


@dataclass
class Route:
    method: str
    path: str
    handler: str


class ApiInfo(Resource):
    def get(self):
        api_routing = get_routing(get_api_routing())
        response = []
        for route in api_routing:
            if route.method == "RESOURCE":
                continue
            response.append(
                {
                    "method": route.method,
                    "path": route.path,
                }
            )
        return response


def print_routing(routing, prefix=""):
    for key, value in routing.items():
        if isinstance(value, dict):
            print_routing(value, prefix + "/" + key)
        elif key != "RESOURCE":
            print(f"{key:>10} {value.replace('_', ' '):40} {prefix}")


def get_routing(routing, prefix=""):
    routes = []
    for key, value in routing.items():
        if isinstance(value, dict):
            routes += get_routing(value, prefix + "/" + key)
        else:
            routes.append(Route(key, prefix, value))
    return routes


def get_routing_resources(routing, prefix=""):
    routes = []
    for key, value in routing.items():
        if isinstance(value, dict):
            routes += get_routing_resources(value, prefix + "/" + key)
        elif key == "RESOURCE":
            routes.append(Route(key, prefix, value))
    return routes


def register_api_routes(api: Api, routing, prefix=""):
    routes = get_routing_resources(routing, prefix)
    for route in routes:
        api.add_resource(route.handler, route.path)
        # print(f"Registering {route.method} {route.path}")


if __name__ == "__main__":
    print_routing(get_api_routing())
