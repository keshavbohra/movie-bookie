from main import db
from main.model.movie import Movie
from main.model.theatre import Theatre
from main.model.screening import Screening

def add_new_movie(data):
    """
    Service method to add movie data to database
    """
    status = 409
    response_object = dict()
    
    movie = Movie.query.filter_by(movie_name=data['movie_name']).first()
    
    if not movie:
        new_movie = Movie(movie_name=data['movie_name'], movie_duration=data['movie_duration'], poster_url=data['poster_url'])
        commit_data(new_movie)
        
        response_object['status'] = 'Success'
        response_object['message'] = 'Successfully added movie information'
        status = 201
    
    else:
        response_object['status'] = 'Failure'
        response_object['message'] = 'Movie already present in the database'

    return response_object, status

def get_all_movies():
    return Movie.query.all()

def get_movie_by_name(data):
    # Movie.query.filter_by(movie_name=data).first()
    movie = Movie.query.filter(Movie.movie_name.ilike(data)).first()
    return movie

def get_movie_by_city(data):
    movies = Movie.query.join(Screening, Movie.id == Screening.movie_id).join(
        Theatre, (Screening.theatre_id == Theatre.id) & (Theatre.theatre_city.ilike(data))).all()
    return movies

def commit_data(data):
    db.session.add(data)
    db.session.commit()
