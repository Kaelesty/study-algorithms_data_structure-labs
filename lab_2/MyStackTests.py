import unittest
from MyStack import *

class MyStackTests(unittest.TestCase):

    def test_equals(self):
        self.assertTrue(MyStack() == MyStack())
        self.assertTrue(MyStack([5]) == MyStack([5]))
        self.assertFalse(MyStack([4]) == MyStack([5]))
        self.assertFalse(MyStack([19, 5]) == MyStack([19]))
        self.assertFalse(MyStack([1, 19]) == MyStack([19, 1]))

    def test_push(self):

        initial: MyStack[int] = MyStack([4, 5, 6])
        after_add: MyStack[int] = MyStack()

        self.assertFalse(initial == after_add)

        after_add.push(4).push(5).push(6)

        self.assertTrue(initial == after_add)

    def test_pop(self):

        initial: MyStack[int] = MyStack([4, 5, 6])

        for item in [4, 5, 6][::-1]:
            self.assertEqual(initial.pop(), item)

        with self.assertRaises(RuntimeError):
            initial.pop()

    def test_empty(self):

        self.assertTrue(MyStack().empty())
        self.assertFalse(MyStack([19]).empty())

if __name__ == '__main__':
    unittest.main()