# Python3 program for implementation
# of Lagrange's Interpolation

# To represent a data point corresponding to x and y = f(x)
class Data:
	def __init__(self, x, y):
		self.x = x
		self.y = y

def interpolate(f: list, xi: int, n: int) -> float:

	# Initialize result
	result = 0.0
	for i in range(n):
		count = 1
		# Compute individual terms of above formula
		term = f[i].y
		for j in range(n):
			if j != i:
				term = term * (xi - f[j].x) / (f[i].x - f[j].x)
			count+=1

		# Add current term to result
		result += term
	print(count)
	return result

# Driver Code
if __name__ == "__main__":
	f = [Data(0.5, 0.48), Data(1, 0.84), Data(1.25, 0.95), Data(1.75, 0.98), Data(2.0, 0.91)]

	# 5 - how many xi
	print("Value of f is :", interpolate(f, 1.85, 5)) 