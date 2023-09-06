"""
7.	Реализуйте структуру данных «Множество» на основе такой структуры данных, как «Динамический массив».
Обращение к элементам множества должно производиться с использованием дандерных (магических) методов Python.
Также реализуйте 2 варианта проверки вхождения элемента в структуру данных,
метод intersect для выполнения такой операции над множествами, как пересечение
и метод union для выполнения такой операции над множествами, как объединение.
"""
from __future__ import annotations

import typing
from typing import Generic, TypeVar, Optional

T = TypeVar('T')


class MySet(Generic[T]):
    def __init__(self, initial_items: Optional[list[T]] = None, are_items_comparable: Optional[bool] = False) -> None:
        self.__items: list[T] = []
        self.__comparable_flag = are_items_comparable
        self.__sorted_flag = True

        if initial_items is not None:

            for item in initial_items:
                if item not in self.__items:
                    self.__items += [item]

    def add(self, item: T) -> MySet:
        if item not in self:
            self.__items += [item]
        self.__sorted_flag = False
        return self

    def pop(self) -> T:
        if len(self.__items) == 0:
            raise RuntimeError("Can't pop empty set")
        self.__sorted_flag = False
        return self.__items.pop()

    def __delitem__(self, item: T) -> None:
        if item in self:
            self.__items.remove(item)
        self.__sorted_flag = False

    def __contains__(self, item: T) -> bool:
        if self.__comparable_flag:
            return self.__binarySearch(item)
        return self.__linear_search(item)

    def __linear_search(self, item_to_find: T) -> bool:
        for item in self.__items:
            if item == item_to_find:
                return True
        return False

    def __binarySearch(self, item: T) -> bool:
        if not self.__sorted_flag:
            self.__sort()

        def recursiveSearch(item: T, items: list[T]) -> bool:
            if len(items) == 0:
                return False
            if len(items) == 1:
                return items[0] == item

            middle_index: int = len(items) // 2
            if item == items[middle_index]:
                return True
            return recursiveSearch(
                item,
                items[:middle_index] if item < items[middle_index] else items[middle_index + 1:]
            )

        return recursiveSearch(item, self.__items)


    def __sort(self) -> None:
        self.__sorted_flag = True

        def qsort(items) -> list[T]:
            if len(items) in (0, 1):
                return items
            picked: T = items[0]
            items = items[1:]
            return qsort(list(filter(lambda x: x < picked, items))) \
                   + [picked] + qsort(list(filter(lambda x: x > picked, items)))

        self.__items = qsort(self.__items)

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




