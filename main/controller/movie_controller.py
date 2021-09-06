from flask import request
from flask_restx import Resource

from ..utils.dto import MovieDto
from ..utils.decorators import admin_token_required
from ..service.movie_service import add_new_movie, get_all_movies, get_movie_by_name, get_movie_by_city

api = MovieDto.api
_movie = MovieDto.movie

@api.route('/')
class MovieList(Resource):
    
    @api.doc('List of all the movies')
    @admin_token_required
    @api.marshal_list_with(_movie, envelope='data')
    def get(self):
        """
            List all the movies
        """
        return get_all_movies()

@api.route('/add')
@api.response(409, 'Not authorized.')
class MovieAdd(Resource):

    @api.response(409, 'Not authorized.')
    @admin_token_required
    @api.doc('Add a new movie')
    @api.expect(_movie, validate=True)
    def post(self):
        """
            Add a new movie
        """
        data = request.json
        return add_new_movie(data=data)

@api.route('/<movie_name>')
@api.param('movie_name', 'The movie identifier')
@api.response(404, 'Movie not found.')
class Movie(Resource):
    @api.doc(security=None)
    @api.doc('get a movie')
    @api.marshal_with(_movie)
    def get(self, movie_name):
        """get a user given its identifier"""
        movie = get_movie_by_name(movie_name)
        if not movie:
            api.abort(404)
        else:
            return movie

@api.route('/city_name=<city_name>')
@api.param('city_name', 'City in which the movies are running')
@api.response(404, 'Movie not found.')
class MoviesInCity(Resource):
    
    @api.doc(security=None)
    @api.doc('get movies running in the city')
    @api.marshal_list_with(_movie, envelope='data')
    def get(self, city_name):
        """
            Get movies given its identifier
        """
        print(city_name)
        return get_movie_by_city(city_name)
