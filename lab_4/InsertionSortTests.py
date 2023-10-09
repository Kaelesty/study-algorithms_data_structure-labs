import unittest
from BookArray import *
from entities.Book import *


def pages_list_to_book_list(pages: list[int]) -> list[Book]:
    return list(map(lambda x: get_random_book_with_pages(x) if x is not None else None, pages))


def are_bookArrays_eq_by_pages(arr_0: BookArray, arr_1: BookArray) -> bool:
    return list(map(lambda x: x.pages if x is not None else None, arr_0.items)) == list(map(lambda x: x.pages if x is not None else None, arr_1.items))


class InsertionSortTests(unittest.TestCase):

    def test_empty(self):
        self.assertTrue(BookArray([]) == BookArray([]).insertion_pages())

    def test_matching(self):
        self.assertTrue(are_bookArrays_eq_by_pages(
            BookArray(pages_list_to_book_list([1, 2, 3])),
            BookArray(pages_list_to_book_list([3, 1, 2])).insertion_pages()))
        self.assertTrue(are_bookArrays_eq_by_pages(
            BookArray(pages_list_to_book_list([1, 1, 1])),
            BookArray(pages_list_to_book_list([1, 1, 1])).insertion_pages()))
        self.assertTrue(are_bookArrays_eq_by_pages(
            BookArray(pages_list_to_book_list([2, 5, 5])),
            BookArray(pages_list_to_book_list([5, 2, 5])).insertion_pages()))

    def test_mismatching(self):
        self.assertFalse(are_bookArrays_eq_by_pages(
            BookArray(pages_list_to_book_list([1, 2, 3])),
            BookArray(pages_list_to_book_list([3, 1, 3])).insertion_pages()))
        self.assertFalse(are_bookArrays_eq_by_pages(
            BookArray(pages_list_to_book_list([1, 2, 3])),
            BookArray(pages_list_to_book_list([3, 1, 2, 4])).insertion_pages()))
        self.assertFalse(are_bookArrays_eq_by_pages(
            BookArray(pages_list_to_book_list([1, 2, 3])),
            BookArray(pages_list_to_book_list([])).insertion_pages()))
        self.assertFalse(are_bookArrays_eq_by_pages(
            BookArray(pages_list_to_book_list([5, 2, 5])),
            BookArray(pages_list_to_book_list([2, 5, 2])).insertion_pages()))

    def test_nones(self):
        self.assertTrue(
            BookArray(pages_list_to_book_list([2, 2, 5, None])),
            BookArray(pages_list_to_book_list([2, None, 5, 2])).insertion_pages()
        )


if __name__ == '__main__':
    unittest.main()