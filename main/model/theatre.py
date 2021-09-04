from .. import db

class Theatre(db.Model):
    """ 
        User Model for storing theatre related details 
    """
    __tablename__ = "theatres"
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    theatre_name = db.Column(db.String(255))
    theatre_city = db.Column(db.String(255))
    seats_num = db.Column(db.Integer)
    screening = db.relationship('Screening', lazy='dynamic', backref='theatre')
