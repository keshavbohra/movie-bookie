from flask_restx import Namespace, fields

screening_marshaller = {
    'screening_start': fields.DateTime(required=True, description='Screening start time'),
    'screening_end': fields.DateTime(required=True, description='Screening end time'),
    'seats_remain': fields.Integer(required=True, description='Remaining Seats')
}

booking_marshaller = {
    'booking_id': fields.Integer(attribute='id', required=True, description='Booking id'),
    'movie_name': fields.String(required=True, description='Movie Name'),
    'theatre_name': fields.String(required=True, description='Theatre Name'),
    'theatre_city': fields.String(required=True, description='Theatre City'),
    'screening_time': fields.DateTime(attribute='screening_start', required=True, description='Screening Start'),
    'movie_duration': fields.Integer(required=True, description='Duration of the movie.'),
    'total_seats': fields.Integer(required=True, description='Seats Booked')
}

screening_book_marshaller = {
    'screening_id': fields.Integer(attribute='id', required=True, description='Screening id'),
    'movie_id': fields.Integer(attribute='id', required=True, description='Movie id'),
    'theatre_id': fields.Integer(attribute='id', required=True, description='Theatre id'),
    'seats': fields.Integer(required=True, description='Seats Booked')
}

movie_marshaller = {
    'movie_id': fields.Integer(attribute='id', required=False, description='Movie id'),
    'movie_name': fields.String(required=True, description='Movie name'),
    'movie_duration': fields.Integer(required=True, description='Movie duration'),
    'poster_url': fields.String(required=True, description='Poster URL')
}

theatre_marshaller = {
    'theatre_id': fields.Integer(attribute='id', required=False, description='Theatre id'),
    'theatre_name': fields.String(required=True, description='Theatre name'),
    'theatre_city': fields.String(required=True, description='Theatre duration'),
    'seats_num': fields.Integer(attribute='seats_remain', required=True, description='Total Seats')
}

user_marshaller = {
    'username': fields.String(attribute='user_name', required=True, description='user username'),
    'email': fields.String(required=True, description='user email address'),
    'password': fields.String(required=True, description='user passw, ord'),
    'public_id': fields.String(required=False, description='user Identifier')
}

user_update_marshaller = {
    'email': fields.String(required=True, description='user email address'),
    'admin': fields.Boolean(required=True, description='User role flag')
}

auth_marshaller = {
    'email': fields.String(required=True, description='The email address'),
    'password': fields.String(required=True, description='The user password '),
}

class MovieDto:
    api = Namespace('movie', description='Movie related opertions')
    movie = api.model('movie_obj', movie_marshaller)

class BookingDto:
    api = Namespace('booking', description='Ticket Booking related operations')
    screening_model = api.model('screening_book', screening_book_marshaller)
    booking_model = api.model('booking', booking_marshaller)

class TheatreDto:
    api = Namespace('theatre', description='Theatre related opertions')
    theatre = api.model('theatre_obj', theatre_marshaller)

class ScreeningDto:
    api = Namespace('screening', description='Screening related opertions')
    screening = api.model('screening', screening_marshaller)
    movie_screening_marshaller = {**screening_marshaller, **theatre_marshaller}
    movie_screening = api.model('movie_screening', movie_screening_marshaller)
    theatre_screening_marshaller = {**screening_marshaller, **movie_marshaller}
    theatre_screening = api.model('theatre_screening', theatre_screening_marshaller)

class UserDto:
    api = Namespace('user', description='user related operations')
    user = api.model('user', user_marshaller)
    user_update = api.model('user_update', user_update_marshaller)

class AuthDto:
    api = Namespace('auth', description='authentication related operations')
    user_auth = api.model('auth_details', auth_marshaller)
