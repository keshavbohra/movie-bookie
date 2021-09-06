from flask import Blueprint
from flask_restx import Api

from main.controller.user_controller import api as user_ns
from main.controller.auth_controller import api as auth_ns
from main.controller.movie_controller import api as movie_ns
from main.controller.theatre_controller import api as theatre_ns
from main.controller.booking_controller import api as booking_ns
from main.controller.screening_controller import api as screening_ns

blueprint = Blueprint('api', __name__)

authorizations = {
    'Bearer Auth': {
        'type': 'apiKey',
        'in': 'header',
        'name': 'Authorization'
    },
}

api = Api(blueprint, title='Flask RestX APIs', security='Bearer Auth', authorizations=authorizations, version='1.0', description='API endpoints for various functions.')

api.add_namespace(auth_ns)
api.add_namespace(user_ns, path='/user')
api.add_namespace(movie_ns, path='/movie')
api.add_namespace(theatre_ns, path='/theatre')
api.add_namespace(booking_ns, path='/booking')
api.add_namespace(screening_ns, path='/screening')
