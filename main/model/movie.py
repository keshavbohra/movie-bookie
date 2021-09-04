from .. import db

class Movie(db.Model):
    """ 
        User Model for storing movie related details 
    """
    __tablename__ = "movies"
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    movie_name = db.Column(db.String(255))
    movie_duration = db.Column(db.Integer)
    poster_url = db.Column(db.String(255), unique=True)
    screening = db.relationship('Screening', lazy='dynamic', backref='movie')
