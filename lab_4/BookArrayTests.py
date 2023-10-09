import unittest
from BookArray import *
from entities.Book import *

class BookArrayTests(unittest.TestCase):
    def test_eq(self):
        books: list[Book] = [get_random_book() for _ in range(16)]
        self.assertEqual(BookArray(), BookArray())
        self.assertEqual(BookArray(books), BookArray(books))
        self.assertNotEqual(BookArray(books), BookArray())

    def test_contains(self):
        books: list[Book] = [get_random_book() for _ in range(16)]
        arr: BookArray = BookArray(books)
        for book in books:
            self.assertTrue(book in arr)

    def test_getitem(self):
        books: list[Book] = [get_random_book() for _ in range(16)]
        arr: BookArray = BookArray(books)
        for i in range(len(books)):
            self.assertEqual(arr[i], books[i])

    def test_delitem(self):
        books: list[Book] = [get_random_book() for _ in range(16)]
        arr: BookArray = BookArray(books)
        for i in range(len(arr)):
            del arr[i]
        self.assertTrue(arr == BookArray(len_=16))

    def test_len(self):
        books: list[Book] = [get_random_book() for _ in range(16)]
        arr: BookArray = BookArray(books)
        self.assertEqual(len(arr), 16)

    def test_qsort(self):
        books: list[Book] = [get_random_book_with_pages(i) for i in range(9, -1, -1)]
        arr_sorted: BookArray = BookArray(sorted(books, key=lambda x: x.pages))
        arr_to_sort: BookArray = BookArray(books)
        self.assertNotEqual(arr_sorted, arr_to_sort)
        self.assertEqual(arr_sorted, arr_to_sort.qsort_pages())

    def test_radix(self):
        books: list[Book] = [get_random_book_with_cost(i) for i in range(10)]
        arr_sorted: BookArray = BookArray(sorted(books, key=lambda x: -x.cost))
        arr_to_sort: BookArray = BookArray(books)
        self.assertNotEqual(arr_sorted, arr_to_sort)
        self.assertEqual(arr_sorted, arr_to_sort.radix_cost())

    def test_insertion(self):
        books: list[Book] = [get_random_book_with_pages(i) for i in range(9, -1, -1)]
        arr_sorted: BookArray = BookArray(sorted(books, key=lambda x: x.pages))
        arr_to_sort: BookArray = BookArray(books)
        self.assertNotEqual(arr_sorted, arr_to_sort)
        self.assertEqual(arr_sorted, arr_to_sort.insertion_pages())

    def test_merge(self):
        books: list[Book] = [get_random_book_with_author(i) for i in range(10)]
        arr_sorted: BookArray = BookArray(sorted(books, key=lambda x: x.author)[::-1])
        arr_to_sort: BookArray = BookArray(books)
        self.assertNotEqual(arr_sorted, arr_to_sort)
        self.assertEqual(arr_sorted, arr_to_sort.merge_authors())


if __name__ == '__main__':
    unittest.main()
