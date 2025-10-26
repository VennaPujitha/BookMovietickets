
from myexception import MovieAlreadyAvailableError, MovieNotAvailableError, TicketsNotAvailableError

class MovieInventory:
    movie = {}
 
    @staticmethod
    def add_movie(movie_obj):
        movie_name = movie_obj["movie_name"]
        ticket_count = movie_obj["tickets"]
        if movie_name in MovieInventory.movie:
            raise MovieAlreadyAvailableError(f"{movie_name} movie is already available")
        else:
            MovieInventory.movie[movie_name] = ticket_count
            print(f"Movie '{movie_name}' added successfully!")

    @staticmethod
    def show_movie_inventory():
        if not MovieInventory.movie:
            print("No Movie Available")
        else:
            for movie_name, tickets in MovieInventory.movie.items():
                print(f"{movie_name} - {tickets} tickets available")

    @staticmethod
    def find_movie(expected, finder):
        for movie_name in MovieInventory.movie:
            if finder(movie_name, expected):
                print(f"Movie '{movie_name}' found.")
                return movie_name
        raise MovieNotAvailableError(f"{expected} not found in inventory")

    @staticmethod
    def book_movie_tickets(movie_name, tickets):
        if movie_name not in MovieInventory.movie:
            raise MovieNotAvailableError(f"{movie_name} not available for booking.")
        available = MovieInventory.movie[movie_name]
        if tickets > available:
            raise TicketsNotAvailableError(f"Only {available} tickets available for {movie_name}")
        MovieInventory.movie[movie_name] -= tickets
        print(f"Booked {tickets} tickets for '{movie_name}'.")
 