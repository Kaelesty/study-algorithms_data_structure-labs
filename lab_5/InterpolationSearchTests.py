import unittest
from BookArray import *
from entities.Book import *


class InterpolationSearchTests(unittest.TestCase):
    def test_finding(self):
        books: list[Book] = [get_random_book_with_pages(i) for i in range(10)]
        arr: BookArray = BookArray(books)
        for book in books:
            self.assertTrue(arr.interpolation_search(book.pages) == book)

    def test_nonfinding(self):
        books: list[Book] = [get_random_book_with_pages(i) for i in range(10)]
        arr: BookArray = BookArray(books)
        for book in [get_random_book_with_author(i) for i in range(11, 15)]:
            self.assertTrue(arr.interpolation_search(book.pages) is None)

    def test_exception(self):
        books: list[Book] = [get_random_book_with_pages(i) for i in range(9, 0, -1)]
        arr: BookArray = BookArray(books)
        with self.assertRaises(RuntimeError):
            arr.interpolation_search(11)


if __name__ == '__main__':
    unittest.main()
