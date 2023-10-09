"""
15		5, 11

5.	Реализуйте структуру данных «Массив», элементами которого выступают экземпляры класса Book (минимум 10 элементов),
содержащие следующие поля (автор, издательство, кол-во страниц, стоимость, ISBN).
Добавьте методы для быстрой сортировки (по возрастанию) по полю «кол-во страниц» и
сортировки по основанию (по убыванию) по полю «стоимость».

11.	Реализуйте структуру данных «Массив», элементами которого выступают экземпляры класса Book (минимум 10 элементов),
содержащие следующие поля (автор, издательство, кол-во страниц, стоимость, ISBN).
Добавьте методы для сортировки вставками (по возрастанию) по полю «стоимость» и
сортировки слиянием (по убыванию) по полю «автор».
"""
from __future__ import annotations

from entities.Book import *
from typing import Optional, Union


class BookArray:

    def __init__(self, initial_items: Optional[list[Book]] = None,len_: Optional[int] = None,) -> None:
        if len_ is not None and initial_items is not None:
            raise RuntimeError("BookArray constructor must get the length OR initial elements")
        if len_ is not None:
            self.items: list[Union[Book, None]] = [None for _ in range(len_)]
        else:
            self.items: list[Union[Book, None]] = initial_items

    def __getitem__(self, index: int) -> Union[Book, None]:
        return self.items[index]

    def __delitem__(self, index: int) -> None:
        self.items[index] = None

    def __contains__(self, item: Book) -> bool:
        return item in self.items

    def __eq__(self, other: BookArray) -> bool:
        return self.items == other.items

    def __len__(self) -> int:
        return len(self.items)

    def qsort_pages(self) -> BookArray:
        none_counter: int = self.items.count(None)
        self.items = list(filter(lambda x: x is not None, self.items))

        def qsort(items: list[Book]):
            if len(items) in (1, 0):
                return items
            return (qsort(list(
                filter(lambda x: x.pages <= items[0].pages, items[1:])))
                    + [items[0]]
                    + qsort(list(
                filter(lambda x: x.pages > items[0].pages, items[1:]))))
        self.items = qsort(self.items) + [None for _ in range(none_counter)]
        return self

    def radix_cost(self) -> BookArray:

        if len(self.items) == 0: return self

        none_counter: int = self.items.count(None)
        self.items = list(filter(lambda x: x is not None, self.items))

        def int_len(num: int) -> int:
            return len(str(num))

        def int_digit(num: int, index: int) -> int:
            try:
                return int(str(num)[index])
            except IndexError:
                return 0

        longest_num = int_len(max(list(map(lambda x: x.cost, self.items))))
        intermediate_array: list[list[int]] = [[] for _ in range(10)]
        for digit in range(-1, -longest_num - 1, -1):
            for item in self.items:
                index: int = int_digit(item.cost, digit)
                intermediate_array[index] += [item]
            self.items = sum(intermediate_array, [])
            intermediate_array = [[] for _ in range(10)]

        self.items.reverse()
        self.items += [None for _ in range(none_counter)]
        return self

    def insertion_pages(self) -> BookArray:

        none_counter: int = self.items.count(None)
        self.items = list(filter(lambda x: x is not None, self.items))
        sorted_: list[Book] = []
        while len(self.items) != 0:
            item = self.items[0]
            self.items = self.items[1:]
            if len(sorted_) == 0:
                sorted_ = [item]
                continue
            if item.pages <= sorted_[0].pages:
                sorted_ = [item] + sorted_
                continue
            if item.pages >= sorted_[-1].pages:
                sorted_ = sorted_ + [item]
                continue
            for i, elem in enumerate(sorted_):
                if elem.pages <= item.pages < sorted_[i + 1].pages:
                    sorted_.insert(i + 1, item)
                    break
        self.items = sorted_
        self.items += [None for _ in range(none_counter)]
        return self

    def merge_authors(self) -> BookArray:

        none_counter: int = self.items.count(None)
        self.items = list(filter(lambda x: x is not None, self.items))

        def merge(items: list[Book]) -> list[Book]:
            if len(items) in (1, 0):
                return items
            first_half: list[Book] = merge(items[:len(items) // 2])
            second_half: list[Book] = merge(items[len(items) // 2:])
            for i in range(len(items)):
                if len(second_half) == 0:
                    items[i] = first_half[0]
                    first_half = first_half[1:]
                elif len(first_half) == 0:
                    items[i] = second_half[0]
                    second_half = second_half[1:]
                elif first_half[0].author > second_half[0].author:
                    items[i] = first_half[0]
                    first_half = first_half[1:]
                else:
                    items[i] = second_half[0]
                    second_half = second_half[1:]
            return items

        self.items = merge(self.items)
        self.items += [None for _ in range(none_counter)]
        return self