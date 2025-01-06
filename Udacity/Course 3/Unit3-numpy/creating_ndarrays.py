import numpy as np

# create an ndarray with all zeros
X = np.zeros((3,4))
Y = np.ones((2, 3))

# full((shape, constant value))
Z = np.full((2, 3), 5) 



print(X)
print(X.shape)
print(X.dtype)
print(type(X))
print(Y)
print(Z)

# create an identity matrix with nparray
I = np.eye(5)
print(I)

# create a diagonal matrix with nparray
D = np.diag([10, 20, 30, 50])
print(D)

# return evenly spaced values
# np.arange(start, stop, step)
# np.arange([start, ]stop, [step, ]dtype=None)
# start is INCLUSIVE, stop is EXCLUSIVE
A = np.arange(10)
print(A)

A = np.arange(4, 10)
print(A)

A = np.arange(1, 14, 3)
print(A)

# return evenly spaced numbers OVER A SPECIFIED INTERVAL
# np.linspace(start, stop, num=50, endpoint=True, retstep=False, dtype=None)
# DEFAULT IS 50
l = np.linspace(0, 25)
print(l)

# linespace will be the same as number of rows!
l = np.linspace(0, 25, 10)
print(l)

# reshape the ndarray to create a RANK 2 ARRAY
# np.reshape() is a function
R = np.arange(20)
S = np.reshape(R, (4, 5))
print(S)

# np.ndarray.reshape() is a method
# call the METHOD on the nparray
T = R.reshape(5, 4)
print(T)

U = np.arange(20).reshape(4, 5)
print(U)

V = np.linspace(0,50,10, endpoint=False).reshape(5,2)
print(V)

# create an nparray with random floats
# np.random.random(number or shape)
W = np.random.random(5)
print(W)

X = np.random.random((3,3))
print(X)

Z = np.random.randint(0, 10, (4, 3))
print(Z)

# create an nparray with random 'Normal' distribution numbers
# random.normal(mean, standard deviation, size)
X = np.random.normal(0, 0.1, size=(1000,1000))
print(X)