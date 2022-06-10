import numpy as np


a = np.array([[3,-2, -1], [-1, 2, 1], [2, -3, -4]])
b = np.array([[3,-2,-1], [-1, 2, 1], [3, -2, -1]])


a1 = np.array([[0,0,1], [0,1,0], [1,0,0]])
b1 = np.array([[-5], [-1], [5]])

A = np.array([[3,-2, -1], [-1, 2, 1], [2, -3, -4]])
B = np.array([[5], [-1], [-5]])


# print(np.dot(a1,b1))
print(np.linalg.solve(A, B))