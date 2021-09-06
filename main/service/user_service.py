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
        response_object, status = generate_token(user)
    else:
        status = 409
        response_object = {
            'status': 'Failure',
            'message': 'User already exists. Please Log in.',
        }
    return response_object, status

def get_all_users():
    return User.query.all()

def update_user_role(data):
    user = User.query.filter_by(email=data['email']).first()
    if not user:
        status = 404
        response_object = {
            'status': 'Failure',
            'message': 'User not present.'
        }
    else:
        user.admin = data['admin']
        save_changes(user)
        status = 200
        response_object = {
            'status': 'Success',
            'message': 'User role updated succesfully.'
        }
    return response_object, status


def generate_token(user):
    try:
        auth_token = User.encode_auth_token(user.id)
        response_object = {
            'status': 'Success',
            'message': 'Successfully registered.',
            'Authorization': auth_token
        }
        return response_object, 201
    except Exception as e:
        response_object = {
            'status': 'Failure',
            'message': 'Some error occured. Please try again'
        }
        return response_object, 401

def get_a_user(public_id):
    return User.query.filter_by(public_id=public_id).first()

def save_changes(data):
    db.session.add(data)
    db.session.commit()
