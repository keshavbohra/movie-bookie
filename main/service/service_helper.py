from ..model.user import User
from ..service.blacklist_service import save_token

class Auth:
    """
        Helper class for Authentication
    """

    @staticmethod
    def login_user(data):
        try:
            user = User.query.filter_by(email=data['email']).first()
            if user and user.check_password(data['password']):
                auth_token = User.encode_auth_token(user.id)

                if auth_token:
                    response_object = {
                        'status': 'success',
                        'message': 'Successfully logged in.',
                        'Authorization': auth_token
                    }
                    status = 200
            else:
                response_object = {
                    'status': 'failure',
                    'message': 'Email or password not matching'
                }
                status = 401
            return response_object, status
        except Exception as e:
            print(e)
            response_object = {
                'status': 'fail',
                'message': 'Some error occured. Try again.'
            }
            status = 500
            return response_object, status

    @staticmethod
    def logout_user(data):
        if data:
            auth_token = data.split(' ')[1]
        else:
            auth_token = ''
        
        if auth_token:
            resp = User.decode_auth_token(auth_token)
            if not isinstance(resp, str):
                # The token is valid with reponse containing user_id
                return save_token(token=auth_token)
            else:
                response_object = {
                    'status': 'failure',
                    'message': resp
                }
                return response_object, 401
        else:
            response_object = {
                'status': 'failure',
                'message': 'Provide a valid auth token for the user.'
            }
            return response_object, 403
    
    @staticmethod
    def get_logged_in_user(request_obj):
        data = request_obj.headers.get('Authorization')
        if data:
            auth_token = data.split(' ')[1]
        else:
            auth_token = ''
        if auth_token:
            response = User.decode_auth_token(auth_token)
            if not isinstance(response, str):
                user = User.query.filter_by(id=response).first()
                response_object = {
                    'status': 'success',
                    'data': {
                        'user_id': user.id,
                        'email': user.email,
                        'admin': user.admin,
                        'registered_on': str(user.registered_on)
                    }
                }
                return response_object, 200
            
            response_object = {
                'status': 'failure',
                'message': response
            }
            return response_object, 401
        else:
            response_object = {
                'status': 'fail',
                'message': 'Provide a valid auth token.'
            }
            return response_object, 401
