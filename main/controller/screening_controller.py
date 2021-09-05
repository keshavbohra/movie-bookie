from flask import request
from flask_restx import Resource, reqparse, inputs

from ..utils.dto import ScreeningDto
from ..service.screening_service import get_all_screenings, get_screening_of_movie, get_screening_of_theatre

api = ScreeningDto.api
_screening = ScreeningDto.screening
_movie_screening = ScreeningDto.movie_screening
_theatre_screening = ScreeningDto.theatre_screening

@api.route('/')
class ScreeningList(Resource):

    @api.doc('List of all the screenings')
    @api.marshal_list_with(_screening, envelope='data')
    def get(self):
        """
            List all the screenings
        """
        return get_all_screenings()

    # @api.response(201, 'Theatre information added successfully.')
    # @api.doc('Add a new theatre')
    # @api.expect(_screening, validate=True)
    # def post(self):
    #     """
    #         Add a new theatre
    #     """
    #     data = request.json
    #     return add_new_theatre(data=data)


@api.route('/movie-screen')
@api.response(404, 'No screenings present for the given details.')
class Movie(Resource):

    parser = reqparse.RequestParser()
    parser.add_argument('theatre_city', type=str,
                        help="City in which the theatre is present.",
                        default=True, required=True)
    parser.add_argument('movie_id', type=int,
                        help="Movie id for which the screening is required.",
                        default=True, required=True)

    @api.expect(parser)
    @api.doc('List all the screenings for the given movie and city details')
    @api.marshal_list_with(_movie_screening)
    def get(self):
        """
            List of all the screenings for the given movie and city details 
        """
        data = self.parser.parse_args()
        # data['theatre_city'] = request.args.get('theatre_city')
        # data['movie_id'] = request.args.get('movie_id')
        return get_screening_of_movie(data)


@api.route('/theatre-screen')
@api.response(404, 'There are no active screenings in the theatre.')
class Theatre(Resource):

    parser = reqparse.RequestParser()
    parser.add_argument('theatre_city', type=str,
                        help="City in which the theatre is present.",
                        default=True, required=True)
    parser.add_argument('theatre_id', type=int,
                        help="Theatre id for which the screening is required.",
                        default=True, required=True)

    @api.expect(parser)
    @api.doc('List all the screenings for the given theatre and city details')
    @api.marshal_list_with(_theatre_screening)
    def get(self):
        """
            List of all the screenings for the given theatre and city details 
        """
        data = self.parser.parse_args()
        # data['theatre_city'] = request.args.get('theatre_city')
        # data['movie_id'] = request.args.get('movie_id')
        return get_screening_of_movie(data)
