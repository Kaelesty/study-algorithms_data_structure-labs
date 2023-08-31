"""
2.	Реализуйте структуру данных «Массив», элементами которого выступают экземпляры класса Car (минимум 10 элементов),
содержащие следующие поля (марка, VIN, объем двигателя, стоимость, средняя скорость).
Добавьте методы для сортировки вставками (по возрастанию) по полю «VIN»
и сортировка расческой (по убыванию) по полю «средняя скорость».

9.	Реализуйте структуру данных «Массив», элементами которого выступают экземпляры класса Book (минимум 10 элементов),
содержащие следующие поля (автор, издательство, кол-во страниц, стоимость, ISBN).
Добавьте методы для сортировки слиянием (по возрастанию) по полю «издательство»
и сортировки подсчетом (по убыванию) по полю «ISBN».
"""

from entities.Car import *
from entities.Book import *

from CarArray import CarArray
from BookArray import BookArray

array = BookArray(4, getRandomBook(), getRandomBook(), getRandomBook(), getRandomBook())

array.display()
array.countSort()
array.display()