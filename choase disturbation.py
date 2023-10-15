import numpy as np
import matplotlib.pyplot as plt

# Generate a sample dataset (randomly generated values)
data = np.random.randn(1000000000)  # 1000 random values from a standard normal distribution

# Create the histogram plot
plt.hist(data, bins=100)

# Add labels and title
plt.xlabel('Values')
plt.ylabel('Frequency')
plt.title('Histogram Plot')

# Show the plot
plt.show()
