from flask import request
from flask_restx import Resource, reqparse, inputs

from ..service.service_helper import Auth
from ..utils.dto import AuthDto

api = AuthDto.api
_user_auth = AuthDto.user_auth

@api.doc(security=None)
@api.route('/login')
class LoginAPIController(Resource):
    """
        User login Resource
    """

    @api.doc('User login')
    @api.expect(_user_auth, validate=True)
    def post(self):
        data = request.json
        return Auth.login_user(data=data)
    
@api.route('/logout')
class LogoutAPIController(Resource):
    """
        User logout Resource
    """
    # api.authorizations = {"Bearer": {"type": "apiKey",
    #                                  "in": "header", "name": "Authorization"}}
    
    parser = reqparse.RequestParser()
    parser.add_argument('Authorization', required=True, location='headers')
    
    @api.expect(parser)
    @api.doc('User logout')
    def post(self):
        data = request.headers['Authorization']
        return Auth.logout_user(data=data)
