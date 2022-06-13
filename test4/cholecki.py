import numpy as np

# Declaring the first array
arr1 = np.array([[4,6,1], [6,10,3], [1,3,5]])

print("Original array is :\n", arr1)

# Calculating and printing cholesky value
L = np.linalg.cholesky(arr1)
print("Cholesky value is:\n", L)

# Verifying the output

v_val = np.dot(L, L.T.conj())
print("Verified value is:\n", v_val)