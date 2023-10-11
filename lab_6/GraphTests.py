import unittest
from Graph import *
from entities.Book import *

class BookArrayTests(unittest.TestCase):
    def test_eq(self):
        matrix: list[list[int]] = [
            [0, 1, 3],
            [1, 0, 5],
            [3, 5, 0]
        ]
        self.assertTrue(Graph(matrix) == Graph(matrix))
        self.assertFalse(Graph(matrix) == Graph(matrix, is_oriented=False))
        self.assertFalse(Graph(matrix) == Graph([[0]]))

    def test_Prima(self):
        graph_0: Graph = Graph([  # For Prima example
            #     A   B   C   D   E   F   G
            [0, 7, 0, 5, 0, 0, 0],  # A
            [7, 0, 8, 9, 5, 0, 0],  # B
            [0, 8, 0, 0, 5, 0, 0],  # C
            [5, 9, 0, 0, 15, 6, 0],  # D
            [0, 5, 5, 15, 0, 8, 10],  # E
            [0, 0, 0, 6, 8, 0, 11],  # F
            [0, 0, 0, 0, 10, 11, 0],  # G
        ], is_oriented=False).prima()

        graph_1: Graph = Graph([
            [0,    7,    0,    5,    0,    0,    0],
            [7,    0,    8,    0,    5,    0,    0],
            [0,    8,    0,    0,    0,    0,    0],
            [5,    0,    0,    0,    0,    6,    0],
            [0,    5,    0,    0,    0,    0,    10],
            [0,    0,    0,    6,    0,    0,    0],
            [0,    0,    0,    0,    10,   0,    0],
        ], is_oriented=False)
        self.assertTrue(graph_0 == graph_1)

    def test_tarian(self):
        graph_0: Graph = Graph([  # For Tarian example
            #     A   B   C   D   E
            [0, 1, 1, 0, 1],  # A
            [0, 0, 0, 0, 0],  # B
            [0, 0, 0, 1, 1],  # C
            [0, 1, 0, 0, 0],  # D
            [0, 1, 0, 0, 0],  # E
        ], is_oriented=True)
        graph_0.tarian()
        for i in range(len(graph_0.vertexes)):
            self.assertTrue(graph_0.vertexes[i].literal == "BDECA"[i])

    def test_exceptions(self):
        with self.assertRaises(RuntimeError):
            Graph([[0]], is_oriented=False).tarian()
            Graph([[0]], is_oriented=True).prima()

    def test_filing(self):
        graph_0: Graph = Graph([
            #     A   B   C   D   E   F   G
            [0, 7, 0, 5, 0, 0, 0],  # A
            [7, 0, 8, 9, 5, 0, 0],  # B
            [0, 8, 0, 0, 5, 0, 0],  # C
            [5, 9, 0, 0, 15, 6, 0],  # D
            [0, 5, 5, 15, 0, 8, 10],  # E
            [0, 0, 0, 6, 8, 0, 11],  # F
            [0, 0, 0, 0, 10, 11, 0],  # G
        ], is_oriented=False)

        graph_0.to_file()
        graph_1: Graph = Graph([[]])
        graph_1.from_file()
        self.assertTrue(graph_0 == graph_1)


if __name__ == '__main__':
    unittest.main()
