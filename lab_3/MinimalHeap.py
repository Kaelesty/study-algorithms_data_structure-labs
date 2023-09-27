"""
13.	Реализуйте структуру данных «Минимальная куча» на основе динамического массива,
элементами которой выступают экземпляры класса Student (минимум 10 элементов),
содержащие следующие поля (ФИО, номер группы, курс, возраст, средняя оценка за время обучения),
где в качестве ключевого элемента при добавлении будет выступать средняя оценка.
Структура данных должна иметь возможность сохранять свое состояние в файл и загружать данные из него.
 Также реализуйте 2 варианта проверки вхождения элемента в структуру данных.
 Когда «Куча» заполнена и осуществляется добавление нового элемента, ее размер должен увеличиваться.
"""

from __future__ import  annotations
from entities.Student import *
from typing import Optional, Union
from json import loads, dumps

class MinimalHeap:
    def __init__(self, initial_items: Optional[list[Student]] = None):
        self.items = []

        if initial_items is not None:
            self.items = initial_items[:]
            self.heapify()

    def __eq__(self, other: MinimalHeap) -> bool:
        return self.items == other.items

    def to_file(self, filename: str) -> None:
        with open(filename, "w") as file:
            file.write(dumps(
                list(map(lambda x: student_to_dict(x), self.items))
            ))

    def from_file(self, filename: str) -> None:
        with open(filename, "r") as file:
            self.items = list(map(
                lambda x: student_from_dict(x), loads(file.read())
            ))

    def heapify(self) -> None:

        def heapify(i: int) -> None:
            left_index: int = 2 * i + 1
            right_index: int = 2 * i + 2
            minimal_index: int = i
            try:
                if self.items[left_index].avr_rating < self.items[minimal_index].avr_rating:
                    minimal_index = left_index
            except IndexError:
                pass
            try:
                if self.items[right_index].avr_rating < self.items[minimal_index].avr_rating:
                    minimal_index = right_index
            except IndexError:
                pass

            self.items[minimal_index], self.items[i] = self.items[i], self.items[minimal_index]

        for i in range(len(self.items) // 2 - 1, -1, -1):
            heapify(i)

    def __contains__(self, item: float) -> bool:
        for elem in self.items:
            if elem.avr_rating == item:
                return True
        return False

    def contains(self, item: Student) -> bool:
        return item in self

    def add(self, item: Student) -> None:
        for i, elem in enumerate(self.items):
            if elem.avr_rating == item.avr_rating:
                self.items[i] = item
                return
        self.items += [item]
        self.heapify()

    def __delitem__(self, key: float) -> None:
        for i, elem in enumerate(self.items):
            if elem.avr_rating == key:
                self.items[i], self.items[-1] = self.items[-1], self.items[i]
                del self.items[-1]
                self.heapify()
                return

    def __getitem__(self, item: float) -> Union[Student, None]:
        for elem in self.items:
            if elem.avr_rating == item:
                return elem
        return None

    def peek(self) -> Union[Student, None]:
        if len(self.items) == 0:
            return None
        return self.items[0]

    def pop(self) -> Union[Student, None]:
        item: Union[Student, None] = self.peek()
        if item is None:
            return None
        del self[item.avr_rating]
        return item
