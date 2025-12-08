def tsp_medium_graph(self, start):
    """
    Solve TSP for medium graphs (~300 nodes) with better solution quality.
    Uses greedy nearest neighbor with 2-opt local search optimization.

    Parameters:
    start: The starting node

    Returns:
    tuple: (total_distance, tour_path)
           tour_path is a list of nodes representing the tour (including return to start)
    """
    if start not in self.graph:
        raise KeyError(f"Start vertex '{start}' not in graph")

    if len(self.graph) == 0:
        return 0, []
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

    def tsp(self, start):
        """
        Solve the Travelling Salesman Problem using a greedy nearest neighbor heuristic.
        Optimized for large graphs (~1000 nodes). No guarantee of optimal solution.

        Parameters:
        start: The starting node

        Returns:
        tuple: (total_distance, tour_path)
               tour_path is a list of nodes representing the tour (including return to start)
        """
        if start not in self.graph:
            raise KeyError(f"Start vertex '{start}' not in graph")

        if len(self.graph) == 0:
            return 0, []

        if len(self.graph) == 1:
            return 0, [start]

        # Greedy nearest neighbor algorithm
        unvisited = set(self.graph.keys())
        tour = [start]
        current = start
        total_distance = 0
        unvisited.remove(start)

        # Build tour by always going to nearest unvisited neighbor
        while unvisited:
            nearest = None
            min_distance = float('inf')

            # Find nearest unvisited neighbor
            for neighbor in unvisited:
                distance = self._get_edge_weight(current, neighbor)
                if distance < min_distance:
                    min_distance = distance
                    nearest = neighbor

            if nearest is None or min_distance == float('inf'):
                # No valid edge found - graph is not complete
                return float('inf'), []

            # Move to nearest neighbor
            tour.append(nearest)
            total_distance += min_distance
            current = nearest
            unvisited.remove(nearest)

        # Return to start to complete the tour
        return_distance = self._get_edge_weight(current, start)
        if return_distance == float('inf'):
            return float('inf'), []

        total_distance += return_distance
        tour.append(start)  # Complete the cycle

        return total_distance, tour

    def tsp_medium_graph(self, start):
        """
        Solve TSP for medium graphs (~300 nodes) with better solution quality.
        Uses greedy nearest neighbor with 2-opt local search optimization.

        Parameters:
        start: The starting node

        Returns:
        tuple: (total_distance, tour_path)
               tour_path is a list of nodes representing the tour (including return to start)
        """
        if start not in self.graph:
            raise KeyError(f"Start vertex '{start}' not in graph")

        if len(self.graph) == 0:
            return 0, []

        if len(self.graph) == 1:
            return 0, [start]

        # Step 1: Get initial tour using nearest neighbor
        distance, tour = self.tsp(start)

        if distance == float('inf'):
            return distance, tour

        # Step 2: Improve with 2-opt local search
        # Remove the duplicate start node at the end for easier processing
        tour = tour[:-1]

        improved = True
        max_iterations = 100  # Limit iterations to stay under time constraint
        iteration = 0

        while improved and iteration < max_iterations:
            improved = False
            iteration += 1

            # Try all possible 2-opt swaps
            for i in range(1, len(tour) - 1):
                for j in range(i + 1, len(tour)):
                    # Calculate current distance of the two edges
                    current_dist = (
                            self._get_edge_weight(tour[i-1], tour[i]) +
                            self._get_edge_weight(tour[j], tour[(j+1) % len(tour)])
                    )

                    # Calculate distance after swap
                    new_dist = (
                            self._get_edge_weight(tour[i-1], tour[j]) +
                            self._get_edge_weight(tour[i], tour[(j+1) % len(tour)])
                    )

                    # If improvement found, do the swap
                    if new_dist < current_dist:
                        # Reverse the segment between i and j
                        tour[i:j+1] = reversed(tour[i:j+1])
                        improved = True
                        break

                if improved:
                    break

        # Recalculate total distance and add return to start
        total_distance = 0
        for i in range(len(tour)):
            weight = self._get_edge_weight(tour[i], tour[(i + 1) % len(tour)])
            if weight == float('inf'):
                return float('inf'), []
            total_distance += weight

        # Add start node at the end to complete the cycle
        tour.append(start)

        return total_distance, tour

    def __str__(self):
        return str(self.graph)


# Performance test and demonstration
if __name__ == "__main__":
    import time
    import random

    print("=== Performance Test: Dijkstra on Large Sparse Graph ===\n")

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
    print("\n=== Simple Dijkstra Example ===\n")
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

    print("\n" + "="*60)
    print("=== Performance Test: TSP on Complete Graph (~1000 nodes) ===")
    print("="*60 + "\n")

    # Create complete graphs of various sizes
    tsp_test_sizes = [100, 500, 1000]

    for size in tsp_test_sizes:
        print(f"\nTesting TSP (greedy) with {size} nodes (complete graph)...")
        g_tsp = Graph(directed=False)

        # Add vertices
        for i in range(size):
            g_tsp.add_vertex(i)

        # Create complete graph - every node connected to every other node
        random.seed(42)
        edge_count = 0
        for i in range(size):
            for j in range(i + 1, size):
                weight = random.randint(1, 100)
                g_tsp.add_edge(i, j, weight)
                edge_count += 1

        print(f"  Created complete graph with {edge_count} edges")

        # Run TSP from node 0
        start_time = time.time()
        distance, tour = g_tsp.tsp(0)
        elapsed = time.time() - start_time

        print(f"  Total tour distance: {distance}")
        print(f"  Tour visits {len(tour)} nodes (including return)")
        print(f"  Time: {elapsed:.4f} seconds")
        print(f"  {'✓ PASS' if elapsed < 0.5 else '✗ FAIL'} (< 0.5s requirement)")

        # Verify tour validity
        if len(tour) == size + 1 and tour[0] == tour[-1] == 0:
            unique_nodes = set(tour[:-1])
            if len(unique_nodes) == size:
                print(f"  ✓ Tour is valid (visits all {size} nodes exactly once)")
            else:
                print(f"  ✗ Tour error: only {len(unique_nodes)} unique nodes")
        else:
            print(f"  ✗ Tour structure error")

    print("\n" + "="*60)
    print("=== Performance Test: TSP Medium Graph with 2-opt (~300 nodes) ===")
    print("="*60 + "\n")

    # Test medium-sized graphs with the improved algorithm
    medium_test_sizes = [50, 100, 200, 300]

    for size in medium_test_sizes:
        print(f"\nTesting TSP Medium (2-opt) with {size} nodes...")
        g_med = Graph(directed=False)

        # Add vertices
        for i in range(size):
            g_med.add_vertex(i)

        # Create complete graph
        random.seed(42)
        for i in range(size):
            for j in range(i + 1, size):
                weight = random.randint(1, 100)
                g_med.add_edge(i, j, weight)

        # Run both algorithms for comparison
        start_time = time.time()
        greedy_dist, greedy_tour = g_med.tsp(0)
        greedy_time = time.time() - start_time

        start_time = time.time()
        improved_dist, improved_tour = g_med.tsp_medium_graph(0)
        improved_time = time.time() - start_time

        improvement = ((greedy_dist - improved_dist) / greedy_dist * 100) if greedy_dist > 0 else 0

        print(f"  Greedy tour distance: {greedy_dist} (time: {greedy_time:.4f}s)")
        print(f"  2-opt tour distance:  {improved_dist} (time: {improved_time:.4f}s)")
        print(f"  Improvement: {improvement:.2f}%")
        print(f"  {'✓ PASS' if improved_time < 1.5 else '✗ FAIL'} (< 1.5s requirement)")

        # Verify tour validity
        if len(improved_tour) == size + 1 and improved_tour[0] == improved_tour[-1] == 0:
            unique_nodes = set(improved_tour[:-1])
            if len(unique_nodes) == size:
                print(f"  ✓ Tour is valid (visits all {size} nodes exactly once)")
            else:
                print(f"  ✗ Tour error: only {len(unique_nodes)} unique nodes")
        else:
            print(f"  ✗ Tour structure error")

    print("\n" + "="*60)
    print("=== Simple TSP Example ===")
    print("="*60 + "\n")

    # Small complete graph for demonstration
    g_tsp_small = Graph(directed=False)
    nodes = ['A', 'B', 'C', 'D']

    for node in nodes:
        g_tsp_small.add_vertex(node)

    # Create complete graph with specific weights
    edges = [
        ('A', 'B', 10), ('A', 'C', 15), ('A', 'D', 20),
        ('B', 'C', 35), ('B', 'D', 25),
        ('C', 'D', 30)
    ]

    for src, dest, weight in edges:
        g_tsp_small.add_edge(src, dest, weight)

    distance, tour = g_tsp_small.tsp('A')
    print(f"TSP Tour starting from 'A': {' -> '.join(tour)}")
    print(f"Total distance: {distance}")
    print(f"\nNote: This is a greedy nearest-neighbor solution.")
    print(f"It may not be the optimal tour, but it's fast!")