import unittest
from MinimalHeap import *
from entities.Student import *


def avr_rating_list_to_student_list(rating_list: list[float]) -> list[Student]:
    return list(map(
        lambda x: get_random_student_with_avr_rating(x), rating_list
    ))


class MinimalHeapTests(unittest.TestCase):

    def test_equals(self):
        self.assertTrue(MinimalHeap() == MinimalHeap())
        self.assertTrue(MinimalHeap([]) == MinimalHeap([]))
        student_list: list[Student] = avr_rating_list_to_student_list([5])
        self.assertTrue(
            MinimalHeap(student_list)
            ==
            MinimalHeap(student_list)
        )
        student_list = avr_rating_list_to_student_list([1, 5])
        self.assertTrue(
            MinimalHeap(student_list)
            ==
            MinimalHeap(student_list)
        )
        self.assertFalse(
            MinimalHeap(avr_rating_list_to_student_list([1])) == MinimalHeap(avr_rating_list_to_student_list([5]))
        )
        
    def test_filing(self):
        # to_file, from_file
        student_list: list[Student] = avr_rating_list_to_student_list([5])
        heap_0: MinimalHeap = MinimalHeap(student_list)
        heap_1: MinimalHeap = MinimalHeap()
        heap_0.to_file("test.json()")
        heap_1.from_file("test.json()")
        self.assertTrue(heap_0 == heap_1)

    def test_heapify(self):
        student_list: list[Student] = avr_rating_list_to_student_list([9, 8, 7, 6, 5, 4, 3, 2])
        heap_0: MinimalHeap = MinimalHeap(student_list)
        heap_1: MinimalHeap = MinimalHeap()
        heap_1.items = student_list
        self.assertFalse(heap_0 == heap_1)
        heap_1.heapify()
        self.assertTrue(heap_0 == heap_1)

    def test_contains(self):
        student_list_0: list[Student] = avr_rating_list_to_student_list([9, 8, 7])
        student_list_1: list[Student] = avr_rating_list_to_student_list([6, 5, 4])
        heap_0: MinimalHeap = MinimalHeap(student_list_0)
        for elem in student_list_0:
            self.assertTrue(elem in heap_0)
        for elem in student_list_1:
            self.assertFalse(elem in heap_0)

    def test_add(self):
        student_list: list[Student] = avr_rating_list_to_student_list([9, 8, 7, 6, 5, 4, 3, 2])
        heap_0: MinimalHeap = MinimalHeap(student_list)
        heap_1: MinimalHeap = MinimalHeap()
        for elem in student_list:
            heap_1.add(elem)
            self.assertTrue(elem in heap_1)

    def test_delitem(self):
        student_list: list[Student] = avr_rating_list_to_student_list([9, 8, 7, 6, 5, 4, 3, 2])
        heap_0: MinimalHeap = MinimalHeap(student_list)
        heap_1: MinimalHeap = MinimalHeap()
        for elem in student_list:
            del heap_0[elem.avr_rating]
            self.assertFalse(elem in heap_0)
        self.assertTrue(heap_0 == heap_1)

    def test_peek(self):
        student_list: list[Student] = avr_rating_list_to_student_list([9, 8, 7, 6, 5, 4, 3, 2])
        heap_0: MinimalHeap = MinimalHeap(student_list)
        heap_1: MinimalHeap = MinimalHeap()
        self.assertTrue(heap_0.peek().avr_rating == 2)
        self.assertTrue(heap_1.peek() is None)

    def test_pop(self):
        student_list: list[Student] = avr_rating_list_to_student_list([9, 8, 7, 6, 5, 4, 3, 2])
        heap_0: MinimalHeap = MinimalHeap(student_list)
        heap_1: MinimalHeap = MinimalHeap()
        self.assertTrue(heap_0.pop().avr_rating == 2)
        self.assertTrue(heap_1.pop() is None)

    def test_getitem(self):
        student_list_0: list[Student] = avr_rating_list_to_student_list([9, 8, 7])
        student_list_1: list[Student] = avr_rating_list_to_student_list([6, 5, 4])
        heap_0: MinimalHeap = MinimalHeap(student_list_0)
        for elem in student_list_0:
            self.assertTrue(heap_0[elem.avr_rating] == elem)
        for elem in student_list_1:
            self.assertTrue(heap_0[elem.avr_rating] is None)



if __name__ == '__main__':
    unittest.main()