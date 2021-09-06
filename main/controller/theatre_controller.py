from flask import request
from flask_restx import Resource

from ..utils.dto import TheatreDto
from ..utils.decorators import admin_token_required
from ..service.theatre_service import add_new_theatre, get_all_theatres, get_theatre_by_name, get_theatres_by_city

api = TheatreDto.api
_theatre = TheatreDto.theatre


@api.route('/')
class TheatreList(Resource):

    @api.doc(security=None)
    @api.doc('List of all the theatres')
    @admin_token_required
    @api.marshal_list_with(_theatre, envelope='data')
    def get(self):
        """
            List all the theatres
        """
        return get_all_theatres()

@api.route('/add')
@api.response(409, 'Not authorized.')
class TheatreAdd(Resource):

    @api.response(409, 'Not authorized.')
    @admin_token_required
    @api.doc('Add a new theatre')
    @api.expect(_theatre, validate=True)
    def post(self):
        """
            Add a new theatre
        """
        data = request.json
        return add_new_theatre(data=data)

@api.route('/<theatre_city>')
@api.param('theatre_city', 'The theatre identifier')
@api.response(404, 'No theatres for the given city.')
class Theatres(Resource):
    
    @api.doc(security=None)
    @api.doc('List of all the theatres for the given city')
    @api.marshal_list_with(_theatre, envelope='data')
    def get(self, theatre_city):
        """
            List of all the theatres for the given city
        """
        return get_theatres_by_city(theatre_city)


@api.route('/<theatre_name>')
@api.param('theatre_name', 'The theatre identifier')
@api.response(404, 'Theatre not found.')
class Theatre(Resource):

    @api.doc('get a theatre')
    @api.marshal_with(_theatre)
    def get(self, theatre_name):
        """get a theatre given its identifier"""
        theatre = get_theatre_by_name(theatre_name)
        if not theatre:
            api.abort(404)
        else:
            return theatre
