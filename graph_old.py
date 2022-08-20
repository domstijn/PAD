"""

let's build a "perfect" graph

"""
from typing import Any

# todo build a basic graph datastructure and add all the necessary extra's like certain types of searches


class Vertex:
    def __init__(self, data: Any, identifier: str | int = None):
        self.id_ = identifier
        self.data = data
        self.edges = set()

    def __repr__(self):
        return f"Node({self.id_})"


class Graph:
    def __init__(self, name: str, directed: bool = False):
        self.name = name
        self.directed = directed
        self.vertices = dict()

    def add_vertex(self, vertex: Vertex):
        self.vertices[vertex.data] = vertex

    def add_edge(self, from_vertex: Vertex, to_vertex: Vertex, weight=0):
        self.vertices[from_vertex.data].add_edge(to_vertex, weight)

        if not self.directed:
            self.vertices[to_vertex.data].add_edge(from_vertex, weight)

    def find_path(self, start_vertex, end_vertex):
        start = [start_vertex]
        seen = {}

        while len(start) > 0:
            current_vertex = start.pop()
            seen[current_vertex] = True

            if current_vertex == end_vertex:
                return True

            else:
                vertices_to_visit = set(self.vertices[current_vertex].edges.keys())
                start += [vertex for vertex in vertices_to_visit if vertex not in seen]

        return False

    # todo implement a depth first search

    # todo implement a breadth first search
    # def bfs(graph, start_vertex, target_value):
    #
    #     path = [start_vertex]
    #
    #     vertex_and_path = [start_vertex, path]
    #
    #     bfs_queue = [vertex_and_path]
    #
    #     visited = set()
    #
    #     while bfs_queue:
    #         current_vertex, path = bfs_queue.pop(0)
    #         visited.add(current_vertex)
    #         for neighbor in graph[current_vertex]:
    #             if neighbor not in visited:
    #                 if neighbor is target_value:
    #                     return path + [neighbor]
    #                 else:
    #                     bfs_queue.append([neighbor, path + [neighbor]])

    # some_hazardous_graph = {
    #     'lava': set(['sharks', 'piranhas']),
    #     'sharks': set(['piranhas', 'bees']),
    #     'piranhas': set(['bees']),
    #     'bees': set(['lasers']),
    #     'lasers': set([])
    # }
    #
    # print(bfs(some_hazardous_graph, 'sharks', 'bees'))


    # use a queue to add all the neighbours of the node you are visiting, as it is
    # NOTE implementation
    def breadth_first_search(self, data):


    # todo implement a A* search
