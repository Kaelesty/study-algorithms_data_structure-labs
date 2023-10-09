import unittest
from BookArray import *
from entities.Book import *


def authors_list_to_book_list(pages: list[int]) -> list[Book]:
    return list(map(lambda x: get_random_book_with_author(x) if x is not None else None, pages))


def are_bookArrays_eq_by_authors(arr_0: BookArray, arr_1: BookArray) -> bool:
    return list(map(lambda x: x.author if x is not None else None, arr_0.items)) == list(map(lambda x: x.author if x is not None else None, arr_1.items))


class MergeTests(unittest.TestCase):

    def test_empty(self):
        self.assertTrue(BookArray([]) == BookArray([]).merge_authors())

    def test_matching(self):
        self.assertTrue(are_bookArrays_eq_by_authors(
            BookArray(authors_list_to_book_list([3, 2, 1])),
            BookArray(authors_list_to_book_list([2, 1, 3])).merge_authors()))
        self.assertTrue(are_bookArrays_eq_by_authors(
            BookArray(authors_list_to_book_list([1, 1, 1])),
            BookArray(authors_list_to_book_list([1, 1, 1])).merge_authors()))
        self.assertTrue(are_bookArrays_eq_by_authors(
            BookArray(authors_list_to_book_list([5, 5, 2])),
            BookArray(authors_list_to_book_list([5, 2, 5])).merge_authors()))

    def test_mismatching(self):
        self.assertFalse(are_bookArrays_eq_by_authors(
            BookArray(authors_list_to_book_list([3, 2, 1])),
            BookArray(authors_list_to_book_list([3, 1, 3])).merge_authors()))
        self.assertFalse(are_bookArrays_eq_by_authors(
            BookArray(authors_list_to_book_list([3, 2, 1])),
            BookArray(authors_list_to_book_list([3, 1, 2, 4])).merge_authors()))
        self.assertFalse(are_bookArrays_eq_by_authors(
            BookArray(authors_list_to_book_list([3, 2, 1])),
            BookArray(authors_list_to_book_list([])).merge_authors()))
        self.assertFalse(are_bookArrays_eq_by_authors(
            BookArray(authors_list_to_book_list([5, 5, 2])),
            BookArray(authors_list_to_book_list([2, 5, 2])).merge_authors()))

    def test_nones(self):
        self.assertTrue(
            BookArray(authors_list_to_book_list([5, 2, 2, None])),
            BookArray(authors_list_to_book_list([2, None, 5, 2])).merge_authors()
        )


if __name__ == '__main__':
    unittest.main()