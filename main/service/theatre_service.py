from main import db
from main.model.theatre import Theatre
# from .main.model.movie import Movie
# from .main.model.screening import Screening

def add_new_theatre(data):
    """
    Service method to add movie data to database
    """
    status = 409
    response_object = dict()
    
    theatre = Theatre.query.filter_by(theatre_name=data['theatre_name']).first()
    
    if not theatre:
        new_theatre = Theatre(
            theatre_name=data['theatre_name'], theatre_city=data['theatre_city'], seats_num=data['seats_num'])
        commit_data(new_theatre)
        
        response_object['status'] = 'Success'
        response_object['message'] = 'Successfully added theatre information'
        status = 201
    
    else:
        response_object['status'] = 'Failure'
        response_object['message'] = 'Theatre already present in the database'

    return response_object, status

def get_all_theatres():
    return Theatre.query.all()

def get_theatre_by_name(data):
    # Theatre.query.filter_by(theatre_name=data).first()
    return Theatre.query.filter(Theatre.theatre_name.ilike(data)).first()

def get_theatres_by_city(data):
    # Theatre.query.filter_by(theatre_city=data).all()
    return Theatre.query.filter(Theatre.theatre_city.ilike(data)).all()

def commit_data(data):
    db.session.add(data)
    db.session.commit()
