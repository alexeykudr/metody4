# metoda gaussa seidela

import numpy as np

eps = 10**-11

A = np.array([[2,1,-1],
             [2,3,-1],
             [-3,2,5]], dtype=float)

B = np.array([[2],
             [4],
             [4]], dtype=float)

x = np.zeros(len(B))
# print(len(B))


D = np.tril(np.triu(A))
L = np.tril(A,-1)
U = np.triu(A,1)

first = np.matmul(np.linalg.inv(L + D), -1*U)
second = np.matmul(np.linalg.inv(L + D) , B)

number_iteration = 1

while True:
    print("{} iteracja\n".format(number_iteration))
    number_iteration = number_iteration + 1
    
    y = np.matmul(first,x) + second.reshape(len(B),)
    print("x{} -> {} (wektor)".format(number_iteration - 1,y))
    
    norm = np.linalg.norm(y - x)
    print("Norma = {}\n".format(norm))
    
    r = np.linalg.norm(B.reshape(len(B),) - np.matmul(A,y))
    print("Promien {}\n".format(r))
    
    x = y
    
    if np.linalg.norm(r) < eps:
        break