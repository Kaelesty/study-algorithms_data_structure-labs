"""
5.	Реализуйте структуру данных «Массив», элементами которого выступают экземпляры класса Book (минимум 10 элементов),
содержащие следующие поля (автор, издательство, кол-во страниц, стоимость, ISBN).
Добавьте метод для любой метод сортировки и метод скачкообразного поиска по полю «автор».
При вызове поиска убедитесь, что элементы структуры данных отсортированы, в ином случае – выбросите исключение.

11.	Реализуйте структуру данных «Массив», элементами которого выступают экземпляры класса Book (минимум 10 элементов),
содержащие следующие поля (автор, издательство, кол-во страниц, стоимость, ISBN).
Добавьте метод для любой метод сортировки и метод интерполяционного поиска по полю «кол-во страниц».
При вызове поиска убедитесь, что элементы структуры данных отсортированы, в ином случае – выбросите исключение.
"""
import cProfile
import random

from Graph import Graph


graph_0: Graph = Graph([ # For Prima example
#     A   B   C   D   E   F   G
    [ 0 , 7 , 0 , 5 , 0 , 0 , 0 ], # A
    [ 7 , 0 , 8 , 9 , 5 , 0 , 0 ], # B
    [ 0 , 8 , 0 , 0 , 5 , 0 , 0 ], # C
    [ 5 , 9 , 0 , 0 , 15, 6 , 0 ], # D
    [ 0 , 5 , 5 , 15, 0 , 8 , 10], # E
    [ 0 , 0 , 0 , 6 , 8 , 0 , 11], # F
    [ 0 , 0 , 0 , 0 , 10, 11, 0 ], # G
], is_oriented=False)

graph_1: Graph = Graph([ # For Tarian example
#     A   B   C   D   E
    [ 0 , 1 , 1 , 0 , 1 ], # A
    [ 0 , 0 , 0 , 0 , 0 ], # B
    [ 0 , 0 , 0 , 1 , 1 ], # C
    [ 0 , 1 , 0 , 0 , 0 ], # D
    [ 0 , 1 , 0 , 0 , 0 ], # E
], is_oriented=True)


def get_random_graph(N: int, is_oriented: bool) -> Graph:
    matrix: list[list[int]] = [[0] * N for _ in range(N)]
    for i in range(N):
        for j in range(N):
            if i <= j: continue
            num: int = random.randint(1, 100)
            matrix[i][j] = num
            if not is_oriented:
                matrix[j][i] = num
    return Graph(matrix, is_oriented)


def benchmark_prima(N: int) -> None:
    graph = get_random_graph(N, False)
    graph.prima()


def benchmark_tarian(N: int) -> None:
    graph = get_random_graph(N, True)
    graph.tarian()


if __name__ == "__main__":
    N: int = 500
    cProfile.run("benchmark_tarian(N)")
