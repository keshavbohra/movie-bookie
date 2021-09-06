from .. import db
from ..model.movie import Movie
from ..model.theatre import Theatre
from ..model.screening import Screening

def add_new_screening(data):
    """
    Service method to add movie data to database
    """
    status = 409
    response_object = dict()

    movie = Movie.query.filter_by(id=data['movie_id']).first()
    theatre = Theatre.query.filter_by(
        id=data['theatre_id'], theatre_city=data['theatre_city'])
    
    screening = Screening.query.filter_by(theatre=theatre, movie=movie).first()
    
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

def get_screening_of_movie(data):
    screenings = db.session.query(Screening.id, Screening.screening_start, Screening.screening_end, Screening.seats_remain, Theatre.id, Theatre.theatre_name, Theatre.theatre_city).join(Theatre).join(Movie).filter((Theatre.theatre_city.ilike(data['theatre_city'])) & (Movie.id == data['movie_id'])).all()
    return screenings

def get_screening_of_theatre(data):
    screenings = db.session.query(Screening.id, Screening.screening_start, Screening.screening_end, Screening.seats_remain, Movie.id, Movie.movie_name, Movie.movie_duration,Movie.poster_url).join(Theatre).join(Movie).filter((Theatre.id.ilike(data['theatre_id']))).all()
    return screenings

def commit_data(data):
    db.session.add(data)
    db.session.commit()
