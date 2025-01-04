# Why use NumPy?
import time
import numpy as np


x = np.random.random(100000000)

# Case 1
# start = time.time()
# sum(x) / len(x)
# print(time.time() - start)

# Case 2
start = time.time()
np.mean(x)
print(time.time() - start)

## We create a 1D ndarray that contains only integers
x = np.array([1, 2, 3, 4, 5])

## Let's print the ndarray we just created using the print() command
print('x = ', x)

