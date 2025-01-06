# Why use NumPy?
import time
import numpy as np


#  PYTHON SPEED 

x = np.random.random(100000000)

# Case 1
# start = time.time()
# sum(x) / len(x)
# print(time.time() - start)

# Case 2
start = time.time()
np.mean(x)
print(time.time() - start)


#  NUMPY ARRAYS
## We create a 1D ndarray that contains only integers
x = np.array([1, 2, 3, 4, 5])

## Let's print the ndarray we just created using the print() command
print('x = ', x)


# NUMPY MULTI DIMENSIONAL ARRAYS
print("Here is how ndim gives the dimension of the array:")

## 1-D array
print(x.ndim)

## 2-D array
Y = np.array([[1,2,3],[4,5,6],[7,8,9], [10,11,12]])
print(Y.ndim)

## Here the`zeros()` is an inbuilt function that you'll study on the next page. 
## The tuple (2, 3, 4( passed as an argument represents the shape of the ndarray
y = np.zeros((2, 3, 4))
print(y.ndim)

## 
print("Here are examples of the shape and dtype methods:")

print('x has dimensions:', x.shape)
print('x is an object of type:', type(x))
print('The elements in x are of type:', x.dtype)

#  ARRAYS WITH STRINGS
## We create a rank 1 ndarray that only contains strings
x = np.array(['Hello', 'World'])

## We print information about x
print('x = ', x)
print('x has dimensions:', x.shape)
print('x is an object of type:', type(x))
print('The elements in x are of type:', x.dtype)

# ARRAYS WITH MIXED TYPES
## We create a rank 1 ndarray from a Python list that contains integers and strings
x = np.array([1, 2, 'World'])

## We print information about x
print('x = ', x)
print('x has dimensions:', x.shape)
print('x is an object of type:', type(x))
print('The elements in x are of type:', x.dtype)

# NUMPY ARRAY OF FLOATS AND INTEGERS - upcasting
## We create a rank 1 ndarray that contains integers
x = np.array([1,2,3])

## We create a rank 1 ndarray that contains floats
y = np.array([1.0,2.0,3.0])

## We create a rank 1 ndarray that contains integers and floats
z = np.array([1, 2.5, 4])

## We print the dtype of each ndarray
print('The elements in x are of type:', x.dtype)
print('The elements in y are of type:', y.dtype)
print('The elements in z are of type:', z.dtype)

# NUMPY ARRAY OF FLOATS AND INTEGERS - specify the type
## We create a rank 1 ndarray of floats but set the dtype to int64
x = np.array([1.5, 2.2, 3.7, 4.0, 5.9], dtype = np.int64)

## We print the dtype x
print('x = ', x)
print('The elements in x are of type:', x.dtype)

# NUMPY 2D ARRAYS
## We create a rank 2 ndarray that only contains integers
Y = np.array([[1,2,3],[4,5,6],[7,8,9], [10,11,12]])

print('Y = \n', Y)

## We print information about Y
#shape will give (row, col), where row is the number of elements in a one dimensional array
print('Y has dimensions:', Y.shape)  
print('Y has a total of', Y.size, 'elements')
print('Y is an object of type:', type(Y))
print('The elements in Y are of type:', Y.dtype)

# SAVE NUMPY ARRAY
## We save x into the current directory as 
np.save('my_array', Y)

# We load the saved array from our current directory into variable y
z = np.load('my_array.npy')

print("This is my_array.npy: \n", z)