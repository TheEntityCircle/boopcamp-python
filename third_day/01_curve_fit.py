"""
scipy -- тоже огромная библиотека, но нам
опять понадобится только одна функция:
попробуем аппроксимировать экспериментальные
данные заданной функцией.
"""

from scipy.optimize import curve_fit

import numpy as np
import matplotlib.pyplot as plt


# Зададим функцию, которая должна приближать
# экспериментальные данные
def func(x, a, b):
    return a * x ** 2 + np.sin(3*x) - b

# Количество рассматриваемых точек
N = 50

# Параметры функции
A = 2.5
B = 3

x = np.linspace(0, 2, N)
y = func(x, A, B)

# Синтезируем экспериментальные данные,
# добавив к точкам графика случайный шум

# Амплитуда шума
n_amp = 0.1

x_exp = x + n_amp * (np.random.random(N) - 0.5)
y_exp = y + n_amp * (np.random.random(N) - 0.5)


# Пробуем подобрать коэффициенты a и b, чтобы
# аппроксимировать шумные данные
coefs, pcov = curve_fit(func, x_exp, y_exp)

# Погрешность определения каждого коэффициента
coef_error = np.sqrt(np.diag(pcov))

print(coefs, coef_error)

plt.figure(dpi=200)
plt.plot(x, y, lw=4.0)
plt.plot(x_exp, y_exp, 'rv', ms=3)

plt.plot(x, func(x, coefs[0], coefs[1]), 'm-.', lw=1.5)
plt.show()

