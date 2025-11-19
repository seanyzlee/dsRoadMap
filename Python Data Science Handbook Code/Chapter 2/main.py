import numpy as np
print(np.__version__)

# Creating Arrays from Python Lists
arr1 = np.array([1, 4, 2, 5, 3])

# Nested lists results in multi-dimensional arrays
arr2 = np.array([range(i,i+3) for i in [2,4,6] ])

print("Array 1: ", arr1)
print("Array 2: ", arr2)

# Create a length-10 integer array filled with zeros
arr_zeros = np.zeros(10, dtype=int)
print("Array of zeros: ", arr_zeros)
# Create a 3x5 floating-point array filled with ones
arr_ones = np.ones((3,5), dtype=float)
print("Array of ones: \n", arr_ones)

# Create an array filled with a linear sequence
arr_seq = np.arange(0, 20, 2)
print("Array with linear sequence: ", arr_seq)

# Create an array of five values evenly spaced between 0 and 1
arr_linspace = np.linspace(0, 1, 5)
print("Array with linspace: ", arr_linspace)

