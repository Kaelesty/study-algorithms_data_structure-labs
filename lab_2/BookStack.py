from Stack import Stack


class BookStack(Stack):
    def __init__(self, startValue: [str, None]) -> None:
        super().__init__(startValue)
        self.__len = 1 if startValue is not None else 0

    def push(self, newValue: str) -> None:
        self.__len += 1
        return super().push(newValue)

    def get(self) -> [str, None]:
        return super(BookStack, self).get()

    def pop(self) -> [str, None]:
        if super().get() is not None:
            self.__len -= 1
        return super().pop()

    def doesContain(self, value: str, startFromRoot: bool = False):
        return super().doesContain(value, startFromRoot)

    def __add__(self, other):
        while other.get() is not None:
            self.push(other.pop())
        return self

    def __len__(self) -> int:
        return self.__len
