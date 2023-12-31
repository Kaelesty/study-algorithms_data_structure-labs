from __future__ import annotations

from typing import Generic, TypeVar, Optional

T = TypeVar('T')


class MySet(Generic[T]):
    def __init__(self, initial_items: Optional[list[T]] = None) -> None:
        self.__items: list[T] = []

        if initial_items is not None:
            for item in initial_items:
                if item not in self.__items:
                    self.__items += [item]

    def add(self, item: T) -> MySet:
        if item in self: return self
        self.__items += [item]
        return self

    def pop(self) -> T:
        if len(self.__items) == 0:
            raise RuntimeError("Can't pop empty set")
        return self.__items.pop()

    def __delitem__(self, item: T) -> None:
        if item in self:
            self.__items.remove(item)

    def __contains__(self, item: T) -> bool:
        return item in self.__items

    def contains(self, item: T) -> bool:
        return item in self

    def intersect(self, other: MySet) -> MySet:
        intersection: list[T] = []
        for item in self.__items:
            if item in other:
                intersection += [item]
        return MySet(intersection)

    def union(self, other: MySet) -> MySet:
        return MySet(self.__items + other.__items)

    def __eq__(self, other: MySet) -> bool:
        other_items = other.__items[:]
        for item in self.__items:
            if item in other_items:
                other_items.remove(item)
            else:
                return False
        return len(other_items) == 0
