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

    # Returns the first string in alphabetic order
    def _compare_string(self, str_a, str_b):
        str_a = str.lower(str_a)
        str_b = str.lower(str_b)
        if str_a < str_b:
            return str_a
        return str_b

    # Given two books returns the first in alphabetic order by the title
    def _compare_by_title(self, book_a, book_b):
        if self._compare_string(book_a.title, book_b.title) == book_a.title:
            return book_a
        return book_b

    # Given two books returns the first in alphabetic order by the author
    def _compare_by_author(self, book_a, book_b):
        if self._compare_string(book_a.author, book_b.author) == book_a.author:
            return book_a
        return book_b

    # Given two books returns the first in alphabetic order by the genre
    def _compare_by_genre(self, book_a, bool_b):
        if self._compare_string(book_a.genre, bool_b.genre) == book_a.genre:
            return book_a
        return bool_b

    # Given two books returns the one with the year that comes first in ascending order
    def _compare_by_year(self, book_a, book_b):
        if min(book_a.year, book_b.year) == book_a.year:
            return book_a
        return book_b

    def add_book(self, book):
        self.books.add_node(book)

    def sort_books_by_title(self):
        for i in range(len(self.books) - 1):
            if self._compare_by_title(self.books[i], self.books[i + 1]).title == self.books[i + 1].title:
                self.books.swap_nodes(i, i+1)

