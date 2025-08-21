"""
Если у каждой точки на графике есть погрешность,
то используют график с крестами ошибок.
"""

import numpy as np
import pandas as pd
import matplotlib.pyplot as plt


# Счиатали наши данные из файла
data = pd.read_csv('./data_files/data.csv',
                   header=None).to_numpy()

x = data[:, 0]
y = data[:, 1]

# Абсолютная погрешность измерения x и y
x_err = 0.5
y_err = 0.75

# Построим график с крестами ошибок
plt.errorbar(x, y, xerr=x_err, yerr=y_err)
plt.show()

#%%
# Теперь попробуем его кастомизировать, глядя в документацию
# https://matplotlib.org/stable/api/_as_gen/matplotlib.pyplot.errorbar.html
plt.errorbar(x, y, xerr=x_err, yerr=y_err,
             lw=0,
             capsize=3,
             capthick=1,
             elinewidth=1.5,
             figure=plt.figure(figsize=(6,6),
                               dpi=500),
             marker='o',
             ms=6, 
             mew = 1.5)
plt.show()



