"""

creating a better graph to work with

"""
from __future__ import annotations

from typing import Any

import numpy as np

from queue import Queue
from stack import Stack


class Vertex:
    def __init__(self, data: Any):
        self.data = data
        self.edges = set()

    def __repr__(self):
        return f"{self.data}"

    def add_edge(self, other, weight: int):
        self.edges.add((other, weight))


class Graph:
    def __init__(self, name: str, directed: bool):
        self.name = name
        self.directed = directed
        self.vertices = dict()

    def __repr__(self):
        # todo a visual representation of the graph
        return self.name

    def add_vertex(self, data):
        """
        a new vertex is made from the data you pass as input
        """
        if isinstance(data, list):
            for entry in data:
                self.add_vertex(entry)
            return

        new_vertex = Vertex(data)

        self.vertices[data] = new_vertex

    def add_edge(self, from_, to_, weight=0):
        """
        both from_ and to_ are vertex-data attributes,
        the corresponding vertices are searched in the dictionary
        """
        from_v: Vertex = self.vertices[from_]
        to_v: Vertex = self.vertices[to_]

        from_v.add_edge(to_v, weight)

        if not self.directed:
            to_v.add_edge(from_v, weight)

    def add_edges(self, adjacency_list):
        """
        adjacency list is a list of dictionaries,
        which have every node as the key and their edges as values
        """
        for vertex, adjacent_vertices in adjacency_list.items():
            for adjacent_vertex, weight in adjacent_vertices:
                self.add_edge(vertex, adjacent_vertex, weight)

    def find_path_breadth(self, start, goal):
        """
        BREADTH FIRST

        both start and goal are both data attributes from vertices,
        to enable searching on known info,
        breadth first searches the shortest route,
        which is efficient when the results aren't nested too deep
        """
        # start a queue with the starting node as the first entity
        bfs_queue = Queue(f"search path {self.name} for {goal} from {start}")

        start_v = self.vertices[start]
        start_v: Vertex

        vertices_seen = set()

        bfs_queue.enqueue((start_v, [start_v, ]))

        while not bfs_queue.is_empty:
            possible_match, path = bfs_queue.dequeue()

            if possible_match.data == goal:
                # todo, the path does not contain the weights, so should be implemented
                return possible_match, path

            vertices_seen.add(possible_match)

            # be careful with loops, only add the ones which haven't been seen
            bfs_queue.enqueue([(vertex, path + [vertex]) for vertex, weight in possible_match.edges if vertex not in vertices_seen])

        return False, None

    def find_path_depth(self, start, goal):
        """
        DEPTH FIRST

        both start and goal are both data instances and not vertices,
        depth first searches, are meant to find a route to the goal,
        not the fastest or shortest persé,
        """

        dfs_stack = Stack('stack for dfs', size_limit=np.inf)

        start_v = self.vertices[start]
        start_v: Vertex

        dfs_stack.push(start_v)

        vertices_seen = set()

        # the stack is the traceback for the node
        while not dfs_stack.empty:
            vertices_seen.add(dfs_stack.peek())

            if dfs_stack.peek().data == goal:
                dfs_stack.reverse()
                dfs_stack.is_reversed = False
                return dfs_stack

            # add next child vertex to the stack and check
            else:
                children = dfs_stack.peek().edges
                if children is None:
                    dfs_stack.pop()
                else:
                    pop = True
                    for vertex, weight in children:
                        if vertex not in vertices_seen:
                            dfs_stack.push(vertex)
                            pop = False
                            break
                    if pop:
                        dfs_stack.pop()

        return None


if __name__ == '__main__':
    graph = Graph('simple graph', False)

    graph.add_vertex(['a', 'b', 'c', 'd', 'e', 'f', 'x'])
    adjacent_list = {
            'a': {('e', 0), ('f', 0), ('b', 0), },
            'b': {('d', 0), ('c', 0), },
            'c': {('d', 0), ('x', 0), },
            'e': {('f', 0), },
            'f': {('d', 0), },
    }

    graph.add_edges(adjacent_list)

    match, pathway = graph.find_path_breadth('a', 'b')

    if match:
        print(pathway)
    else:
        print('no pathway found')

    path_stack = graph.find_path_depth('a', 'b')
    print(path_stack)




