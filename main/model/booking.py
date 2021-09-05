from .. import db


class Booking(db.Model):
    """ 
        User Model for storing booking related details 
    """
    __tablename__ = "booking"
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    screening_id = db.Column(db.Integer, db.ForeignKey('screening.id'))
    user_id = db.Column(db.Integer, db.ForeignKey('users.id'))
    total_seats = db.Column(db.Integer)
