import numpy as np

A = np.array([[2, -3, -4],
              [-1, 2, 1],
              [3, -2, -1]], dtype='float32')
B = np.array([[-5, -1, 5 ]], dtype='float32').T
n=len(A)-1
print(n)
for n in range(1,len(A)):
    for i in range(n,len(A)):
        l=A[i][n-1]/A[n-1][n-1]
        print("Mnoznik:",l)
        B[i] = B[i] - B[n-1] * l
        for j in range(0,len(A[1])):
            A[i][j]=A[i][j]-A[n-1][j]*l
        print(A)
        print(B)
suma = 0
n=len(A)
x=np.zeros(n, dtype='float32')
x[n-1] = B[n-1] / A[n-1][n-1]

for i in range(n-2, -1, -1):
    suma = B[i]
    for j in range(i+1, n):
        suma = suma - A[i][j]*x[j]
    x[i] = suma / A[i][i]
print(x)