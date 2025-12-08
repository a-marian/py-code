import unittest
import heapq

def dijkstra(graph, start):
    # Ensure every node from 0 to 19 is represented in the graph as a key
    for node in range(20):
        if node not in graph:
            graph[node] = []

    distances = {node: float('infinity') for node in range(20)}
    distances[start] = 0
    pq = [(0, start)]
    visited = set()

    while pq:
        current_distance, current_node = heapq.heappop(pq)
        if current_node in visited:
            continue
        visited.add(current_node)

        for neighbor, weight in graph[current_node]:
            # Defensive: ensure weight is a number
            weight = float(weight)
            distance = current_distance + weight
            if distance < distances[neighbor]:
                distances[neighbor] = distance
                heapq.heappush(pq, (distance, neighbor))

    # Correctly check reachability
    all_nodes_visited = all(distances[node] < float('infinity') for node in distances)

    return distances, all_nodes_visited


class TestDijkstra(unittest.TestCase):

    def test_simple_path(self):
        graph = {
            0: [(1, 1)],
            1: [(2, 1)],
            2: []
        }
        distances, all_reached = dijkstra(graph, 0)
        self.assertEqual(distances[2], 2)
        self.assertFalse(all_reached)

    def test_multiple_paths(self):
        graph = {
            0: [(1, 2), (2, 4)],
            1: [(2, 1)],
            2: []
        }
        distances, all_reached = dijkstra(graph, 0)
        self.assertEqual(distances[2], 3)  # 0->1->2
        self.assertFalse(all_reached)

    def test_unreachable_nodes(self):
        graph = {
            0: [(1, 1)],
            1: []
            # nodes 2..19 missing
        }
        distances, all_reached = dijkstra(graph, 0)
        for node in range(2, 20):
            self.assertEqual(distances[node], float('infinity'))
        self.assertFalse(all_reached)

    def test_fully_connected(self):
        # Each node connects to node+1 with a weight of 1
        graph = {i: [(i+1, 1)] for i in range(19)}
        graph[19] = []
        distances, all_reached = dijkstra(graph, 0)
        self.assertTrue(all_reached)
        self.assertEqual(distances[19], 19)
        self.assertEqual(distances[0], 0)

    def test_single_node_graph(self):
        graph = {0: []}
        distances, all_reached = dijkstra(graph, 0)
        self.assertEqual(distances[0], 0)
        for node in range(1, 20):
            self.assertEqual(distances[node], float('infinity'))
        self.assertFalse(all_reached)

    def test_cycle(self):
        graph = {
            0: [(1, 1)],
            1: [(2, 1)],
            2: [(0, 1)]
        }
        distances, all_reached = dijkstra(graph, 0)
        self.assertEqual(distances[2], 2)
        self.assertFalse(all_reached)

    def test_weights_as_strings(self):
        graph = {
            0: [(1, "3.5"), (2, "7.1")],
            1: [(2, "2.5")],
            2: []
        }
        distances, all_reached = dijkstra(graph, 0)
        self.assertAlmostEqual(distances[2], 6.0)
        self.assertFalse(all_reached)

if __name__ == '__main__':
    unittest.main()
