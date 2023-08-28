class Array:
    def __init__(self, size, *args):
        self.elems = []
        self.__size = size

        for elem in args:
            self.elems += [elem]

    def get(self, index):
        try:
            return self.elems[index]
        except IndexError:
            return None

    def display(self, separator=" "):
        for elem in self.elems:
            print(elem, end=separator)
        print()
