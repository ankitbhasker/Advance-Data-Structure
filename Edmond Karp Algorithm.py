from collections import deque, defaultdict

class Graph:
    def __init__(self, vertices):
        self.V = vertices
        self.graph = defaultdict(lambda: defaultdict(int))  # Residual graph

    def add_edge(self, u, v, w):
        self.graph[u][v] += w  # If there are parallel edges, sum them up

    def bfs(self, source, sink, parent):
        visited = [False] * self.V
        queue = deque([source])
        visited[source] = True

        # Perform BFS to find a path from source to sink
        while queue:
            u = queue.popleft()

            for v, capacity in self.graph[u].items():
                if not visited[v] and capacity > 0:
                    queue.append(v)
                    visited[v] = True
                    parent[v] = u
                    if v == sink:
                        return True

        return False

    def edmonds_karp(self, source, sink):
        parent = [-1] * self.V  # Array to store path
        max_flow = 0

        # Augment the flow while there is a path from source to sink
        while self.bfs(source, sink, parent):
            # Find the maximum flow through the path found by BFS
            path_flow = float('Inf')
            s = sink

            while s != source:
                path_flow = min(path_flow, self.graph[parent[s]][s])
                s = parent[s]

            # update residual capacities of the edges and reverse edges along the path
            v = sink
            while v != source:
                u = parent[v]
                self.graph[u][v] -= path_flow
                self.graph[v][u] += path_flow
                v = parent[v]

            max_flow += path_flow

        return max_flow


# Example usage
g = Graph(6)
g.add_edge(0, 1, 16)
g.add_edge(0, 2, 13)
g.add_edge(1, 2, 10)
g.add_edge(1, 3, 12)
g.add_edge(2, 1, 4)
g.add_edge(2, 4, 14)
g.add_edge(3, 2, 9)
g.add_edge(3, 5, 20)
g.add_edge(4, 3, 7)
g.add_edge(4, 5, 4)

source = 0
sink = 5
max_flow = g.edmonds_karp(source, sink)
print(f"The maximum possible flow is {max_flow}")
