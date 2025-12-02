import random
import heapq
import itertools

class Graph:
    def __init__(self, directed=False):
        self.graph = {}
        self.directed = directed

    def add_vertex(self, vertex):
        if not isinstance(vertex, (int, str, tuple)):
            raise ValueError("Vertex must be a hashable type.")
        if vertex not in self.graph:
            self.graph[vertex] = {}

    def add_edge(self, src, dest, weight):
        if src not in self.graph or dest not in self.graph:
            raise KeyError("Both vertices must exist in the graph.")
        if dest not in self.graph[src]:  # Check to prevent duplicate edges
            self.graph[src][dest] = weight
        if not self.directed and src not in self.graph[dest]:
            self.graph[dest][src] = weight

    def remove_edge(self, src, dest):
        if src in self.graph and dest in self.graph[src]:
            del self.graph[src][dest]
        if not self.directed:
            if dest in self.graph and src in self.graph[dest]:
                del self.graph[dest][src]

    def remove_vertex(self, vertex):
        if vertex in self.graph:
            # Remove any edges from other vertices to this one
            for adj in list(self.graph):
                if vertex in self.graph[adj]:
                    del self.graph[adj][vertex]
            # Remove the vertex entry itself
            del self.graph[vertex]

    def get_adjacent_vertices(self, vertex):
        return list(self.graph.get(vertex, {}).keys())

    def tour_length(self, tour):
        if tour and tour[0] == tour[-1] and len(tour) > 1:
            raise ValueError("Tour should not include the return to the starting vertex.")
        total_length = 0
        for i in range(len(tour)):
            weight = self._get_edge_weight(tour[i], tour[(i + 1) % len(tour)])
            if weight == float('inf'):  # Check for missing edge
                return float('inf')  # Tour is invalid if any edge is missing
            total_length += weight
        return total_length

    def _get_edge_weight(self, src, dest):
        return self.graph[src].get(dest, float('inf'))

    def __str__(self):
        return str(self.graph)