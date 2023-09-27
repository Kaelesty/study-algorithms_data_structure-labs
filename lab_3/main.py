"""
4.	Реализуйте структуру данных «Двоичное дерево поиска»,
элементами которой выступают экземпляры класса Car (минимум 10 элементов),
содержащие следующие поля (марка, VIN, объем двигателя, стоимость, средняя скорость),
где в качестве ключевого элемента при добавлении будет выступать стоимость.
Структура данных должна иметь возможность сохранять свое состояние в файл и загружать данные из него.
Также реализуйте 2 варианта проверки вхождения элемента в структуру данных.

13.	Реализуйте структуру данных «Минимальная куча» на основе динамического массива,
элементами которой выступают экземпляры класса Student (минимум 10 элементов),
содержащие следующие поля (ФИО, номер группы, курс, возраст, средняя оценка за время обучения),
где в качестве ключевого элемента при добавлении будет выступать средняя оценка.
Структура данных должна иметь возможность сохранять свое состояние в файл и загружать данные из него.
 Также реализуйте 2 варианта проверки вхождения элемента в структуру данных.
 Когда «Куча» заполнена и осуществляется добавление нового элемента, ее размер должен увеличиваться.
"""
import cProfile

from MinimalHeap import *
from BinarySearchTree import *

from entities.Student import *
from entities.Car import *


def BinarySearchTree_Benchmark():
    N: int = 50000
    cars: list[Car] = [get_random_car() for _ in range(N)]
    tree: BinarySearchTree = BinarySearchTree()
    for car in cars:
        tree.insert(car)
    for car in cars:
        car.cost in tree
        tree[car.cost]
    for car in cars:
        del tree[car.cost]


def MinimalHeap_Benchmark():
    N: int = 50000
    students: list[Student] = [get_random_student() for _ in range(N)]
    heap: MinimalHeap = MinimalHeap()
    for student in students:
        heap.add(student)
    for student in students:
        student.avr_rating in heap
        heap[student.avr_rating]
    for student in students:
        heap.peek()
        del heap[student.avr_rating]


if __name__ == "__main__":
    #cProfile.run("BinarySearchTree_Benchmark()")
    cProfile.run("MinimalHeap_Benchmark()")
