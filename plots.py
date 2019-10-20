import matplotlib.pyplot as plt


n = 4
data = [(x, x**2, x**x) for x in range(n)]

x = [x[0] for x in data]
y = [x[1] for x in data]
print(x)
print(y)
plt.plot(x, y)
plt.show()
plt.plot(data)
plt.show()
