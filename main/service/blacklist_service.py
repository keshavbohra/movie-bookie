from .. import db
from ..model.blacklist import BlacklistToken

def save_token(token):
    blacklist_token = BlacklistToken(token=token)
    try:
        commit_data(blacklist_token)
        response_object = {
            'status': 'success',
            'message': 'Successfully logged out.'
        }
        return response_object, 200
    except Exception as e:
        response_object = {
            'status': 'failure',
            'message': e
        }
        return response_object, 200

def commit_data(data):
    db.session.add(data)
    db.session.commit()
