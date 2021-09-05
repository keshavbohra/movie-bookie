from flask import request
from flask_restx import Resource

from ..utils.dto import MovieDto
from ..service.movie_service import add_new_movie, get_all_movies, get_movie_by_name

api = MovieDto.api
_movie = MovieDto.movie

@api.route('/')
class MovieList(Resource):
    
    @api.doc('List of all the movies')
    @api.marshal_list_with(_movie, envelope='data')
    def get(self):
        """
            List all the movies
        """
        return get_all_movies()

    @api.response(201, 'Movie information added successfully.')
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
    
    @api.doc('get a movie')
    @api.marshal_with(_movie)
    def get(self, movie_name):
        """get a user given its identifier"""
        movie = get_movie_by_name(movie_name)
        if not movie:
            api.abort(404)
        else:
            return movie
