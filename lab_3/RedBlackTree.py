BLACK = 0
RED = 1

from Car import Car


class rbtContainer:

    def __init__(self):
        self.root = rbtLeaf()

    def insert(self, car):
        if isinstance(self.root, rbtLeaf):
            self.root = rbtNode(
                car, self, self, True
            )
        else:
            self.root.insert(car)

    def find(self, key):
        pass

    def delete(self, key):
        pass


class rbtNode:

    def __init__(self, car, container, parent, isRoot=False):
        self.parent = parent
        self.car = car
        self.container = container
        self.left = rbtLeaf()
        self.right = rbtLeaf()

        if isRoot:
            self.color = BLACK
        else:
            self.color = RED
            # we should check tree balance

    def insert(self, car):

        if self.car.price > car.price:

            if isinstance(self.left, rbtLeaf):
                self.left = rbtNode(
                    car, self.container, self
                )
            else:
                self.left.insert(car)

        elif self.car.price < car.price:

            if isinstance(self.right, rbtLeaf):
                self.right = rbtNode(
                    car, self.container, self
                )
            else:
                self.right.insert(car)

        else:  # car.price == self.car.price
            self.car = car


class rbtLeaf:
    pass
