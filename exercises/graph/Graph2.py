import heapq

class Graph:
    def __init__(self, directed=False):
        self.graph = {}
        self.directed = directed

    def add_vertex(self, vertex):
        """Add a vertex to the graph"""
        if not isinstance(vertex, (int, str, tuple)):
            raise ValueError("Vertex must be a hashable type.")
        if vertex not in self.graph:
            self.graph[vertex] = {}

    def add_edge(self, src, dest, weight):
        """Add an edge with weight between src and dest"""
        if src not in self.graph or dest not in self.graph:
            raise KeyError("Both vertices must exist in the graph.")

        # Allow weight updates for existing edges
        self.graph[src][dest] = weight
        if not self.directed:
            self.graph[dest][src] = weight

    def remove_edge(self, src, dest):
        """Remove an edge from the graph"""
        if src in self.graph and dest in self.graph[src]:
            del self.graph[src][dest]
        if not self.directed:
            if dest in self.graph and src in self.graph[dest]:
                del self.graph[dest][src]

    def remove_vertex(self, vertex):
        """Remove a vertex and all its edges from the graph"""
        if vertex in self.graph:
            # Remove any edges from other vertices to this one
            for adj in list(self.graph):
                if vertex in self.graph[adj]:
                    del self.graph[adj][vertex]
            # Remove the vertex entry itself
            del self.graph[vertex]

    def get_adjacent_vertices(self, vertex):
        """Get all adjacent vertices of a given vertex"""
        return list(self.graph.get(vertex, {}).keys())

    def dijkstra(self, start, end):
        """
        Find shortest path from start to end using Dijkstra's algorithm.
        Optimized for sparse graphs with 10,000+ nodes.

        Args:
            start: Starting vertex
            end: Ending vertex

        Returns:
            tuple: (path as list of vertices, total distance)
                   Returns ([], float('inf')) if no path exists
        """
        if start not in self.graph:
            raise KeyError(f"Start vertex '{start}' not in graph")
        if end not in self.graph:
            raise KeyError(f"End vertex '{end}' not in graph")

        # Early exit if start == end
        if start == end:
            return [start], 0

        # Initialize distances and previous vertices
        distances = {start: 0}
        previous = {}

        # Priority queue: (distance, vertex)
        pq = [(0, start)]
        visited = set()

        while pq:
            current_dist, current = heapq.heappop(pq)

            # Skip if already visited (handles duplicate entries in pq)
            if current in visited:
                continue

            visited.add(current)

            # Early termination: found shortest path to end
            if current == end:
                return self._reconstruct_path(previous, start, end), current_dist

            # Skip if this distance is outdated
            if current_dist > distances.get(current, float('inf')):
                continue

            # Explore neighbors
            for neighbor, weight in self.graph[current].items():
                if neighbor in visited:
                    continue

                distance = current_dist + weight

                # Only update if we found a shorter path
                if distance < distances.get(neighbor, float('inf')):
                    distances[neighbor] = distance
                    previous[neighbor] = current
                    heapq.heappush(pq, (distance, neighbor))

        # No path found
        return [], float('inf')

    def _reconstruct_path(self, previous, start, end):
        """Reconstruct path from start to end using previous vertices"""
        path = []
        current = end

        while current is not None:
            path.append(current)
            current = previous.get(current)

        path.reverse()

        # Verify path starts at start vertex
        if path and path[0] == start:
            return path
        return []

    def tour_length(self, tour):
        """
        Calculate the total length of a tour (cycle through vertices).
        Tour should be a list of vertices without explicit return to start.
        Example: [A, B, C] implies A->B->C->A
        """
        if not tour:
            return 0
        if len(tour) == 1:
            return 0

        total_length = 0
        for i in range(len(tour)):
            weight = self._get_edge_weight(tour[i], tour[(i + 1) % len(tour)])
            if weight == float('inf'):
                return float('inf')  # Invalid tour
            total_length += weight
        return total_length

    def _get_edge_weight(self, src, dest):
        """Get weight of edge from src to dest"""
        return self.graph[src].get(dest, float('inf'))

    def __str__(self):
        return str(self.graph)


# Performance test and demonstration
if __name__ == "__main__":
    import time
    import random

    print("=== Performance Test: Large Sparse Graph ===\n")

    # Create a large sparse graph (10,000 nodes)
    num_nodes = 10000
    edges_per_node = 5  # Sparse graph

    g = Graph(directed=True)

    print(f"Creating graph with {num_nodes} nodes...")
    start_time = time.time()

    # Add vertices
    for i in range(num_nodes):
        g.add_vertex(i)

    # Add edges (sparse connectivity)
    random.seed(42)
    for i in range(num_nodes):
        # Connect to random nodes
        for _ in range(edges_per_node):
            dest = random.randint(0, num_nodes - 1)
            if dest != i:
                weight = random.randint(1, 100)
                g.add_edge(i, dest, weight)

    setup_time = time.time() - start_time
    print(f"Graph created in {setup_time:.4f} seconds")
    print(f"Approximate edges: {num_nodes * edges_per_node}\n")

    # Test Dijkstra on various path lengths
    test_cases = [
        (0, 100, "Short distance"),
        (0, 1000, "Medium distance"),
        (0, 9999, "Long distance"),
    ]

    for start, end, desc in test_cases:
        start_time = time.time()
        path, distance = g.dijkstra(start, end)
        elapsed = time.time() - start_time

        print(f"{desc} ({start} -> {end}):")
        print(f"  Distance: {distance}")
        print(f"  Path length: {len(path)} nodes")
        print(f"  Time: {elapsed:.4f} seconds")
        print(f"  {'✓ PASS' if elapsed < 0.5 else '✗ FAIL'} (< 0.5s requirement)\n")

    # Small example for clarity
    print("\n=== Simple Example ===\n")
    g_small = Graph(directed=False)

    for v in ['A', 'B', 'C', 'D', 'E']:
        g_small.add_vertex(v)

    g_small.add_edge('A', 'B', 4)
    g_small.add_edge('A', 'C', 2)
    g_small.add_edge('B', 'C', 1)
    g_small.add_edge('B', 'D', 5)
    g_small.add_edge('C', 'D', 8)
    g_small.add_edge('C', 'E', 10)
    g_small.add_edge('D', 'E', 2)

    path, distance = g_small.dijkstra('A', 'E')
    print(f"Shortest path from A to E: {' -> '.join(path)}")
    print(f"Total distance: {distance}")