from flask import Blueprint
from flask_restx import Api

from main.controller.user_controller import api as user_ns
from main.controller.movie_controller import api as movie_ns
from main.controller.theatre_controller import api as theatre_ns
from main.controller.screening_controller import api as screening_ns

blueprint = Blueprint('api', __name__)

api = Api(blueprint, title='Flask RestX API', version='1.0', description='NA')

api.add_namespace(user_ns, path='/user')
api.add_namespace(movie_ns, path='/movie')
api.add_namespace(theatre_ns, path='/theatre')
api.add_namespace(screening_ns, path='/screening')
