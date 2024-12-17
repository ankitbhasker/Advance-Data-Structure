import numpy as np

# Define the Sphere function
def sphere_function(position):
    return np.sum(np.array(position)**2)

class AntColonyOptimization:
    def __init__(self, n, bounds, num_ants=30, iterations=100, evaporation=0.1, alpha=1, beta=2):
        self.n = n  # Number of dimensions
        self.bounds = bounds  # Search bounds
        self.num_ants = num_ants
        self.iterations = iterations
        self.evaporation = evaporation
        self.alpha = alpha  # Pheromone importance
        self.beta = beta  # Desirability importance
        self.pheromone = np.ones((n,))  # Initial pheromone (one per dimension)

    def optimize(self):
        best_solution = None
        best_value = float("inf")

        for iteration in range(self.iterations):
            solutions = []
            solution_values = []

            # Step 1: Construct solutions
            for _ in range(self.num_ants):
                solution = []
                for i in range(self.n):
                    # Compute probabilities for current dimension
                    desirability = 1.0 / (abs(self.bounds[1] - self.bounds[0]) + 1e-10)
                    probability = (self.pheromone[i] ** self.alpha) * (desirability ** self.beta)
                    
                    # Sample solution within bounds
                    sample = np.random.uniform(self.bounds[0], self.bounds[1])
                    solution.append(sample)
                solutions.append(solution)

                # Evaluate the solution
                solution_value = sphere_function(solution)
                solution_values.append(solution_value)

                # Update the best solution
                if solution_value < best_value:
                    best_value = solution_value
                    best_solution = solution

            # Step 2: Update pheromones
            for i in range(self.n):
                # Evaporate pheromones
                self.pheromone[i] *= (1 - self.evaporation)

                # Deposit pheromones based on solution quality
                for j, solution in enumerate(solutions):
                    self.pheromone[i] += (1.0 / (solution_values[j] + 1e-10)) * solution[i]

        return best_solution, best_value


# Example usage
aco_solver = AntColonyOptimization(n=3, bounds=(-5, 5), iterations=200, num_ants=50)
best_solution, best_value = aco_solver.optimize()
print("Ant Colony Optimization Solution:")
print("Best Position:", best_solution)
print("Best Value:", best_value)
