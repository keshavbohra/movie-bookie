from .. import db
from ..model.user import User
from ..model.movie import Movie
from ..model.booking import Booking
from ..model.theatre import Theatre
from ..model.screening import Screening

from datetime import datetime

def add_new_booking(token, data):
    """
    Service method to add booking of a screening
    """
    user_id = User.decode_auth_token(token)
    if not isinstance(user_id, str):
        screening = Screening.query.join(Movie).join(Theatre).filter((Movie.id == data['movie_id']) & (
            Theatre.id == data['theatre_id']) & (Screening.id == data['screening_id']) & (Screening.seats_remain >= data['seats'])).first()
        
        if screening:
            screening.seats_remain -= data['seats']
            commit_data(screening)
            booking = Booking(
                screening_id=screening.id,
                user_id=user_id,
                total_seats=data['seats']
            )
            commit_data(booking)
            
            response_object = {
                'status': 'Success',
                'message': 'Yay!! Booking completed! Have fun watching {}'.format(screening.movie.movie_name)
            }
            status = 201
        else:
            response_object = {
                'status': 'Failure',
                'message': 'Too late. Better luck next time.'
            }
            status = 404
    else:
        response_object = {
            'status': 'Failure',
            'message': 'Invalid token! Please login again to book the tickets.'
        }
        status = 401
    return response_object, status

def get_all_bookings(token):
    user_id = User.decode_auth_token(token)
    if not isinstance(user_id, str):
        return db.session.query(Booking.id, Movie.movie_name, Theatre.theatre_name, Theatre.theatre_city, Screening.screening_start, Movie.movie_duration, Booking.total_seats).join(User).join(Screening).join(Theatre).join(Movie).filter((User.id == user_id)).all()
    else:
        reponse_object = {
            'status': 'Failure',
            'message': 'Invalid Token. Please login again'
        }
        status = 401
        return reponse_object, status

def get_booking_by_id(token, data):
    user_id = User.decode_auth_token(token)
    if not isinstance(user_id, str):
        return db.session.query(Booking.id, Movie.movie_name, Theatre.theatre_name, Theatre.theatre_city, Screening.screening_start, Movie.movie_duration, Booking.total_seats).join(User).join(Screening).join(Theatre).join(Movie).filter(Booking.id == data).first()
    else:
        reponse_object = {
            'status': 'Failure',
            'message': 'Invalid Token. Please login again'
        }
        status = 401
        return reponse_object, status

def commit_data(data):
    db.session.add(data)
    db.session.commit()
