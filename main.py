from movie import Movie
from inventory import MovieInventory
from myexception import MovieNotAvailableError, TicketsNotAvailableError, MovieAlreadyAvailableError
 
class MainClass:
    def read_movie_details():
        try:
            movie_name = input("Enter movie name: ")
            available_tickets = int(input("Enter available tickets: "))
            ticket_price = int(input("Enter the ticket price: "))
            movie = Movie(movie_name, available_tickets, ticket_price)
            MovieInventory.add_movie({
                "movie_name": movie.movie_name,
                "tickets": movie.available_tickets,
                "ticket_price": movie.ticket_price
            })
        except ValueError:
            print("Invalid ticket number.")
        except MovieAlreadyAvailableError as e:
            print(e.message)

    def show_inventory():
        MovieInventory.show_movie_inventory()

    def search_movie():
        try:
            name = input("Enter movie name to search: ")
            def finder(movie, expected):
                return movie.lower() == expected.lower()
            MovieInventory.find_movie(name, finder)
        except MovieNotAvailableError as e:
            print(e.message)

    def book_tickets():
        try:
            name = input("Enter movie name to book tickets for: ")
            tickets = int(input("Enter number of tickets to book: "))
            MovieInventory.book_movie_tickets(name, tickets)
        except MovieNotAvailableError as e:
            print(e.message)
        except TicketsNotAvailableError as e:
            print(e.message)
        except ValueError:
            print("Invalid ticket number.")

if __name__ == "__main__":
    while True:
        print("\n--- Movie Booking System ---")
        print("1. Add Movie")
        print("2. Show Inventory")
        print("3. Search Movie")
        print("4. Book Tickets")
        print("5. Exit")
        choice = input("Enter your choice: ")

        if choice == '1':
            MainClass.read_movie_details()
        elif choice == '2':
            MainClass.show_inventory()
        elif choice == '3':
            MainClass.search_movie()
        elif choice == '4':
            MainClass.book_tickets()
        elif choice == '5':
            print("Exiting...")
            break
        else:
            print("Invalid choice. Try again.")
