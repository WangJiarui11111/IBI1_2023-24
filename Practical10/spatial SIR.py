# import necessary libraries
import numpy as np
import matplotlib.pyplot as plt

# Define the basic variables of the model
N = 100  # Population size
beta = 0.3  # Infection probability
gamma = 0.05  # Recovery probability
time_max = 100

# make array of all susceptible population
population = np.zeros((N, N), dtype=int)

# Choose one random point for where the outbreak happens
outbreak = (np.random.choice(N), np.random.choice(N))
population[outbreak] = 1  # Infect the chosen point

# Plot the initial state
plt.figure(figsize=(6, 4), dpi=150)
plt.imshow(population, cmap='viridis', interpolation='nearest')
plt.title('Initial State')
plt.show()

for t in range(time_max):
    # Copy current state to handle recovery
    population_copy = population.copy()

    # Find infected points
    infectedIndex = np.where(population == 1)

    # Loop through all infected points
    for i in range(len(infectedIndex[0])):
        x, y = infectedIndex[0][i], infectedIndex[1][i]

        # Infect each neighbor with probability beta
        for dx in [-1, 0, 1]:
            for dy in [-1, 0, 1]:
                if dx == 0 and dy == 0:
                    continue  # Skip the current cell (itself)
                nx, ny = x + dx, y + dy
                if 0 <= nx < N and 0 <= ny < N:  # Check for grid boundaries
                    if population[nx, ny] == 0:  # Only infect susceptible neighbors
                        if np.random.random() < beta:
                            population_copy[nx, ny] = 1

    # Recovery process
    for x, y in zip(*infectedIndex):
        if np.random.random() < gamma:
            population_copy[x, y] = 2

    # Update the population with the new state after infection and recovery
    population = population_copy

    # Plot the figure for the current time point
    if t < time_max - 1:
        plt.imshow(population, cmap='viridis', interpolation='nearest')
        plt.title(f'Time Point {t + 1}')
        plt.show()
        plt.clf()  # Clear the figure for the next iteration

# Final plot after all time points have passed
plt.figure(figsize=(6, 4), dpi=150)
plt.imshow(population, cmap='viridis', interpolation='nearest')
plt.title(f'Final Time Point {time_max}')
plt.show()
