import unittest
from MySet import *


# noinspection PyStatementEffect
class MySetTests(unittest.TestCase):

    def test_add_item_to_empty(self) -> None:
        initial: MySet[int] = MySet([1])
        afterAdd: MySet[int] = MySet[int]().add(1)
        self.assertEqual(
            initial, afterAdd
        )

    def test_add_to_non_empty(self) -> None:
        initial: MySet[int] = MySet([1, 4])
        afterAdd: MySet[int] = MySet[int]([4]).add(1)
        self.assertEqual(
            initial, afterAdd
        )

    def test_add_multipe(self) -> None:
        initial: MySet[int] = MySet([1, 4, 5, 6])
        afterAdd: MySet[int] = MySet[int]([4])\
            .add(1)\
            .add(6)\
            .add(5)
        self.assertEqual(
            initial, afterAdd
        )

    def test_add_existing(self) -> None:
        initial: MySet[int] = MySet([1, 4, 5, 6])
        afterAdd: MySet[int] = initial.add(5)
        self.assertEqual(
            initial, afterAdd
        )

    def test_equals(self) -> None:
        initial_0: MySet[int] = MySet[int]()
        initial_1: MySet[int] = MySet[int]()
        self.assertTrue(initial_1 == initial_0)

        initial_1.add(5)
        self.assertFalse(initial_1 == initial_0)

        initial_0.add(4)
        self.assertFalse(initial_1 == initial_0)

        initial_1.add(4)
        initial_0.add(5)
        self.assertTrue(initial_1 == initial_0)

    def test_pop_all(self) -> None:
        initial: MySet[int] = MySet([1, 4, 5, 6])
        for i in range(4):
            self.assertEqual(initial.pop(), [1, 4, 5, 6][3 - i])
        with self.assertRaises(RuntimeError):
            initial.pop()

    def test_del(self) -> None:
        initial: MySet[int] = MySet[int]()
        del initial[4]
        self.assertEqual(initial, MySet[int]())
        initial.add(19).add(4).add(1)
        del initial[4]
        self.assertEqual(initial, MySet[int]([19, 1]))
        del initial[19]
        self.assertEqual(initial, MySet[int]([1]))
        del initial[1]
        self.assertEqual(initial, MySet[int]())

    def test_contains(self) -> None:
        initial: MySet[int] = MySet[int]()
        self.assertFalse(5 in initial)
        initial.add(19).add(1).add(4).add(5).add(6)
        for item in [1, 4, 5, 6, 19]:
            self.assertTrue(item in initial)
        del initial[4]
        self.assertFalse(4 in initial)

    def test_intersert(self) -> None:
        initial_0: MySet[int] = MySet[int]()
        initial_1: MySet[int] = MySet[int]()
        self.assertEqual(initial_1.intersect(initial_0), MySet[int]())
        initial_0.add(19).add(5)
        self.assertEqual(initial_1.intersect(initial_0), MySet[int]())
        initial_1.add(19)
        self.assertEqual(initial_1.intersect(initial_0), MySet[int]([19]))

    def test_union(self) -> None:
        initial_0: MySet[int] = MySet[int]()
        initial_1: MySet[int] = MySet[int]()
        self.assertEqual(initial_1.union(initial_0), MySet[int]())
        initial_0.add(19).add(5)
        self.assertEqual(initial_1.union(initial_0), MySet[int]([19, 5]))
        initial_1.add(4)
        self.assertEqual(initial_1.union(initial_0), MySet[int]([19, 5, 4]))






if __name__ == '__main__':
    unittest.main()