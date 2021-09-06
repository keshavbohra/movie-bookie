import unittest
from datetime import datetime, timedelta
from test.base import BaseTestCase

from main import db
from main.model.user import User
from main.model.movie import Movie
from main.model.theatre import Theatre
from main.model.booking import Booking
from main.model.screening import Screening


def add_movie():
    movie = Movie(
        movie_name='Test Movie',
        movie_duration=200,
        poster_url='www.test.com/testMovie'
    )
    db.session.add(movie)
    db.session.commit()
    return movie

def add_theatre():
    theatre = Theatre(
        theatre_name='Test Theatre',
        theatre_city='Test City',
        seats_num=50
    )
    db.session.add(theatre)
    db.session.commit()
    return theatre

def add_user():
    user = User(
        email='test@test.com',
        password='test',
        registered_on=datetime.utcnow()
    )
    db.session.add(user)
    db.session.commit()
    return user

def add_screening(movie, theatre):
    screening = Screening(
        movie=movie,
        theatre=theatre,
        screening_start=datetime.now(),
        screening_end=datetime.now() + timedelta(minutes=movie.movie_duration),
        seats_remain=theatre.seats_num
    )
    db.session.add(screening)
    db.session.commit()
    return screening

def add_booking(user, screening):
    booking = Booking(
        screening=screening,
        user=user,
        total_seats=5
    )
    screening.seats_remain -= 5
    db.session.add(booking)
    db.session.add(screening)
    db.session.commit()
    return booking


class TestUserModelUser(BaseTestCase):
    
    def test_encode_auth_token(self):
        user = add_user()
        auth_token = User.encode_auth_token(user.id)
        self.assertTrue(isinstance(auth_token, str))

    def test_decode_auth_token(self):
        user = add_user()
        auth_token = User.encode_auth_token(user.id)
        self.assertTrue(isinstance(auth_token, str))
        self.assertTrue(User.decode_auth_token(auth_token) == user.id)

class TestUserModelMovie(BaseTestCase):

    def test_movie_insert(self):
        self.assertTrue(isinstance(add_movie().id, int))
    
    def test_movie_details_after_insert(self):
        self.assertTrue(isinstance(add_movie().id, int))
        self.assertTrue(isinstance(Movie.query.filter_by(movie_name='Test Movie').first(), Movie))

class TestUserModelTheatre(BaseTestCase):
    def test_theatre_insert(self):
        self.assertTrue(isinstance(add_theatre().id, int))
    
    def test_theatre_details_after_insert(self):
        self.assertTrue(isinstance(add_theatre().id, int))
        self.assertTrue(isinstance(Theatre.query.filter_by(theatre_name='Test Theatre').first(), Theatre))

class TestUserModelScreening(BaseTestCase):
    def test_screening_insert(self):
        theatre = add_theatre()
        movie = add_movie()
        self.assertTrue(isinstance(add_screening(movie, theatre).id, int))

    def test_screening_details_after_insert(self):
        theatre = add_theatre()
        movie = add_movie()
        self.assertTrue(isinstance(add_screening(movie, theatre).id, int))
        self.assertTrue(isinstance(Screening.query.join(Movie).filter_by(
            movie_name='Test Movie').first(), Screening))

class TestUserModelScreening(BaseTestCase):
    def test_booking_insert(self):
        theatre = add_theatre()
        movie = add_movie()
        user = add_user()
        screening = add_screening(movie, theatre)
        self.assertTrue(isinstance(add_booking(user, screening).id, int))

    def test_booking_details_after_insert(self):
        theatre = add_theatre()
        movie = add_movie()
        user = add_user()
        screening = add_screening(movie, theatre)
        self.assertTrue(isinstance(add_booking(user, screening).id, int))
        self.assertTrue(isinstance(Booking.query.join(Screening).join(Movie).filter_by(
            movie_name='Test Movie').first(), Booking))

    
if __name__ == '__main__':
    unittest.main()
