"""
Вообще-то кастомизировать в графике можно всё, что угодно
"""

import numpy as np
import pandas as pd
import matplotlib.pyplot as plt


data = pd.read_csv('./data_files/data.csv', header=None).to_numpy()

x = data[:, 0]
y = data[:, 1]
y2 = data[:, 2]

rel_error = 0.05

x_err = x * rel_error
y_err = y * rel_error

plt.figure(dpi=300)
err_line = plt.errorbar(x, y, xerr=x_err, yerr=y_err, fmt='o')
normal_line = plt.plot(x, y2)

plt.legend([err_line, normal_line[0]],
            [f"График номер {np.max(y2)/ 3.3: .2f}", 
            "Другая линия"], loc=5)
# До этого места всё как в прошлых файлах

# С помощью функции plt.rc() мы будем менять самые разные параметры
# графика. Все возможные настраиваемые параметры перечислены в документации:
# https://matplotlib.org/stable/api/matplotlib_configuration_api.html#matplotlib.rcParams
# на этой странице можно найти длинный список параметров. 

# Задаём некоторые параметры таким образом
plt.rc('axes', linewidth=2.0) # Толщина линий осей
plt.rc('xtick.major', width=2.0) # Тощина насечек по Ох
plt.rc('xtick.minor', width=0) # Отключаем побочные насечки по Ох
plt.rc('xtick', direction='in') # Направляем насечки по Ох внутрь графика
plt.rc('axes', labelsize=20) # Высота шрифта на названии осей
plt.rc('ytick.major', width=2.0) # Аналогично
plt.rc('ytick.minor', width=0)
plt.rc('ytick', direction='in')
plt.rc('xtick', labelsize=18) # Высота шрифта цифр масштаба
plt.rc('ytick', labelsize=18)
plt.rc('xtick.major', pad=10) # Отступ между осью и цифрами
plt.rc('ytick.major', pad=10)
plt.rc('legend', fontsize=4) # Размер шрифта легенды
plt.show()