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

from BookArray import *
import cProfile


def benchmark():
    global arr
    arr.insertion_pages()


if __name__ == "__main__":
    N: int = 100000
    arr: BookArray = BookArray([get_random_book() for _ in range(N)])
    cProfile.run("benchmark()")
