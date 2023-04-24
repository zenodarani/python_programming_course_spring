from book import Library
from book import Book

if __name__ == "__main__":
    my_library = Library()
    my_library.add_book(Book("Rosso", "Gino", 1989, "thriller"))
    my_library.add_book(Book("Giallo", "Dino", 2000, "horror"))
    my_library.add_book(Book("Blu", "Lino", 1829, "thriller"))
    my_library.add_book(Book("Verde", "Gaia", 1992, "thriller"))

    print("------- List of Books -------")
    print(my_library)

    print("------- Sorted by title -------")
    my_library.sort_books_by_title()
    print(my_library)

    print("------- Sorted by author -------")
    my_library.sort_books_by_author()
    print(my_library)

    print("------- Sorted by year -------")
    my_library.sort_books_by_year()
    print(my_library)

    print("------- Sorted by genre -------")
    my_library.sort_books_by_genre()
    print(my_library)


