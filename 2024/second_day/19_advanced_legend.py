"""
Рассмотрим кастомизацию легенды графика
"""

import numpy as np
import pandas as pd
import matplotlib.pyplot as plt


# Счиатали наши данные из файла
data = pd.read_csv('./data_files/data.csv', header=None).to_numpy()

x = data[:, 0]
y = data[:, 1]
y2 = data[:, 2]

# Относительная ошибка измерения x и y
rel_error = 0.05

x_err = x * rel_error
y_err = y * rel_error

plt.figure(dpi=300)
# Чтобы на легенде правильно отбразился кусок линии,
# которому соответствует какое-то название,
# стиль линии нужно получить вот так:
normal_line = plt.plot(x, y2)

# Построим легенду для одного графика
# Почему первые два аргумента -- массивы
# смотрите ниже
plt.legend([normal_line[0]], # Стиль линии для корректного отображения в окошке легенды
           ["График номер 1"], # Соответствующее той линии название
           loc=0, # Положение легенды (0 -- выбирается автоматически), число от 0 до 10 включительно
           title='Название легенды') 

plt.show()

#%%

# Или для двух графиков
plt.figure(dpi=300)
err_line = plt.errorbar(x, y, xerr=x_err, yerr=y_err, fmt='o')
normal_line = plt.plot(x, y2)

plt.legend([err_line, normal_line[0]], # у err_line не нужно брать первый элемент для отображения
            [f"График номер {np.max(y2)/ 3.3: .2f}", 
            "Другая линия"], 
            loc=5) # 5 -- означает справа посередине, подробнее: https://matplotlib.org/stable/api/_as_gen/matplotlib.pyplot.legend.html

plt.show()



