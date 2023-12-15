from werkzeug.exceptions import HTTPException
from flask import make_response, jsonify

error_codes = {
    "ADMIN101": "NO_ADMIN_FOUND",
    "THEATRE101": "Theatre not found",
    "MOVIE101": "NOT_FOUND",
    "OTP104" : "Email ID is not Valid",
    "OTP102" : "INVALID_OTP",
    "PASS102": "INCORRECT_PASSWORD",
    "USER101": "NO_USER_FOUND",
    "USER102": "USER_EXISTS",
    "EMAIL102": "INVALID_EMAIL",
    "LOGOUT101": "Bad Request",
    "ACCESS101":"ACCESS_DENIED",
    "SCREEN101": "FAILED",
    "SCREEN102": "LIMIT_2_EXCEEDED",
    "SHOW101": "NOT_FOUND",
    "RATING_REVIEW101": "FAILED"

}

class BusinessValidationError(HTTPException):
    def __init__(self, status_code, error_code):
        message = {"error_code": error_code, "error_message": error_codes[error_code]}
        self.response = make_response(jsonify(message), status_code)
