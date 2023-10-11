from __future__ import annotations

import json
from typing import Optional, Union
from copy import deepcopy


class Graph:
    def __init__(self, matrix: list[list[int]], is_oriented: Optional[bool] = True) -> None:
        self.is_oriented = is_oriented
        self.matrix: list[list[int]] = matrix
        self.vertexes: list[Vertex] = [Vertex(self, i) for i in range(len(self.matrix))]
        self.edges: list[Edge] = []
        for i in range(len(self.matrix)):
            for j in range(len(self.matrix[i])):
                if j <= i: continue
                if self.matrix[i][j] != 0:
                    edge: Edge = Edge(self, self.matrix[i][j], self.vertexes[i], self.vertexes[j])
                    self.edges += [edge]
                    self.vertexes[i].edges += [edge]

    def __str__(self) -> str:
        return "\n".join(["\t".join(map(str, row)) for row in self.matrix])

    def print_vertexes(self) -> None:
        for vertex in self.vertexes:
            print(vertex, end="\t")
        print()

    def prima(self) -> Graph:
        if self.is_oriented:
            raise RuntimeError("Cant apply Prima algorithm to oriented graph")
        picked_vertexes: list[Vertex] = [self.vertexes[0]]
        picked_edges: list[Edge] = []
        while len(picked_vertexes) < len(self.vertexes):
            nearests: list[Edge] = []
            for vertex in picked_vertexes:
                edges: list[edges] = sorted(
                    filter(lambda x: x not in picked_edges and not (
                                x.vertex_0 in picked_vertexes and x.vertex_1 in picked_vertexes),
                           vertex.edges),
                    key=lambda x: x.weight
                )
                if len(edges) != 0:
                    if not edges[0] in nearests:
                        nearests += [edges[0]]

            nearest: Edge = sorted(nearests, key=lambda x: x.weight)[0]
            picked_edges += [nearest]
            picked_vertexes += [nearest.vertex_1 if nearest.vertex_0 in picked_vertexes else nearest.vertex_0]

        for vertex in picked_vertexes:
            vertex.edges = []

        for edge in picked_edges:
            if edge not in edge.vertex_0.edges:
                edge.vertex_0.edges += [edge]
            if edge not in edge.vertex_1.edges:
                edge.vertex_1.edges += [edge]

        matrix: list[list[int]] = [[0] * len(picked_vertexes) for _ in range(len(picked_vertexes))]
        for edge in picked_edges:
            matrix[edge.vertex_0.index][edge.vertex_1.index] = edge.weight
            matrix[edge.vertex_1.index][edge.vertex_0.index] = edge.weight
        return Graph(matrix, is_oriented=self.is_oriented)

    def tarian(self) -> None:
        if not self.is_oriented:
            raise RuntimeError("Cant apply Tarian algorithm to non-oriented graph")

        class Tarian:
            def __init__(self, vertexes: list[Vertex]):
                self.vertexes: list[Vertex] = vertexes
                self.white_vertexes: list[Vertex] = vertexes[:]
                self.grey_vertexes: list[Vertex] = []
                self.black_vertexes: list[Vertex] = []
                self.loop_flag: bool = False

            def __step(self, vertex: Vertex) -> None:
                if vertex in self.black_vertexes:
                    return
                if vertex in self.grey_vertexes:
                    loop_flag = True
                    return
                if vertex in self.white_vertexes:
                    self.white_vertexes.remove(vertex)
                    self.grey_vertexes += [vertex]
                    connected_vertexes: list[Vertex] = [
                        edge.vertex_0 if edge.vertex_0 != vertex else edge.vertex_1 for edge in vertex.edges
                    ]
                    for connected_vertex in connected_vertexes:
                        if self.loop_flag:
                            break
                        self.__step(connected_vertex)
                    if self.loop_flag:
                        return
                    self.grey_vertexes.remove(vertex)
                    self.black_vertexes += [vertex]

            def run(self) -> None:
                for vertex in self.vertexes:
                    if self.loop_flag:
                        break
                    self.__step(vertex)

        tarian: Tarian = Tarian(self.vertexes)
        tarian.run()

        if tarian.loop_flag:
            return
        self.vertexes = tarian.black_vertexes

    def __eq__(self, other: Graph) -> bool:
        return self.__str__() == other.__str__() and self.is_oriented == other.is_oriented

    def to_file(self, filename: Optional[str] = "graph.json") -> None:
        with open(filename, "w") as file:
            file.write(json.dumps([self.is_oriented, self.matrix]))

    def from_file(self, filename: Optional[str] = "graph.json") -> None:
        with open(filename, "r") as file:
            data: list = json.loads(file.read())
            matrix: list[list[int]] = data[1]
            self.__init__(matrix, data[0])


class Vertex:
    def __init__(self, graph: Graph, index: int) -> None:
        self.graph: Graph = graph
        self.edges: list[Edge] = []
        self.index = index
        self.literal: str = str(index)
            #"ABCDEFGHIJKLMNOPQISTUVWXYZ"[index]

    def __str__(self) -> str:
        return self.literal


class Edge:
    def __init__(self, graph: Graph, weight: int, vertex_0: Vertex, vertex_1: Vertex) -> None:
        self.graph: Graph = graph
        self.vertex_0: Vertex = vertex_0
        self.vertex_1: Vertex = vertex_1
        self.weight: int = weight

    def __str__(self) -> str:
        return f"{self.vertex_0.literal}-{self.vertex_1.literal}"
