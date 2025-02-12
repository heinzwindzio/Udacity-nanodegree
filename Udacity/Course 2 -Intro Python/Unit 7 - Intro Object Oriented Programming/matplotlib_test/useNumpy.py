import numpy as np
import matplotlib.pyplot as plt

x = np.arange(0, 5, .001)
y = np.sin(x)
plt.plot(x, y)
plt.show()

"""
Demonstrate Histogram function
"""
# Generate some data
data = np.random.randn(1000) 

# Create the histogram
plt.hist(data, bins=30)

# Add labels and title
plt.xlabel('Value')
plt.ylabel('Frequency')
plt.title('Histogram Example')

# Display the plot
plt.show() 