import uuid
from datetime import datetime
from .. import db
from ..model.user import User

def save_new_user(data):
    user = User.query.filter_by(email=data['email']).first()
    if not user:
        user = User(
            email=data['email'],
            registered_on=datetime.utcnow(),
            public_id=str(uuid.uuid4()),
            user_name=data['username'],
            password=data['password']
        )
        save_changes(user)
        status = 201
        response_object = {
            'status': 'success',
            'message': 'User successfully registered.'
        }
    else:
        status = 409
        response_object = {
            'status': 'fail',
            'message': 'User already exists. Please Log in.',
        }
    return response_object, status

def get_all_users():
    return User.query.all()

def get_a_user(public_id):
    return User.query.filter_by(public_id=public_id).first()

def save_changes(data):
    db.session.add(data)
    db.session.commit()
