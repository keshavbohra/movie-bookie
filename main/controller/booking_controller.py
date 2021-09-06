from flask import request
from flask_restx import Resource, reqparse, inputs

from ..utils.dto import BookingDto
from ..utils.decorators import token_required
from ..service.booking_service import add_new_booking, get_all_bookings, get_booking_by_id

api = BookingDto.api
_screening_model = BookingDto.screening_model
_booking_model = BookingDto.booking_model
 
@api.route('/')
class BookingList(Resource):
    
    parser = reqparse.RequestParser()
    parser.add_argument('Authorization', required=True, location='headers')

    @api.doc('List of all the movies')
    @token_required
    @api.expect(parser)
    @api.marshal_list_with(_booking_model, envelope='data')
    def get(self):
        """
            List all the bookings for the user
        """
        try:
            token = request.headers['Authorization'].split(' ')[1]
            return get_all_bookings(token)
        except Exception as e:
            response_object = {
                'status': 'Failure',
                'message': 'Token not present!!'
            }
            status = 401
            return response_object, status


    # @api.expect(parser)
    @api.response(201, 'Tickets Booked.')
    @token_required
    @api.doc('Add a new booking')
    @api.header('Authorization', description='Authorization header for checking if the request is valid.')
    @api.expect(_screening_model, validate=True)
    def post(self):
        """
            Add a new booking
        """
        try:
            data = request.json
            token = request.headers['Authorization'].split(' ')[1]
            return add_new_booking(token=token, data=data)
        except Exception as e:
            response_object = {
                'status': 'Failure',
                'message': 'Token not present!!'
            }
            status = 401
            return response_object, status
        
        # return add_new_booking(data=data)

@api.route('/<booking_id>')
@api.param('booking_id', 'The booking identifier')
@api.response(404, 'Booking not found.')
class Booking(Resource):

    parser = reqparse.RequestParser()
    parser.add_argument('Authorization', required=True, location='headers')
    
    @api.doc('get a booking')
    @token_required
    @api.expect(parser)
    @api.marshal_with(_booking_model)
    def get(self, booking_id):
        """
            Get a booking given its identifier
        """
        try:
            token = request.headers['Authorization'].split(' ')[1]
            return get_booking_by_id(token, booking_id)
        except Exception as e:
            response_object = {
                'status': 'Failure',
                'message': 'Token not present!!'
            }
            status = 401
            return response_object, status
