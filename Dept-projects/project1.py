# Date : 15-01-25
# 1. generate 500 random no. which are on the bell curve distribution. 
import numpy as np
import matplotlib.pyplot as plt

# Parameters for the normal distribution
mean = 0  # Mean of the distribution
std_dev = 1  # Standard deviation of the distribution

# Generate 500 random numbers following a normal distribution
random_numbers = np.random.normal(mean, std_dev, 500)

# Plot the histogram to visualize the bell curve distribution
plt.figure(figsize=(10, 6))
plt.hist(random_numbers, bins=30, density=True, alpha=0.7, color='blue', edgecolor='black')

# Add the theoretical normal distribution curve
x = np.linspace(min(random_numbers), max(random_numbers), 1000)
plt.plot(x, (1 / (std_dev * np.sqrt(2 * np.pi))) * np.exp(-0.5 * ((x - mean) / std_dev) ** 2), color='red', lw=2)

plt.title("Histogram of Random Numbers (Bell Curve Distribution)")
plt.xlabel("Value")
plt.ylabel("Density")
plt.grid()
plt.show()
