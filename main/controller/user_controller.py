from flask import request
from flask_restx import Resource

from ..utils.dto import UserDto
from..utils.decorators import token_required, admin_token_required
from ..service.user_service import save_new_user, get_all_users, get_a_user, update_user_role

api = UserDto.api
_user = UserDto.user
_user_update = UserDto.user_update

@api.route('/')
class UserList(Resource):
    @api.doc('List of registered users')
    @admin_token_required
    @api.marshal_list_with(_user, envelope='data')
    def get(self):
        """
            List all registered users
        """
        return get_all_users()

@api.route('/update')
class UserUpdate(Resource):
    
    @admin_token_required
    @api.response(401, 'User not authorized to perform the action.')
    @api.doc('Update a user from user role to admin role')
    @api.expect(_user_update, validate=True)
    def post(self):
        data = request.json
        return update_user_role(data)

@api.route('/register')
class UserRegister(Resource):
    
    @api.response(500, 'Internal Server error.')
    @api.doc('Create new user')
    @api.expect(_user, validate=True)
    def post(self):
        data = request.json
        return save_new_user(data)


@api.route('/<public_id>')
@api.param('public_id', 'The User identifier')
@api.response(404, 'User not found.')
class User(Resource):
    @api.doc('Get a user for the given public id')
    @token_required
    @api.marshal_with(_user)
    def get(self, public_id):
        """Get a user given its identifier"""
        user = get_a_user(public_id)
        if not user:
            api.abort(404)
        else:
            return user
