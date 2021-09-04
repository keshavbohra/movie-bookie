from .main import db
from .main.model.movie import Movie
from .main.model.theatre import Theatre
from .main.model.screening import Screening

def add_new_screening(data):
    """
    Service method to add movie data to database
    """
    status = 409
    response_object = dict()

    movie = Movie.query.filter_by(.filter_by(movie_name=data['movie_name']).first())
    theatre = Theatre.query.filter_by(theatre_name=data['theatre_name'], theatre_city=data['theatre_city'])
    
    screening = Screening.query.filter_by(screening_name=data['screening_name']).first()
    
    if not screening:
        new_screening = Screening()
        commit_data(new_screening)
        
        response_object['status'] = 'Success'
        response_object['message'] = 'Successfully added screening information'
        status = 201
    
    else:
        response_object['status'] = 'Failure'
        response_object['message'] = 'Theatre already present in the database'

    return response_object, status

def get_all_screenings():
    return Screening.query.all()

def get_screening_by_theatre_name(data):
    return Screening.query.filter_by(theatre_name=data['theatre_name']).all()

def get_movies_by_city(data):
    screenings = Screening.query.filter_by(
        theatre_city=data['theatre_city']).all()
    movie_ids = [s.movie_id for s in screenings]
    movies = Movie.filter_by(Movie.id.in_(movie_ids)).all()
    return movies

def commit_data(data):
    db.session.add(data)
    db.session.commit()
