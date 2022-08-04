# Write a NumPy program to convert a NumPy array into a Python list structure.
# Expected output:
# Original array elements: [[0 1] [2 3] [4 5]]
# Array to list: [[0, 1], [2, 3], [4, 5]]

import numpy as np

arr = np.array([[0, 1], [2, 3], [4, 5]])

list = arr.tolist()
print ("Array: ", arr)
print ("list: ", list)