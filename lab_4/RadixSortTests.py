import unittest
from BookArray import *
from entities.Book import *


def costs_list_to_book_list(pages: list[int]) -> list[Book]:
    return list(map(lambda x: get_random_book_with_cost(x) if x is not None else None, pages))


def are_bookArrays_eq_by_costs(arr_0: BookArray, arr_1: BookArray) -> bool:
    return list(map(lambda x: x.cost if x is not None else None, arr_0.items)) == list(map(lambda x: x.cost if x is not None else None, arr_1.items))


class RadixTests(unittest.TestCase):

    def test_empty(self):
        self.assertTrue(BookArray([]) == BookArray([]).radix_cost())

    def test_matching(self):
        self.assertTrue(are_bookArrays_eq_by_costs(
            BookArray(costs_list_to_book_list([3, 2, 1])),
            BookArray(costs_list_to_book_list([2, 1, 3])).radix_cost()))
        self.assertTrue(are_bookArrays_eq_by_costs(
            BookArray(costs_list_to_book_list([1, 1, 1])),
            BookArray(costs_list_to_book_list([1, 1, 1])).radix_cost()))
        self.assertTrue(are_bookArrays_eq_by_costs(
            BookArray(costs_list_to_book_list([5, 5, 2])),
            BookArray(costs_list_to_book_list([5, 2, 5])).radix_cost()))

    def test_mismatching(self):
        self.assertFalse(are_bookArrays_eq_by_costs(
            BookArray(costs_list_to_book_list([3, 2, 1])),
            BookArray(costs_list_to_book_list([3, 1, 3])).radix_cost()))
        self.assertFalse(are_bookArrays_eq_by_costs(
            BookArray(costs_list_to_book_list([3, 2, 1])),
            BookArray(costs_list_to_book_list([3, 1, 2, 4])).radix_cost()))
        self.assertFalse(are_bookArrays_eq_by_costs(
            BookArray(costs_list_to_book_list([3, 2, 1])),
            BookArray(costs_list_to_book_list([])).radix_cost()))
        self.assertFalse(are_bookArrays_eq_by_costs(
            BookArray(costs_list_to_book_list([5, 5, 2])),
            BookArray(costs_list_to_book_list([2, 5, 2])).radix_cost()))

    def test_nones(self):
        self.assertTrue(
            BookArray(costs_list_to_book_list([5, 2, 2, None])),
            BookArray(costs_list_to_book_list([2, None, 5, 2])).radix_cost()
        )


if __name__ == '__main__':
    unittest.main()