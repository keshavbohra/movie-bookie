# Movie Booking Project

## Summary
A movie ticket booking application based on Python Flask's Restx APIs (backend only) with the power of JWT, SQLAlchemy ORMs.
## APIs
> Auth APIs
  * auth/login - This API reads the json object containing user email and password and retuns JWT Auth Token
  * auth/logout - This API reads the JWT Bearer Token from Authorization header and logs out the user

> User APIs 
  * user (GET)- Lists all the users present in the application. **(Need admin privilages to perform this action)**
  * user/register (POST)- Register a user based on the details given in the input json and retuns JWT Auth Token
  * user/update (POST)- Change user role based on the given input **(Need admin privilages to perform this action)**
  * user/<public_id> (GET)- Get the user information for the given id   ***(Need token information)***

>  Movie APIs
  * movie (GET)- Lists all movies registered in the application. **(Need admin privilages to perform this action)**
  * movie/add (POST)- Add movie information from input json to database **(Need admin privilages to perform this action)**
  * movie/<movie_name> (GET)- Get movie information for the given movie name
  * movie/city_name=<city_name> (GET)- Get movies currently screening in the given city
 
> Theatre APIs
  * theatre (GET)- Lists all theatres registered in the application. **(Need admin privilages to perform this action)**
  * theatre/add (POST)- Add theatre information from input json to database **(Need admin privilages to perform this action)**
  * theatre/<theatre_name> (GET)- Get list of theatre information for the given theatre's name
  * theatre/theatre_city=<theatre_city> (GET)- Get list of theatres currently screening movies in the given city
  
> Screening APIs
  * screening (GET)- Lists all screening currently registered in the application.  **(Need admin privilages to perform this action)**
  * screening (POST)- Add screening information from input json to database **(Need admin privilages to perform this action)**
  * screening/movie-screen (GET)- Lists all the screenings for the given movie and city details. *(Uses request parser to parse request paramerters)*
  * screening/theatre-screen (GET)- List all the screenings for the given theatre id. *(Uses request parser to parse request paramerters)*
  
> Booking APIs
  * booking (GET)-  Lists all the bookings for the user    ***(Need token information)***
  * booking (POST)- Creates a booking for the given movie, theatre, screening and user info  ***(Need token information)***
  * booking/<booking-id> (GET)- Get booking information for the given booking id  ***(Need token information)***
  
## System Architecture
  Please find the below diagram showcasing the system schema architecture of the developed application
  
  ![alt text](https://github.com/keshavbohra/movie_bookie/blob/main/db_schema.jpg?raw=true)

  Now, comes the fun part! :P
  
## Assumptions for the current version
  > Show Screenings - 
    * The API will take requried seats in the input body from user request to show only screenings which have remaining seats > required seats
    * The API will only show screenings which are starting one hour after current request timestamp
  > Seat Booking -
    * The API version assumes that the theater seats are homogenous in pricing and user seats aquiring occurs on theatre premisis on first come first serve basis and so application doesn't have to handle the complexity of seat mapping and seat holding.
  > Role Management - 
    * The current API only considers 2 roles namely, admin and user with a boolean column in the users table.

## Future Buils
  Future builds can have the below funcationalities:
  * Role management using flask-admin package
  * Seats API with temp seat locking for users while the user views.
  * Timezone conversions if we want to handle multiple timezones
  * Ticket pricing API to have a billing gateway *(maybe mockup for the timebeing)*
  
