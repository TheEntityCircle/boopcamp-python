"""
Теперь немного поработаем с осями графика
"""

import numpy as np
import pandas as pd
import matplotlib.pyplot as plt


data = pd.read_csv('./data_files/data.csv', header=None).to_numpy()

x = data[:, 0] * 1e5
y = data[:, 1] * 1e5

rel_error = 0.05

x_err = x * rel_error
y_err = y * rel_error

plt.figure(dpi=400)
plt.errorbar(x, y, xerr=x_err, yerr=y_err)

#%%

# Масштаб в научном стиле без массы нулей с помощью отбражения степеней 10
plt.ticklabel_format(style='sci', # Здесь попробуйте убрать часть аргемнтов и
                      axis='both', # посмотреть, как меняется результат
                     scilimits=(0,0),
                     useMathText=True)

# Включаем мелкие деления
plt.minorticks_on()

# Включаем сетку
plt.grid(visible=True,
         which='major',
         linestyle='-',
         linewidth=1.5,
         color='0.7') # Формат основных линиий сетки
plt.grid(visible=True,
         which='minor',
         linestyle='--',
         linewidth=1,
         color='0.8') # Формат побочных линий, 
# цвет указывается как оттенок серого - 0.0 - чёрный, 1.0 - белый

plt.xlim([np.min(x), np.max(x)]) # Пределы по оси х
plt.ylim([np.min(y), np.max(y)]) # Пределы по оси y

# Альтернативный вариант:
# plt.xlim([np.min(x), np.max(x)*1.05])
# plt.ylim([np.min(y), np.max(y)*1.05])

# Зачем здесь значки долларов
# мы узнаем на третьем дне буткемпа
plt.xlabel(r"$ m$") # Название оси х
plt.ylabel(r"$ r^2 $, кг$^2$") # Название оси y

plt.show()



