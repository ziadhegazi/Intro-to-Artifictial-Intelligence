# Write a NumPy program to compute the covariance matrix of two given arrays.
# Original array1: [0 1 2]
# Original array2: [2 1 0]
# Covariance matrix of the said arrays: [[ 1. -1.] [-1. 1.]]

import numpy as np

array1 = np.array([0, 1, 2])
array2 = np.array([2, 1, 0])

covar = np.cov(array1, array2, bias= True)
covar2 = np.cov(array1, array2)

print("Co-varaince with bias set to True: ", covar)
print("Co-varaince with bias set to False: ", covar2)