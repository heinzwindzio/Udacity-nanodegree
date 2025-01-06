import numpy as np

# Replace None with appropriate code
X = np.zeros((4,4))
print(X)

y = np.array([1, 2, 3, 4])

print(X + y)




### Notebook grading
solution = np.ones((4,4)) * np.arange(1,5)
if type(X) != np.ndarray:
    print("`X` should be an ndarray")
elif np.array_equal(X, solution):
    print("Nice work! You can view my solution below")
elif X.shape != solution.shape:
    print("Your answer for `X` has a shape of {} but it should be 4 x 4".format(X.shape))
else:
    print("Your answer for `X` has the right shape but incorrect values")