"""
11.	Реализуйте структуру данных «Стек» и напишите функцию проверяющую корректность скобочной последовательности в строке,
состоящей из скобок следующего типа - (, {, [, ], }, ).
Необходимо проверить, является ли скобочная последовательность корректной,
то есть количество открывающих скобок равно количеству закрывающих,
и при этом на каждой позиции закрывающая скобка имеет соответствующую открывающую скобку.
"""

from __future__ import annotations

from typing import Generic, TypeVar, Optional

T = TypeVar('T')


class MyStack(Generic[T]):
    def __init__(self, initial_items: Optional[list[T]] = None) -> None:
        self.__len = 0
        self.__items: list[T] = []
        if initial_items is not None:
            self.__len = len(initial_items)
            self.__items = initial_items

    def empty(self) -> bool:
        return self.__len == 0

    def push(self, item: T) -> MyStack:
        self.__len += 1
        self.__items += [item]
        return self

    def pop(self) -> T:
        if self.empty():
            raise RuntimeError("Can't pop empty stack")
        self.__len -= 1
        return self.__items.pop()
    
    def __eq__(self, other: MyStack[T]):
        return self.__items == other.__items