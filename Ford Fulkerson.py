from collections import deque

class FordFulkerson:
    def __init__(self, array_index_string_equivalents):
        self.vertex_count = len(array_index_string_equivalents)
        self.array_index_string_equivalents = array_index_string_equivalents

    def max_flow(self, graph, vertex_s, vertex_t):
        max_flow = 0
        parent = [-1] * self.vertex_count
        residual_graph = [row[:] for row in graph]

        # Keep finding augmenting paths while they exist
        while self.bfs(residual_graph, vertex_s, vertex_t, parent):
            bottleneck_flow = float('inf')

            # Find the bottleneck capacity of the current path
            vertex_v = vertex_t
            while vertex_v != vertex_s:
                vertex_u = parent[vertex_v]
                bottleneck_flow = min (bottleneck_flow,  residual_graph[vertex_u][vertex_v])
                vertex_v = parent[vertex_v]

            # Update residual capacities of the edges and reverse edges
            vertex_v = vertex_t
            while vertex_v != vertex_s:
                vertex_u = parent[vertex_v]
                residual_graph[vertex_u][vertex_v] -= bottleneck_flow
                residual_graph[vertex_v][vertex_u] += bottleneck_flow
                vertex_v = parent[vertex_v]

            max_flow += bottleneck_flow
        # Find the reachable vertices after all flows are sent
        reachable = self.find_reachable_vertices(residual_graph, vertex_s)
        min_cut_edges = self.find_min_cut_edges(graph, residual_graph, reachable)

        return max_flow, min_cut_edges

    def bfs(self, residual_graph, vertex_s, vertex_t, parent):
        visited = [False] * self.vertex_count
        vertex_queue = deque([vertex_s])
        visited[vertex_s] = True
        parent[vertex_s] = -1

        while vertex_queue:
            vertex_u = vertex_queue.popleft()
            for vertex_v in range(self.vertex_count):
                if not visited[vertex_v] and residual_graph[vertex_u][vertex_v] > 0:
                    vertex_queue.append(vertex_v)
                    parent[vertex_v] = vertex_u
                    visited[vertex_v] = True

        return visited[vertex_t]

    def find_reachable_vertices(self, residual_graph, vertex_s):
        """Find all vertices reachable from the source in the residual graph."""
        visited = [False] * self.vertex_count
        queue = deque([vertex_s])
        visited[vertex_s] = True

        while queue:
            vertex_u = queue.popleft()
            for vertex_v in range(self.vertex_count):
                if not visited[vertex_v] and residual_graph[vertex_u][vertex_v] > 0:
                    queue.append(vertex_v)
                    visited[vertex_v] = True

        return visited

    def find_min_cut_edges(self, graph, residual_graph, reachable):
        """Find the edges that form the min-cut."""
        min_cut_edges = []
        for u in range(self.vertex_count):
            for v in range(self.vertex_count):
                # If u is reachable and v is not, and the original graph had capacity
                if reachable[u] and not reachable[v] and graph[u][v] > 0:
                    min_cut_edges.append((self.array_index_string_equivalents[u], 
                                          self.array_index_string_equivalents[v]))
        return min_cut_edges




if __name__ == "__main__":
    # Define the graph and its vertex labels
    array_index_string_equivalents = ["S", "2", "3", "4", "5", "6", "7", "T"]
    graph_matrix = [
        [0, 10, 5, 15, 0, 0, 0, 0],
        [0, 0, 4, 0, 9, 15, 0, 0],
        [0, 0, 0, 4, 0, 8, 0, 0],
        [0, 0, 0, 0, 0, 0, 30, 0],
        [0, 0, 0, 0, 0, 15, 0, 10],
        [0, 0, 0, 0, 0, 0, 15, 10],
        [0, 0, 6, 0, 0, 0, 0, 10],
        [0, 0, 0, 0, 0, 0, 0, 0]
    ]
    # Initialize the Ford-Fulkerson algorithm
    max_flow_finder = FordFulkerson(array_index_string_equivalents)

    # Define source and sink
    vertex_s = 0  # Source vertex 'S'
    vertex_t = len(array_index_string_equivalents) - 1  # Sink vertex 'T'

    # Calculate the max flow and the min cut edges
    max_flow, min_cut_edges = max_flow_finder.max_flow(graph_matrix, vertex_s, vertex_t)

    # Print results
    print(f"Max Flow: {max_flow}")
    print("Min Cut Edges:")
    for edge in min_cut_edges:
        print(f"{edge[0]} -> {edge[1]}")
