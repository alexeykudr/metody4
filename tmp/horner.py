res = 0
n = float(input("Enter max ^"))
x = float(input("Enter x0"))
while n > 0:
    coef = float(input("Enter coefs on x"))
    res += coef
    res *= x
    n -= 1

    
coef = float(input("Enter free coef."))
res += coef
print(res)