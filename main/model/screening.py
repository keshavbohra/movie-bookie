from .. import db
from .user import User
from .movie import Movie
from .theatre import Theatre
from datetime import datetime, timedelta

class Screening(db.Model):
    """ 
        User Model for storing theatre related details 
    """
    __tablename__ = "screening"
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    movie_id = db.Column(db.Integer, db.ForeignKey('movies.id'))
    theatre_id = db.Column(db.Integer, db.ForeignKey('theatres.id'))
    screening_start = db.Column(db.DateTime, nullable=False, default=datetime.now)
    screening_end = db.Column(db.DateTime, nullable=False, default=datetime.now)
    seats_remain = db.Column(db.Integer)
    bookings = db.relationship('Booking', lazy='dynamic', backref='screening')

