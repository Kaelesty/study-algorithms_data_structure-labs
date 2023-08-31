"""
1. Каждый узел является красным или черным.
2. Корень дерева является черным.
3. Каждый лист дерева ( NIL) является черным.
4. Если узел — красный, то оба его дочерних узла — черные.
5. Для каждого узла все пути от него до листьев, являющихся потомками
данного узла, содержат одно и то же количество черных узлов.

"""

import json

BLACK = 0
RED = 1

from entities.Car import carFromDict


def leftRotate(node, repaint=False):
    y = node.right
    node.right = y.left

    if y.left.isLeaf():
        y.left.parent = node

    y.parent = node.parent

    if node.isRoot:
        node.container.root = y
        y.isRoot = True
        node.isRoot = False
    else:
        if node == node.parent.left:
            node.parent.left = y
        else:
            node.parent.right = y
    y.left = node
    node.parent = y
    if repaint:
        node.switchColour()


def rightRotate(node, repaint=False):
    y = node.left
    node.left = y.right

    if not y.right.isLeaf():
        y.right.parent = node

    y.parent = node.parent

    if node.isRoot:
        node.container.root = y
        y.isRoot = True
        node.isRoot = False

    else:
        if node == node.parent.left:
            node.parent.left = y
        else:
            node.parent.right = y
    y.right = node
    node.parent = y
    if repaint:
        node.switchColour()


def rbInsertFixup(node):
    while True:
        if node.parent.isContainer:
            break
        if node.parent.parent.isContainer:
            if node.color == RED and node.parent.color == RED:
                if node.parent.right == node:
                    leftRotate(node.parent, True)
                else:
                    if node.parent.right.color == BLACK:
                        rightRotate(node.parent, True)
            break
        if node.parent.color != RED:
            break

        if node.parent == node.parent.parent.left:
            y = node.parent.parent.right
            if y.color == RED:
                node.parent.color = BLACK
                y.color = BLACK
                node.parent.parent.color = RED
                node = node.parent.parent
            elif node == node.parent.right:
                node = node.parent
                leftRotate(node)
                break
            else:
                node.parent.color = BLACK
                node.parent.parent.color = RED
                rightRotate(node.parent.parent)
                break
        else:
            y = node.parent.parent.left
            if y.color == RED:
                node.parent.color = BLACK
                y.color = BLACK
                node.parent.parent.color = RED
                node = node.parent.parent
            elif node == node.parent.left:
                node = node.parent
                rightRotate(node)
                break
            else:
                node.parent.color = BLACK
                node.parent.parent.color = RED
                leftRotate(node.parent.parent)
                break


def rbDeleteFixup(node):
    pass


class rbtContainer:

    def __init__(self):
        self.leaf = rbtLeaf()
        self.root = self.leaf
        self.isContainer = True

    def insert(self, value):
        if self.root.isLeaf():
            self.root = rbtNode(
                value, self, self, self.leaf, True
            )
        else:
            self.root.insert(value)
        self.root.color = BLACK

    def find(self, key):
        pass

    def delete(self, key):
        self.root.delete(key)

    def toJson(self):
        return json.dumps(self.toDict())

    def toDict(self):
        return {
            "root": self.root.toDict()
        }

    def fromJson(self, jsonString):
        raw = json.loads(jsonString)
        self.root = self.nodeFromDict(raw["root"], self, True)

    def nodeFromDict(self, raw, parent, rootNode=False):
        if raw["value"] == "LEAF":
            return self.leaf

        node = rbtNode(
            carFromDict(raw["value"]),
            parent,
            self,
            self.leaf,
            rootNode,
            True
        )

        node.color = BLACK if raw["color"] == "BLACK" else RED

        node.right = self.nodeFromDict(raw["right"], node)
        node.left = self.nodeFromDict(raw["left"], node)
        return node




class rbtLeaf:
    def __init__(self):
        self.color = BLACK
        self.isContainer = False

    def isLeaf(self):
        return True

    def delete(self, key):
        pass

    def toDict(self):
        return {
            "value": "LEAF"
        }

    def switchColour(self):
        pass


class rbtNode:
    def __init__(self, value, parent, container, leaf, isRoot=False, balanceChecked=False):
        self.value = value
        self.right = leaf
        self.left = leaf
        self.parent = parent
        self.isRoot = isRoot
        self.container = container
        self.isContainer = False

        if isRoot:
            self.color = BLACK
        else:
            self.color = RED
            if not balanceChecked:
                rbInsertFixup(self)

    def toDict(self):
        return {
            "value": self.value.toDict(),
            "color": "BLACK" if self.color == BLACK else "RED",
            "isRoot": self.isRoot,
            "right": self.right.toDict(),
            "left": self.left.toDict()
        }

    def switchColour(self):
        self.color = RED if self.color == BLACK else BLACK
        self.left.switchColour()
        self.right.switchColour()

    def isLeaf(self):
        return False

    def insert(self, value):

        if self.value.price < value.price:

            # to right branch
            if self.right.isLeaf():
                self.right = rbtNode(value, self, self.container, self.right)
            else:
                self.right.insert(value)

        elif self.value.price > value.price:

            # to left branch
            if self.left.isLeaf():
                self.left = rbtNode(value, self, self.container, self.left)
            else:
                self.left.insert(value)

        else:

            self.value = value

    def delete(self, key):

        if key > self.value.price:
            self.right.delete(key)
        elif key < self.value.price:
            self.left.delete(key)
        else:
            self.annihilate()

    def annihilate(self):
        if self.left.isLeaf() and self.right.isLeaf():

            if self.parent.left == self:
                self.parent.left = self.left  # left is leaf ^^^

            else:
                self.parent.right = self.left

        elif self.left.isLeaf():

            if self.parent.left == self:
                self.parent.left = self.right
                # todo: need to fix colours

            else:
                self.parent.right = self.right
                # todo: need to fix colours

        elif self.right.isLeaf():

            if self.parent.left == self:
                self.parent.left = self.left
                # todo: need to fix colours

            else:
                self.parent.right = self.left
                # todo: need to fix colours

        else:

            value, color = self.right.takeLeftest()
            self.value = value
            self.color = color

            if color == BLACK:
                pass
                # todo: need to fix colours

    def takeLeftest(self):
        if self.left.isLeaf():
            self.annihilate()
            return self.value, self.color
        return self.left.takeLeftestValue()
