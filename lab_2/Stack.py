from DoublyLinkedList import DoublyLinkedListNode


class Stack:
    def __init__(self, startValue):
        self.__root = DoublyLinkedListNode(
            startValue, None, None
        )
        self.__vertex = self.__root

    def push(self, newValue):
        # insert new elem
        newNode = DoublyLinkedListNode(newValue, self.__vertex, None)
        self.__vertex.next = newNode
        self.__vertex = newNode


    def get(self):
        # get new elem
        try:
            return self.__vertex.value
        except AttributeError:
            return None

    def pop(self):
        # return last elem and then delete it
        val = self.get()
        try:
            self.__vertex = self.__vertex.prev
            self.__vertex.next = None
        except AttributeError:
            pass
        return val

    def doesContain(self, value, startFromRoot=False):
        if not startFromRoot:
            return self.__checkContainFromVertex(self.__vertex, value)
        else:
            return self.__checkContainFromRoot(self.__root, value)

    def __checkContainFromVertex(self, vertex, value):
        if vertex.value == value:
            return True
        if vertex.prev is None:
            return False
        return self.__checkContainFromVertex(vertex.prev, value)

    def __checkContainFromRoot(self, root, value):
        if root.value == value:
            return True
        if root.next is None:
            return False
        return self.__checkContainFromRoot(root.next, value)



