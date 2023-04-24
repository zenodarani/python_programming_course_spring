from problemset_7_darani.assignment_2_darani.singly_linked_list import SinglyLinkedList

class Book:
    HORROR = "horror"
    FANTASY = "fantasy"
    THRILLER = "thriller"
    FICTION = "fiction"

    def __init__(self, title, author, year, genre):
        self.title = title
        self.author = author
        self.year = year
        self.genre = genre

    def __eq__(self, other):
        return self.title == other.title and self.author == other.author and self.year == other.year \
            and self.genre == other.genre

    def __str__(self):
        return f"{str.title(self.title)} - {str.title(self.author)}, {self.year}, {str.title(self.genre)}"


class Library:
    def __init__(self):
        self.books = SinglyLinkedList()

    def __str__(self):
        str_list = "Books:\n"
        for book in self.books:
            str_list += f"({str(book)})\n"
        return str_list

    # Given two books and a string attribute's name, compares which come first in alphabetic order. (Returns 'book_a'
    # if the two attributes are equivalent)
    def _compare_string(self, book_a, book_b, attribute):
        str_a = getattr(book_a, attribute)
        str_b = getattr(book_b, attribute)
        low_a = str.lower(str_a)
        low_b = str.lower(str_b)
        if low_a <= low_b:
            return book_a
        return book_b

    # Given two books returns the first in alphabetic order by the title
    def _compare_by_title(self, book_a, book_b):
        return self._compare_string(book_a, book_b, "title")

    # Given two books returns the first in alphabetic order by the author
    def _compare_by_author(self, book_a, book_b):
        return self._compare_string(book_a, book_b, "author")

    # Given two books returns the first in alphabetic order by the genre
    def _compare_by_genre(self, book_a, book_b):
        return self._compare_string(book_a, book_b, "genre")

    # Given two books returns the one with the year that comes first in ascending order
    def _compare_by_year(self, book_a, book_b):
        if min(book_a.year, book_b.year) == book_a.year:
            return book_a
        return book_b

    def add_book(self, book):
        self.books.add_node(book)

    def _bubble_sort(self, _comparable_func):
        swapped = True
        while swapped:
            swapped = False
            for i in range(len(self.books) - 1):
                book_a = self.books[i]
                book_b = self.books[i + 1]
                if _comparable_func(book_a, book_b) is book_b:
                    self.books.swap_nodes(i, i + 1)
                    swapped = True

    def sort_books_by_title(self):
        self._bubble_sort(self._compare_by_title)

    def sort_books_by_author(self):
        self._bubble_sort(self._compare_by_author)

    def sort_books_by_year(self):
        self._bubble_sort(self._compare_by_year)

    def sort_books_by_genre(self):
        self._bubble_sort(self._compare_by_genre)
