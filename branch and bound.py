import math
import random

class BranchAndBoundTSP:
    def __init__(self, graph):
        self.graph = graph
        self.n = len(graph)
        self.min_cost = float("inf")
        self.path = []

    def tsp_util(self, level, cost, current_path, visited):
        if level == self.n:
            if self.graph[current_path[-1]][current_path[0]] != 0:
                total_cost = cost + self.graph[current_path[-1]][current_path[0]]
                if total_cost < self.min_cost:
                    self.min_cost = total_cost
                    self.path = current_path[:]
            return

        for i in range(self.n):
            if not visited[i] and self.graph[current_path[-1]][i] != 0:
                temp_cost = cost + self.graph[current_path[-1]][i]
                if temp_cost < self.min_cost:
                    visited[i] = True
                    current_path.append(i)
                    self.tsp_util(level + 1, temp_cost, current_path, visited)
                    visited[i] = False
                    current_path.pop()

    def solve(self):
        visited = [False] * self.n
        visited[0] = True
        self.tsp_util(1, 0, [0], visited)
        return self.min_cost, self.path

# Example usage
graph = [
    [0, 10, 15, 20],
    [10, 0, 35, 25],
    [15, 35, 0, 30],
    [20, 25, 30, 0]
]
bb_solver = BranchAndBoundTSP(graph)
print("Branch and Bound Solution:", bb_solver.solve())

def tsp_dp(graph):
    n = len(graph)
    dp = [[None] * (1 << n) for _ in range(n)]

    def solve(pos, mask):
        if mask == (1 << n) - 1:
            return graph[pos][0] or float("inf")
        if dp[pos][mask] is not None:
            return dp[pos][mask]
        
        ans = float("inf")
        for city in range(n):
            if mask & (1 << city) == 0 and graph[pos][city] != 0:
                ans = min(ans, graph[pos][city] + solve(city, mask | (1 << city)))
        dp[pos][mask] = ans
        return ans

    min_cost = solve(0, 1)
    return min_cost

# Example usage
print("Dynamic Programming Solution:", tsp_dp(graph))

class GeneticAlgorithmTSP:
    def __init__(self, graph, population_size=100, generations=500, mutation_rate=0.01):
        self.graph = graph
        self.n = len(graph)
        self.population_size = population_size
        self.generations = generations
        self.mutation_rate = mutation_rate
        self.population = self.init_population()

    def init_population(self):
        return [random.sample(range(self.n), self.n) for _ in range(self.population_size)]

    def fitness(self, path):
        return sum(self.graph[path[i]][path[(i + 1) % self.n]] for i in range(self.n))

    def selection(self):
        sorted_population = sorted(self.population, key=lambda path: self.fitness(path))
        return sorted_population[:self.population_size // 2]

    def crossover(self, parent1, parent2):
        child = [-1] * self.n
        start, end = sorted(random.sample(range(self.n), 2))
        child[start:end] = parent1[start:end]
        fill_pos = end
        for gene in parent2:
            if gene not in child:
                if fill_pos == self.n:
                    fill_pos = 0
                child[fill_pos] = gene
                fill_pos += 1
        return child

    def mutate(self, path):
        if random.random() < self.mutation_rate:
            i, j = random.sample(range(self.n), 2)
            path[i], path[j] = path[j], path[i]

    def evolve(self):
        new_population = []
        selected_parents = self.selection()
        while len(new_population) < self.population_size:
            parent1, parent2 = random.sample(selected_parents, 2)
            child = self.crossover(parent1, parent2)
            self.mutate(child)
            new_population.append(child)
        self.population = new_population

    def solve(self):
        for _ in range(self.generations):
            self.evolve()
        best_path = min(self.population, key=lambda path: self.fitness(path))
        return self.fitness(best_path), best_path

# Example usage
ga_solver = GeneticAlgorithmTSP(graph)
print("Genetic Algorithm Solution:", ga_solver.solve())

