import numpy as np
import matplotlib.pyplot as plt

# 1 ---------------------------------------------------------------------------
# Нарисовать график любой непрерывной
# придуманной функции.
x = np.linspace(-2, 2, 1000)

def f(x):
    return np.sin(x) * np.log(np.abs(x))

y = f(x)
plt.plot(x, y)

plt.show()
# 1 ---------------------------------------------------------------------------

# 2 ---------------------------------------------------------------------------
# Нарисовать график любой разрывной
# (с условием в теле функции) придуманной 
# функции.
x = np.linspace(-2, 2, 1000)

def g(x):
    if np.abs(x) < 0.5:
        return x
    return np.sin(x) * np.log(np.abs(x))

h = np.vectorize(g)

y = h(x)
plt.plot(x, y)

plt.show()
# 2 ---------------------------------------------------------------------------

# 3 ---------------------------------------------------------------------------
# Нарисовать окружность x**2 + y**2 = 1
x = np.linspace(-1, 1, 1000)

y1 = np.sqrt(1 - x**2)
y2 = -y1

plt.plot(x, y1)
plt.plot(x, y2)

plt.show()
# 3 ---------------------------------------------------------------------------
