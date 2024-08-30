"""
Рассмотрим более сложный случай
"""

from scipy.optimize import curve_fit

import numpy as np
import matplotlib.pyplot as plt


# Теперь функция будет немного хитрее
def func(x, a, b, c):
    return (-np.sign(x) * a * (-1e-5) * np.log(np.abs(70*x)) 
            + b / 100 * np.cos(c / 1000 * x))

# Количество рассматриваемых точек
N = 120

# Параметры функции
A = -5e4
B = -400
C = 2000

real_coefs = np.array([A, B, C])

x = np.linspace(-2, 2, N)
y = func(x, A, B, C)


# Амплитуда шума теперь выше
n_amp = 0.3

x_exp = x + n_amp * (np.random.random(N) - 0.5)
y_exp = y + n_amp * (np.random.random(N) - 0.5)


# Пробуем аппроксимировать

# Так получаются совсем неправильные значения
coefs, pcov = curve_fit(func, x_exp, y_exp)


# Но обычно мы можем каким-то образом
# оценить диапазон значений параметров
bounds = ((-9e4, -1_000, 1_000),
          (-1e4, -100.0, 4_000))
# или их приближённые значения
p0 = np.array([-3.94e4, -267, 2200])

# Тогда можно использовать эти дополнительные
# данные для подбора коэффициентов
# (можно использовать или диапазон, 
# или приближённые значения, одновременно не
# получится)
# coefs, pcov = curve_fit(func, x_exp, y_exp, 
#                         bounds=bounds)

# или
# coefs, pcov = curve_fit(func, x_exp, y_exp, 
#                         p0=p0)

# Погрешность определения каждого коэффициента
coef_error = np.sqrt(np.diag(pcov))


# Обрежем точность выводимых на экран чисел
# до 2-х знаков после запятой
np.set_printoptions(precision=2)
print('Истинные значения: ', real_coefs)
print('Подобранные значения:', coefs)
print('Оценка абс. погрешности:', coef_error)

# Выведем также относительную 
# погрешность относительно реальных коэффициентов
print('Реальная отн. погрешность, %: ',
      (coefs - real_coefs) / real_coefs * 100)

plt.figure(dpi=200)
plt.plot(x, y, lw=4.0)
plt.plot(x_exp, y_exp, 'rv', ms=3)

plt.plot(x, func(x, coefs[0], coefs[1], coefs[2]), 'm-.', lw=1.5)
plt.show()

