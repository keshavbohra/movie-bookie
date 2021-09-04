from flask import Blueprint
from flask_restx import Api

from main.controller.movie_controller import api as movie_ns
from main.controller.theatre_controller import api as theatre_ns

blueprint = Blueprint('api', __name__)

api = Api(blueprint, title='Flask RestX API', version='1.0', description='NA')

api.add_namespace(movie_ns, path='/movie')
api.add_namespace(theatre_ns, path='/theatre')
