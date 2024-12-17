import torch
import random
import torch.nn as nn
import torch.optim as optim
import numpy as np

# Define the Sphere function
def sphere_function(position):
    return np.sum(np.array(position)**2)

class SimpleNN(nn.Module):
    def __init__(self, n):
        super(SimpleNN, self).__init__()
        self.fc1 = nn.Linear(n, 32)
        self.fc2 = nn.Linear(32, 16)
        self.fc3 = nn.Linear(16, n)

    def forward(self, x):
        x = torch.relu(self.fc1(x))
        x = torch.relu(self.fc2(x))
        return self.fc3(x)

# Train the Neural Network
def train_nn(n, bounds, epochs=500, learning_rate=0.01):
    model = SimpleNN(n)
    optimizer = optim.Adam(model.parameters(), lr=learning_rate)
    loss_fn = nn.MSELoss()

    for epoch in range(epochs):
        input_data = torch.FloatTensor([random.uniform(*bounds) for _ in range(n)])
        target = torch.FloatTensor([0] * n)

        optimizer.zero_grad()
        output = model(input_data)
        loss = loss_fn(output, target)
        loss.backward()
        optimizer.step()

    final_solution = model(torch.FloatTensor([random.uniform(*bounds) for _ in range(n)])).detach().numpy()
    return final_solution, sphere_function(final_solution)

# Example usage
print("Neural Network Optimization Solution:", train_nn(n=3, bounds=(-5, 5)))
