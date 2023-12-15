import os

from flask import Flask, request
from flask_restful import Api
from flask_cors import CORS

from config import LocalConfig
from application.model import db
from application.resources import jwt
from application.utils import cache
from application import routes

## Celery

from celery.result import AsyncResult
from application.worker import create_celery_app
from application import tasks

from flask_jwt_extended import JWTManager

app = Flask(__name__)

capp = create_celery_app(app)

app.config.from_object(LocalConfig)

CORS(app, origins="*")

api = Api(app)

cache.init_app(app)

jwt.init_app(app)

routes.register_api_routes(api, routes.get_api_routing())

db.init_app(app)



############################## celery test #####################
# @app.post("/sum")
# def sum():
#     a = request.form.get("a")
#     b = request.form.get("b")
#     s = tasks.sum.delay(int(a), int(b))
#     return str(s.id)

# @app.get('/get-sum/<id>')
# def get_sum(id):
#     s = AsyncResult(id)
#     res= {
#         "Ready": s.ready(),
#         "Result": s.result if s.ready() else None
#     }
#     return res
################################################################


with app.app_context():
    from application.dao import AdminDAO, Admin
    db.create_all()
    if not Admin.query.all():

        data = {
            "first_name": "Admin",
            "last_name": "Admin",
            "email": "ticketnow247@gmail.com",
            "password": os.environ["ADMIN_PASSWORD"]
        }
        admin = AdminDAO.create_admin(data);

app.app_context().push()

host="10.42.243.123"
port=5000

if __name__ == "__main__":
    app.run(host=host, port=port)
