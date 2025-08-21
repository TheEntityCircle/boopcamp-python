"""
Посмотрим разные функции над массивами.
"""
#%%
import numpy as np

a = np.linspace(0, 10, 7)

# Различные статистики массива
print(a)
print("min:", np.min(a))
print("max:", np.max(a))
print("sum:", np.sum(a))
print("mean:", np.mean(a))

#%%
# Теперь математические функции

import matplotlib.pyplot as plt

plt.figure(dpi=800)

x = np.linspace(-10, 10, 1000)

y = np.sqrt(x)
y = x ** -1
y = np.exp(x)
y = np.log(x)
y = np.sin(x)
y = np.sin(np.pi * x)
y = np.arctan(x)
y = np.cosh(x)
y = np.abs(x)

# Своя непрерывная функция
def g(x):
    return 1.5 * x ** 2 \
        + np.sin(np.pi * x) * x
        
y = g(x)

# Своя разрывная функция
def f(x):
    if x < 1:
        return -20
    else:
        return x**2

# y = f(x) # Выдаст ошибку!

vec_f = np.vectorize(f) # Функции могут быть аргументами других функций, да
y = vec_f(x) # Правильно сработает


plt.plot(x, g(x), 'v') # Смотрим, что получается
plt.plot(x, y, 'o') # Смотрим, что получается
plt.show()


#%%
# Округления
x = 2.5
# x = np.linspace(0, 1, 8)
print(x)
print(np.floor(x))
print(np.round(x))
print(np.ceil(x))







