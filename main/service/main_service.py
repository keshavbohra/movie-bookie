from main import db
from main.model.movie import Movie
from main.model.theatre import Theatre
from main.model.booking import Booking
from main.model.screening import Screening
# from movie_service import add_new_movie, get_all_movies, get_movie_by_name
# from theatre_service import add_new_theatre, get_all_theatres, get_theatre_by_name, get_theatres_by_city
# from screening_service import get_all_screenings


def get_movie_list_by_city(data):
    """
        Service method to get list of all the movies which are running in the city
    """
    movies = Movie.query.join(Screening, Movie.id == Screening.movie_id).join(
        Theatre, (Screening.theatre_id == Theatre.id) & (Theatre.theatre_city.ilike('Bangalore'))).all()

    return movies

def get_screenings_of_movie(data):
    """
        Service method to get list of all the screenings which are running in the city for te movie.
    """
    screenings = Screening.query.join(Theatre).join(Movie).filter((Theatre.theatre_city.ilike(data['theatre_city'])) & (Movie.id == data['movie_id']))
    return screenings

def book_screening_of_movie(data):
    """
        Service method to book tickets for the movie screening.
    """
    status = 409
    response_object = dict()

    #TODO add the ticket model for update

    screening = Screening.populate_existing().with_for_update().filter((Screening.id == data['screening_id']) & (
        Screening.seats_remain >= data['total_seats'])).first()
    
    if screening:
        screening.seats_remain -= data['total_seats']
        commit_data(screening)
        booking = Booking(screening=screening, total_seats=data['total_seats'], user=data['user'])
        commit_data(booking)

        response_object['status'] = 200
        response_object['message'] = 'Tickets booked successfully!!'

    return response_object, status

def commit_data(data):
    db.session.add(data)
    db.session.commit()
