import unittest
from BookArray import *
from entities.Book import *


class JumpSearchTests(unittest.TestCase):
    def test_finding(self):
        books: list[Book] = [get_random_book_with_author(i) for i in range(10)]
        arr: BookArray = BookArray(books)
        for book in books:
            self.assertTrue(arr.jump_search(book.author) == book)

    def test_nonfinding(self):
        books: list[Book] = [get_random_book_with_author(i) for i in range(10)]
        arr: BookArray = BookArray(books)
        for book in [get_random_book_with_author(i) for i in range(11, 15)]:
            self.assertTrue(arr.jump_search(book.author) is None)

    def test_exception(self):
        books: list[Book] = [get_random_book_with_author(i) for i in range(9, 0, -1)]
        arr: BookArray = BookArray(books)
        with self.assertRaises(RuntimeError):
            arr.jump_search("")


if __name__ == '__main__':
    unittest.main()
