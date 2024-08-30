'''
Начинаем знакомство с numpy -- умными массивами.
'''
#%%
# Пусть у нас есть массив с числами
# и мы хотим к каждому числу прибавить единичку
x = [1, 2, 4, 5, 6, 7, 9]
print(x)

for i in range(len(x)):
    x[i] += 1
print(x)

#%%
# Для решения такой проблемы и ещё
# тысячи похожих и непохожих был создан numpy
import numpy as np

x = [1.5, 2.0, 3.0]
a = np.array(x) # Создадим numpy массив из имеемого
print(a)

a = a + 1
print(a)

a += 1
print(a)

#%%
# Массивы многут быть и многомерными:

b = np.array([[1, 2, 3], [2, 3, 4]])
print(b)

# Всего элементов
print(b.size)
# Форма массива
print(b.shape)

#%%
# В этих массивах нужно всегда иметь
# в виду с каким типом данных мы работаем
a = np.array([[1, 2, 3], [2, 3, 4]])

print(a)
print(a.dtype)

# a = np.array([[1,2,3],[4,5,6]], dtype=np.float64)
a = np.array([[1., 2, 3],[4,5,6]])

print(a)
print(a.dtype)




