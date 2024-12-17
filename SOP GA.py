import random

# Sphere Function
def sphere_function(x):
    return sum(x_i ** 2 for x_i in x)

class GeneticAlgorithm:
    def __init__(self, n, bounds, population_size=100, generations=500, mutation_rate=0.01):
        self.n = n
        self.bounds = bounds
        self.population_size = population_size
        self.generations = generations
        self.mutation_rate = mutation_rate
        self.population = self.init_population()

    def init_population(self):
        return [[random.uniform(*self.bounds) for _ in range(self.n)] for _ in range(self.population_size)]

    def fitness(self, x):
        return sphere_function(x)

    def selection(self):
        sorted_population = sorted(self.population, key=lambda x: self.fitness(x))
        return sorted_population[:self.population_size // 2]

    def crossover(self, parent1, parent2):
        child = [(p1 + p2) / 2 for p1, p2 in zip(parent1, parent2)]
        return child

    def mutate(self, individual):
        if random.random() < self.mutation_rate:
            idx = random.randint(0, self.n - 1)
            individual[idx] += random.uniform(-1, 1)

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
        best_solution = min(self.population, key=lambda x: self.fitness(x))
        return best_solution, self.fitness(best_solution)

# Example usage
ga_solver = GeneticAlgorithm(n=3, bounds=(-5, 5))
print("Genetic Algorithm Solution:", ga_solver.solve())

