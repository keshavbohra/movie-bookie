from flask import request
from functools import wraps

from ..service.service_helper import Auth

def token_required(f):
    @wraps(f)
    def decorated(*args, **kwargs):
        data, status = Auth.get_logged_in_user(request)
        if not 'data' in list(data.keys()):
            return data, status
        # token = data['data']
        return f(*args, **kwargs)
    return decorated

def admin_token_required(f):
    @wraps(f)
    def decorated(*args, **kwargs):
        data, status = Auth.get_logged_in_user(request)
        if not 'data' in list(data.keys()):
            return data, status
        token = data['data']
        admin = token['admin']
        if not admin:
            response_object = {
                'status': 'failure',
                'message': 'User not authorized to perform this action.'
            }
            # print('User is not admin. So, returning the error response.')
            status = 401
            return response_object, status
        # print('User is admin. So proceeding to the service execution.')
        return f(*args, **kwargs)
    return decorated
