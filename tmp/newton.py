import matplotlib.pyplot as plt

def get_divided_difference(x_values:list, y_values:list, k:int) -> int:
    result = 0
#     trzeba na k tez , range oddaje k-1 , wiec k + 1
    for j in range(k + 1):
        product = 1
        for i in range(k + 1):
            if i != j:
                product *= x_values[j] - x_values[i]
        result += y_values[j] / product
    print(result)
    return result


def generate_Newton_interpolation(x_values, y_values):
    div_diff = []
    for i in range(1, len(x_values)):
        div_diff.append(get_divided_difference(x_values, y_values, i))
        
    def calc_Newton(x):
        result = y_values[0]
        for k in range(1, len(y_values)):
            product = 1
            for j in range(k):
                product *= (x - x_values[j])
            result += div_diff[k-1] * product
        
        return result
    return calc_Newton


x_test = [0,2,3,4,6]
y_test = [1,3,2,5,7]



n = generate_Newton_interpolation(x_test, y_test)

aproximate = []

for i in x_test:
    aproximate.append(n(i))


plt.plot(aproximate, color= 'r')