BLACK = 0
RED = 1

ROOT = 4
LEFT_BRANCH = 5
RIGHT_BRANCH = 6

from Car import Car


class rbtContainer:

    def __init__(self):
        self.root = rbtLeaf()

    def insert(self, car):
        if isinstance(self.root, rbtLeaf):
            self.root = rbtNode(
                car, self, self, ROOT, True
            )
        else:
            self.root.insert(car)

    def repaint(self):
        self.root.switchColor()

    def find(self, key):
        pass

    def delete(self, key):
        pass

    def getOtherChildColor(self, key):
        return None

    def rotateChild(self, rotateType, branchToRotate):
        def rotateRight(branch):
            root = self.root
            root.isRoot = False
            newRoot = root.left
            root.left = newRoot.right
            root = newRoot
            self.root = root
            self.root.isRoot = True

        def rotateLeft(branch):
            root = self.root
            root.isRoot = False
            newRoot = root.right
            root.right = newRoot.left
            newRoot.left = root
            root = newRoot
            self.root = root
            self.root.isRoot = True

        try:
            if rotateType == LEFT_BRANCH:
                rotateRight(branchToRotate)
            else:
                rotateLeft(branchToRotate)
        except AttributeError:
            print("rotate failed")


class rbtNode:

    def __init__(self, car, container, parent, branch, isRoot=False):
        self.parent = parent
        self.car = car
        self.container = container
        self.left = rbtLeaf()
        self.right = rbtLeaf()
        self.isRoot = isRoot
        self.branch = branch

        if isRoot:
            self.color = BLACK
        else:
            self.color = RED

            # we should check tree balance
            if isRoot or self.parent.color == BLACK:
                return  # balance is fine

            uncleColor = self.getUncleColor()

            if uncleColor is None:
                print("balance is fine")
                return  # grandfather is container, don't need to rebalance

            if uncleColor == RED:  # balance is broken, but can be fixed by simple repaint
                print("balance is broken, repainting")
                #self.color = BLACK  # will be changed to RED during container.repaint()
                self.container.repaint()
            else:  # balance is broken, can be fixed by rotating
                print("balance is broken, rotating")
                self.color = BLACK  # will be changed to RED during repaint()
                self.parent.parent.rotate(branch)

    def rotate(self, branch):
        self.parent.rotateChild(branch, self.branch)
        #self.switchColor()


    def rotateChild(self, initBranch, branchToRotate):
        # todo
        pass


    def getUncleColor(self):
        return self.parent.getBrotherColor()

    def getBrotherColor(self):
        return self.parent.getOtherChildColor(self.car.price)

    def getOtherChildColor(self, key):
        if isinstance(self.right, rbtLeaf) or isinstance(self.left, rbtLeaf):
            return BLACK

        if self.right.car.price == key:
            return self.left.color
        return self.right.color

    def insert(self, car):

        if self.car.price > car.price:

            if isinstance(self.left, rbtLeaf):
                self.left = rbtNode(
                    car, self.container, self, LEFT_BRANCH
                )
            else:
                self.left.insert(car)

        elif self.car.price < car.price:

            if isinstance(self.right, rbtLeaf):
                self.right = rbtNode(
                    car, self.container, self, RIGHT_BRANCH
                )
            else:
                self.right.insert(car)

        else:  # car.price == self.car.price
            self.car = car

    def switchColor(self):
        self.color = RED if self.color == BLACK else BLACK
        self.left.switchColor()
        self.right.switchColor()


class rbtLeaf:
    def __init__(self):
        self.color = None

    def switchColor(self):
        pass
