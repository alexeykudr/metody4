import numpy as np

# eliminacja gaussa z przestawianiem

# det(A) = det(L) * det(U) (iloczyn przekontnych) 
# liczba kroków n-1, n to wiersze
# powstaja 2 macierze L i U; L - trojkatna dolna (1 na przekatnej, pod mnozniki); U - trojkatna gorna (macierz koncowa)

# liczba x-sow
n = 4

a = np.array([[1,0,2,1, 2],
            [4,-9,2,1, 14],
            [8,16,6,5, -3],
             [2,3,2,1, 0]], dtype=float)

print("Początkowa:\n")
print(a)
print()

x = np.zeros(n)


for i in range(n-1):
    for j in range(i+1, n):
            
        if np.abs(a[j,i]) > np.abs(a[i,i]):
            a[[j,i]]=a[[i,j]]
            print("Element główny {}".format(a[i,:]))
            #macierz jednostkowa, tam gdzie zmieniaja sie wiersze, jedynka sa na pozycji jedynki z rzedu z ktorym sie zamienia
            print("Byla potrzeba zamiany wierszy\n")
            print(a)
            print()
            
        print("Element główny {}\n".format(a[i,:]))

    
    for j in range(i+1, n):
        ratio = a[j][i]/a[i][i]
        if np.isnan(ratio) == True or np.isinf(ratio) == True:
            ratio = 0.0
        print("Krok {}\n".format(i + 1))
        print("Mnożnik {}\n".format(ratio))
        for k in range(n+1):
            a[j][k] = a[j][k] - ratio * a[i][k]
        print(a)
        print()
        
x[n-1] = a[n-1][n]/a[n-1][n-1]

for i in range(n-2,-1,-1):
    x[i] = a[i][n]
    for j in range(i+1,n):
        x[i] = x[i] - a[i][j]*x[j]
    x[i] = x[i]/a[i][i]

print('Rozwiazanie')
for i in range(n):
    print(i + 1,x[i])