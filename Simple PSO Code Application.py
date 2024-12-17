import numpy as np

# Objective function (example: minimize sum of squares)
def objective_function(x):
    return np.sum(x**2)

# Parameters
num_particles = 10          # Number of particles
dimensions = 2              # Number of dimensions
max_iterations = 50         # Number of iterations
bounds = [-10, 10]          # Bounds for the search space
w = 0.5                     # Inertia weight
c1, c2 = 1.5, 1.5           # Cognitive and social coefficients

# Initialize particles (random positions and velocities)
positions = np.random.uniform(bounds[0], bounds[1], (num_particles, dimensions))
velocities = np.random.uniform(-1, 1, (num_particles, dimensions))

# Initialize personal best positions and values
p_best_positions = positions.copy()
p_best_values = np.array([objective_function(p) for p in positions])

# Initialize global best position and value
g_best_position = p_best_positions[np.argmin(p_best_values)]
g_best_value = np.min(p_best_values)

# PSO Algorithm
for iteration in range(max_iterations):
    for i in range(num_particles):
        # Update velocity
        r1, r2 = np.random.rand(dimensions), np.random.rand(dimensions)
        velocities[i] = (
            w * velocities[i] +
            c1 * r1 * (p_best_positions[i] - positions[i]) +
            c2 * r2 * (g_best_position - positions[i])
        )

        # Update position
        positions[i] += velocities[i]
        positions[i] = np.clip(positions[i], bounds[0], bounds[1])  # Keep within bounds

        # Update personal best
        fitness = objective_function(positions[i])
        if fitness < p_best_values[i]:
            p_best_values[i] = fitness
            p_best_positions[i] = positions[i]

    # Update global best
    best_particle = np.argmin(p_best_values)
    if p_best_values[best_particle] < g_best_value:
        g_best_value = p_best_values[best_particle]
        g_best_position = p_best_positions[best_particle]

    # Print progress
    print(f"Iteration {iteration + 1}, Best Value: {g_best_value}")

# Final result
print("\nOptimal Solution:", g_best_position)
print("Objective Function Value:", g_best_value)
