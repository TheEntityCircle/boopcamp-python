"""
pandas -- огромная библиотека, но нам пока что
потребуется только несколько функций для чтения файлов.
"""

import numpy as np
import pandas as pd
import matplotlib.pyplot as plt


# Вместо считывания файла руками воспользуемся готовой функцией
data = pd.read_csv('./data_files/data.csv')

print(data) # Результат немного не такой, как хотелось бы

#%%

data_correct = pd.read_csv('./data_files/data.csv',
                           header=None)
print(data_correct) # А вот так результат правильный
print(type(data_correct)) # Какая-то странная сущность

#%%
np_data = data_correct.to_numpy()
print(np_data) # Конвертировали в уже знакомый numpy массив
print(type(np_data))


#%%

excel_data = pd.read_excel('./data_files/data.xlsx',
                  header=None).to_numpy()
print(excel_data) # Аналогичную операцию проделали с данными в .xlsx файле

#%%

# Попробуем считать файл с отвратительной разметкой,
# data = pd.read_csv('./data_files/really_bad.csv') # ошибка
data = pd.read_csv('./data_files/really_bad.csv', skiprows=10)
print(data) # Хотя бы считалось, но внутри каша
#%%

# Посмотрим докуменацию: https://pandas.pydata.org/pandas-docs/stable/reference/api/pandas.read_csv.html
# И узнаем, какие аргументы по ключевому слову нам доступны
data = pd.read_csv('./data_files/really_bad.csv',
                   skiprows=10,
                   decimal=',',
                   sep='\t').to_numpy()
print(data) # Победа

plt.plot(data[:, 0], data[:, 1])



