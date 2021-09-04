from flask_restx import Namespace, fields


# class ScreeningDto:
#     api = Namespace('screening', description='Screening related opertions')
#     screening = api.model('screening', )

screening_marshaller = {
    'screening_start': fields.DateTime(required=True, description='Screening start time'),
    'screening_end': fields.DateTime(required=True, description='Screening end time'),
    'seats_remain': fields.Integer(required=True, description='Remaining Seats')
}

class MovieDto:
    api = Namespace('movie', description='Movie related opertions')
    screening_model = api.model('screening', screening_marshaller)
    movie = api.model('movie', {
        'movie_name': fields.String(required=True, description='Movie name'),
        'movie_duration': fields.Integer(required=True, description='Movie duration'),
        'poster_url': fields.String(required=True, description='Poster URL'),
        'screening': fields.List(fields.Nested(screening_model), required=False)
    })

class TheatreDto:
    api = Namespace('theatre', description='Theatre related opertions')
    screening_model = api.model('screening', screening_marshaller)
    theatre = api.model('theatre', {
        'theatre_name': fields.String(required=True, description='Theatre name'),
        'theatre_city': fields.String(required=True, description='Theatre duration'),
        'seats_num': fields.Integer(required=True, description='Total Seats'),
        'screening': fields.List(fields.Nested(screening_model))
    })

class ScreeningDto:
    api = Namespace('screening', description='Movie related opertions')
    screening = api.model('screening', screening_marshaller)
    # movie = api.model('movie', {
    #     'movie_name': fields.String(required=True, description='Movie name'),
    #     'movie_duration': fields.Integer(required=True, description='Movie duration'),
    #     'poster_url': fields.String(required=True, description='Poster URL'),
    #     'screening': fields.List(fields.Nested(screening_model), required=False)
    # })
