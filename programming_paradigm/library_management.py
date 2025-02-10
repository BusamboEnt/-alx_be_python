# library_management.py

class Book:
    """
    Represents a book in the library.
    """
    def __init__(self, title, author):
        """
        Initializes a Book object.
        """
        self.title = title
        self.author = author
        self._is_checked_out = False  # Private attribute

    def check_out(self):
        """
        Marks the book as checked out.
        """
        self._is_checked_out = True

    def return_book(self):
        """
        Marks the book as returned (available).
        """
        self._is_checked_out = False

    def is_checked_out(self):
        """
        Returns True if the book is checked out, False otherwise.
        """
        return self._is_checked_out

    def __str__(self): # for easier debuggin
         return f"{self.title} by {self.author}"


class Library:
    """
    Represents a library that manages a collection of books.
    """
    def __init__(self):
        """
        Initializes a Library object.
        """
        self._books = []  # Private list to store books

    def add_book(self, book):
        """
        Adds a book to the library.
        """
        self._books.append(book)

    def check_out_book(self, title):
        """
        Checks out a book from the library, marking it as unavailable.
        """
        for book in self._books:
            if book.title == title and not book.is_checked_out():
                book.check_out()
                return
        print(f"Book '{title}' not found or already checked out.")

    def return_book(self, title):
        """
        Returns a book to the library, marking it as available.
        """
        for book in self._books:
            if book.title == title and book.is_checked_out():
                book.return_book()
                return
        print(f"Book '{title}' not found or already returned.")

    def list_available_books(self):
        """
        Lists all available books in the library.
        """
        available_books = [book for book in self._books if not book.is_checked_out()]
        if not available_books:
            print("No books available in the library.")
        else:
            for book in available_books:
                print(f"{book.title} by {book.author}")