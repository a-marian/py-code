from collections import deque

graph = {'A':['B', 'C'], 'B':['C', 'D'], 'C':['D'], 'D':['C'], 'E':['F'], 'F':['C']}
def find_shortest_path(graph, start, end):
        dist = {start: [start]}
        q = deque([start])
        while len(q):
            at = q.popleft()
            for next in graph[at]:
                if next not in dist:
                    dist[next] = dist[at], [next]
                    q.append(next)
        return dist.get(end)

print(find_shortest_path(graph, 'A', 'D'))