from main import db
from movie_service import add_new_movie, get_all_movies, get_movie_by_name
from theatre_service import add_new_theatre, get_all_theatres, get_theatre_by_name, get_theatres_by_city
from screening_service import 


def get_movie_list_by_city(data):
    """
    Service method to get list of all the movies which are running in the city
    """
    status = 404
    reponse_object = dict()
    
    theatres = get_theatre_by_name(data)

    print(theatres.screening)

    for theatre in theatres:


    return reponse_object, status
