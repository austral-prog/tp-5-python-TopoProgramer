from src.Book import Book
from src.User import User


class Library:
    def __init__(self):
        self.__books = []
        self.__users = []
        self.__checked_out_books = []
        self.__checked_in_books = []

    # Getters
    def get_books(self)->list:
        return self.__books

    def get_users(self)->list:
        return self.__users

    def get_checked_out_books(self)->list:
        return self.__checked_out_books

    def get_checked_in_books(self)->list:
        return self.__checked_in_books

    # 1.1 Add Book
    def add_book(self, isbn, title, author)->None:
        libro = Book(isbn, title, author)  # Crear una instancia de Book
        self.__books.append(libro)  # Agregar la instancia a la lista de libros

    # 1.2 List All Books
    def list_all_books(self)->None:
            for book in self.__books:
                print(book)  # Esto llamará al método __str__ de Book para cada libro.

        # 2.1 Check out book
    def check_out_book(self, isbn, dni, due_date) -> str:
        # Buscar el libro por ISBN
        for libro in self.__books:
            if libro.get_isbn() == isbn:
                if not libro.is_available():
                    return f"Book {isbn} is not available"
                else:
                    # Marcar el libro como no disponible
                    libro.set_available(False)
                    self.__checked_out_books.append(libro)
                    for user in self.__users:
                        if user.get_dni() == dni:
                            user.increment_checkouts()
                            return f"User {dni} checked out book {isbn}"
        return f"Unable to find the data for the values: ISBN {isbn} and DNI: {dni}"

    # 2.2 Check in book
    def check_in_book(self, isbn, dni, returned_date) -> str:
        for libro in self.__books:
            if libro.get_isbn() == isbn:
                if not libro.is_available():
                    libro.set_available(True)
                    self.__checked_in_books.append(libro)
                    for user in self.__users:
                        if user.get_dni() == dni:
                            user.increment_checkins()
                            self.__checked_out_books.remove(libro)
                            return f"Book {isbn} checked in by user {dni}"
        return f"Book {isbn} is not available or already checked in"

    # Utils
    def add_user(self, dni, name)->None:
        user = User(dni, name)
        self.__users.append(user)   