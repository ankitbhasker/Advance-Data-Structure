import numpy as np

# Define the Sphere function
def sphere_function(position):
    return np.sum(position**2)

class Particle:
    def __init__(self, n, bounds):
        self.position = np.random.uniform(bounds[0], bounds[1], n)
        self.velocity = np.random.uniform(-1, 1, n)
        self.best_position = np.copy(self.position)
        self.best_value = sphere_function(self.position)

class ParticleSwarmOptimization:
    def __init__(self, n, bounds, num_particles=30, iterations=100, w=0.5, c1=1.5, c2=1.5):
        self.n = n
        self.bounds = bounds
        self.num_particles = num_particles
        self.iterations = iterations
        self.w = w  # inertia weight
        self.c1 = c1  # cognitive parameter
        self.c2 = c2  # social parameter
        self.particles = [Particle(n, bounds) for _ in range(num_particles)]
        self.global_best_position = np.copy(self.particles[0].position)
        self.global_best_value = float("inf")

    def optimize(self):
        for _ in range(self.iterations):
            for particle in self.particles:
                value = sphere_function(particle.position)
                if value < particle.best_value:
                    particle.best_position = np.copy(particle.position)
                    particle.best_value = value
                if value < self.global_best_value:
                    self.global_best_position = np.copy(particle.position)
                    self.global_best_value = value

            for particle in self.particles:
                r1, r2 = np.random.random(self.n), np.random.random(self.n)
                cognitive_velocity = self.c1 * r1 * (particle.best_position - particle.position)
                social_velocity = self.c2 * r2 * (self.global_best_position - particle.position)
                particle.velocity = self.w * particle.velocity + cognitive_velocity + social_velocity
                particle.position += particle.velocity
                particle.position = np.clip(particle.position, self.bounds[0], self.bounds[1])

        return self.global_best_position, self.global_best_value

# Example usage
pso_solver = ParticleSwarmOptimization(n=3, bounds=(-5, 5), iterations=200)
best_position, best_value = pso_solver.optimize()
print("Particle Swarm Optimization Solution:")
print("Best Position:", best_position)
print("Best Value:", best_value)
