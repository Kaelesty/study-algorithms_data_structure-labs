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
from typing import Optional, Union, Callable
from math import sqrt


class BookArray:

    def __init__(self, initial_items: Optional[list[Book]] = None, len_: Optional[int] = None, ) -> None:
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

    def qsort(self, by: Callable) -> BookArray:
        none_counter: int = self.items.count(None)
        self.items = list(filter(lambda x: x is not None, self.items))

        def qsort(items: list[Book]):
            if len(items) in (1, 0):
                return items
            return (qsort(list(
                filter(lambda x: by(x) <= by(items[0]), items[1:])))
                    + [items[0]]
                    + qsort(list(filter(lambda x: by(x) > by(items[0]), items[1:]))))

        self.items = qsort(self.items) + [None for _ in range(none_counter)]
        return self

    def are_sorted_by(self, by: Callable) -> bool:
        for i, book in enumerate(self.items):
            if i == len(self.items) - 1:
                break
            if by(book) > by(self.items[i + 1]):
                return False
        return True

    def jump_search(self, author: str) -> Union[Book, None]:
        if not self.are_sorted_by(lambda x: x.author):
            raise RuntimeError("BookArray is not sorted by authors")

        jump = int(sqrt(len(self.items)))
        left: int = 0
        right: int = 0
        while left < len(self.items) and self.items[left].author <= author:
            right = min(len(self.items) - 1, left + jump)
            if self.items[left].author <= author <= self.items[right].author:
                break
            left += jump
        if left >= len(self.items) or self.items[left].author > author:
            return None
        right = min(len(self.items), right + 1)
        for book in self.items[left:right + 1]:
            if book.author == author:
                return book
        return None

    def interpolation_search(self, pages: int) -> Union[Book, None]:
        if not self.are_sorted_by(lambda x: x.pages):
            raise RuntimeError("BookArray is not sorted by pages")

        low: int = 0
        high: int = len(self.items) - 1

        while self.items[low].pages < pages < self.items[high].pages:
            if self.items[high] == self.items[low]:
                break
            mid: int = low + ((pages - self.items[low].pages) * (high - low)) // (self.items[high].pages - self.items[low].pages)
            if self.items[mid].pages < pages:
                low = mid + 1
            elif self.items[mid].pages > pages:
                high = mid - 1
            else:
                return self.items[mid]
        if self.items[low].pages == pages:
            return self.items[low]
        elif self.items[high].pages == pages:
            return self.items[high]
        else:
            return None

