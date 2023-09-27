import unittest
from BinarySearchTree import *
from entities.Car import *


def cost_list_to_car_list(cost_list: list[int]) -> list[Car]:
    return list(map(
        lambda x: get_random_car_with_cost(x), cost_list
    ))


class BinarySearchTreeTests(unittest.TestCase):

    def test_equals(self):
        self.assertTrue(BinarySearchTree() == BinarySearchTree())
        self.assertTrue(BinarySearchTree([]) == BinarySearchTree([]))
        car_list: list[Car] = cost_list_to_car_list([5])
        self.assertTrue(
            BinarySearchTree(car_list)
            ==
            BinarySearchTree(car_list)
        )
        car_list = cost_list_to_car_list([1, 5])
        self.assertTrue(
            BinarySearchTree(car_list)
            ==
            BinarySearchTree(car_list)
        )
        self.assertFalse(
            BinarySearchTree(cost_list_to_car_list([1])) == BinarySearchTree(cost_list_to_car_list([5]))
        )

    def test_insert(self):
        cars_list: list[Car] = cost_list_to_car_list([5, 6, 7])
        tree_0: BinarySearchTree = BinarySearchTree(cars_list)
        tree_1: BinarySearchTree = BinarySearchTree()
        for elem in cars_list:
            tree_1.insert(elem)
        self.assertTrue(tree_0 == tree_1)

    def test_contains(self):
        cars_list_0: list[Car] = cost_list_to_car_list([5, 6, 7])
        cars_list_1: list[Car] = cost_list_to_car_list([1, 2, 3])
        tree_0: BinarySearchTree = BinarySearchTree(cars_list_0)
        for elem in cars_list_0:
            self.assertTrue(elem.cost in tree_0)
        for elem in cars_list_1:
            self.assertFalse(elem.cost in tree_0)

    def test_getitem(self):
        cars_list: list[Car] = cost_list_to_car_list([5, 6, 7])
        tree_0: BinarySearchTree = BinarySearchTree(cars_list)
        for elem in cars_list:
            tree_0[elem.cost] == elem

    def test_delitem(self):
        cars_list: list[Car] = cost_list_to_car_list([5, 6, 7])
        tree_0: BinarySearchTree = BinarySearchTree(cars_list)
        tree_1: BinarySearchTree = BinarySearchTree()
        for elem in cars_list:
            del tree_0[elem.cost]
        self.assertTrue(tree_1 == tree_0)

    def test_lop(self):
        cars_list: list[Car] = cost_list_to_car_list([5, 6, 7])
        tree_0: BinarySearchTree = BinarySearchTree(cars_list)
        tree_1: BinarySearchTree = BinarySearchTree()
        tree_0.lop(0)
        self.assertTrue(tree_1 == tree_0)

    def test_filing(self):
        # to_file from_file, to_dict, node_from_dict, from_dict
        cars_list: list[Car] = cost_list_to_car_list([5, 6, 7])
        tree_0: BinarySearchTree = BinarySearchTree(cars_list)
        tree_1: BinarySearchTree = BinarySearchTree()
        tree_0.to_file("test.json()")
        tree_1.from_file("test.json()")
        self.assertTrue(tree_1 == tree_0)


if __name__ == '__main__':
    unittest.main()