from flask import request
from flask_restx import Resource

from ..utils.dto import UserDto
from ..service.user_service import save_new_user, get_all_users, get_a_user

api = UserDto.api
_user = UserDto.user

@api.route('/')
class UserList(Resource):
    @api.doc('List of registered users')
    @api.marshal_list_with(_user, envelope='data')
    def get(self):
        """
            List all registered users
        """
        return get_all_users()

    @api.response(201, 'User successfully created.')
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
    @api.marshal_with(_user)
    def get(self, public_id):
        """Get a user given its identifier"""
        user = get_a_user(public_id)
        if not user:
            api.abort(404)
        else:
            return user
