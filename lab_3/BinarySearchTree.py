"""
4.	Реализуйте структуру данных «Двоичное дерево поиска»,
элементами которой выступают экземпляры класса Car (минимум 10 элементов),
содержащие следующие поля (марка, VIN, объем двигателя, стоимость, средняя скорость),
где в качестве ключевого элемента при добавлении будет выступать стоимость.
Структура данных должна иметь возможность сохранять свое состояние в файл и загружать данные из него.
Также реализуйте 2 варианта проверки вхождения элемента в структуру данных.
"""
from __future__ import annotations

from typing import Optional, Union
from entities.Car import Car, car_to_dict, car_from_dict

from json import dumps, loads


class BinarySearchTree:
    def __init__(self, initial_items: Optional[list[Car]] = None) -> None:
        self.root: Union[bst_node, None] = None

        if initial_items is not None:
            for item in initial_items:
                self.insert(item)

    def insert(self, item: Car) -> None:
        if self.root is None:
            self.root = bst_node(item, self)
        else:
            self.root.insert(item)

    def __contains__(self, key: int) -> bool:
        if self.root is None:
            return False
        return key in self.root

    def contains(self, key: int) -> bool:
        return key in self

    def __getitem__(self, key: int) -> Union[Car, None]:
        if self.root is None:
            return None
        return self.root[key]

    def __delitem__(self, key: int) -> None:
        if self.root is None:
            return
        del self.root[key]

    def lop(self, key: int) -> None:
        self.root = None

    def to_file(self, filename: str) -> None:
        with open(filename, "w") as file:
            file.write(dumps(self.to_dict()))

    def from_file(self, filename) -> BinarySearchTree:
        with open(filename, "r") as file:
            self.from_dict(loads(file.read()))
        return self

    def from_dict(self, raw: dict) -> None:
        self.root = self.node_from_dict(raw["root"], self)

    def node_from_dict(self, raw: Union[dict, None], parent: Union[bst_node, BinarySearchTree]) -> Union[bst_node, None]:
        if raw is None:
            return None
        node: bst_node = bst_node(
            car_from_dict(raw["value"]),
            parent
        )
        node.right = self.node_from_dict(raw["right"], node)
        node.left = self.node_from_dict(raw["left"], node)
        return node

    def to_dict(self) -> dict[
        str,
        Union[
            dict[str, Union[str, int, float]],
            None,
            dict,
        ]
    ]:
        return {
            "root": None if self.root is None else self.root.to_dict()
        }

    def __eq__(self, other: BinarySearchTree) -> bool:
        return self.to_dict() == other.to_dict()


class bst_node:
    def __init__(self, value: Car, parent: Union[bst_node, BinarySearchTree]) -> None:
        self.value: Car = value
        self.left: Union[None, bst_node] = None
        self.right: Union[None, bst_node] = None
        self.parent: Union[bst_node, BinarySearchTree] = parent

    def to_dict(self) -> dict[str, Union[dict[str, Union[str, int, float]], dict, None]]:
        return {
            "value": car_to_dict(self.value),
            "left": None if self.left is None else self.left.to_dict(),
            "right": None if self.right is None else self.right.to_dict(),
        }

    def insert(self, item: Car) -> None:
        if self.value.cost > item.cost:

            if self.left is None:
                self.left = bst_node(item, self)
            else:
                self.left.insert(item)

        elif self.value.cost < item.cost:

            if self.right is None:
                self.right = bst_node(item, self)
            else:
                self.right.insert(item)

        else:
            self.value = item

    def __contains__(self, item: int) -> bool:
        if item < self.value.cost:
            return False if self.left is None else item in self.left
        if item > self.value.cost:
            return False if self.right is None else item in self.right
        return self.value.cost == item

    def __delitem__(self, key: int) -> None:
        if key < self.value.cost:
            if self.left is None:
                return
            del self.left[key]
        elif key > self.value.cost:
            if self.right is None:
                return
            del self.right[key]
        else:
            if self.right is None and self.left is None:
                self.parent.lop(key)
            elif self.right is None and self.left is not None:
                self.value = self.left.value
                self.left = None
            elif self.left is None and self.right is not None:
                self.value = self.right.value
                self.right = None
            else:
                self.value = self.right.take_leftest()

    def take_leftest(self) -> Car:
        if self.left is None:
            if self.right is None:
                self.parent.lop(self.value.cost)
                return self.value
            else:
                old_value: Car = self.value
                self.value = self.right.value
                self.left = self.right.left
                self.right = self.right.right
                return old_value
        else:
            return self.left.take_leftest()
    
    def lop(self, key: int) -> None:
        if self.left is None:
            self.right = None
        elif self.right is None:
            self.left = None
        else:
            if self.left.value.cost == key:
                self.left = None
            else:
                self.right = None

    def __getitem__(self, key: int) -> Union[Car, None]:
        if key < self.value.cost:
            return None if self.left is None else self.left[key]
        if key > self.value.cost:
            return None if self.right is None else self.right[key]

        return self.value
