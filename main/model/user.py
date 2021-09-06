import jwt
from datetime import datetime, timedelta
from .. import db
from ..model.blacklist import BlacklistToken
from ..config import key

class User(db.Model):
    """ 
        User Model for storing user related details 
    """
    __tablename__ = "users"
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    admin = db.Column(db.Boolean, nullable=False, default=False)
    email = db.Column(db.String(255), unique=True, nullable=False)
    registered_on = db.Column(db.DateTime, nullable=False, default=datetime.utcnow)
    public_id = db.Column(db.String(255), unique=True)
    user_name = db.Column(db.String(255), unique=True)
    password = db.Column(db.String(255))
    booking = db.relationship('Booking', lazy='dynamic', backref='user')

    def check_password(self, password):
        return self.password.__eq__(password)

    def __repr__(self):
        return "<User : '{}'>".format(self.user_name)
    
    @staticmethod
    def encode_auth_token(user_id):
        """
            Generates and encodes the Auth Token for the given user_id.
            :return: string
        """
        try:
            payload = {
                'exp': datetime.utcnow() + timedelta(days=1, seconds=5),
                'iat': datetime.utcnow(),
                'sub': user_id
            }
            return jwt.encode(payload=payload, key=key, algorithm='HS256')
        except Exception as e:
            return e
    
    @staticmethod
    def decode_auth_token(token):
        """
            Decodes and checks status of the given Auth Token.
            :return: integer|string
        """
        try:
            payload = jwt.decode(jwt=token, key=key, algorithms='HS256')
            is_black_listed_token = BlacklistToken.check_blacklist(payload)
            
            if is_black_listed_token:
                return 'Token is blacklisted. Please log in again.'
            else:
                return payload['sub']
        except jwt.ExpiredSignatureError:
            return 'Signature expired. Please log in again.'
        except jwt.InvalidTokenError:
            return 'Invalid token. Please log in again'
