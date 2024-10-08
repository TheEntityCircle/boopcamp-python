# Иногда бывает удобно
# собрать несколько значений в 
# одной переменной. Для этого используют 
# массивы (list)

# Зададим массив из 4-х
# целых чисел
arr = [0, 5, 7, 9]
print(arr)
# Тип -- массив
print(type(arr))

# Получить доступ к элементу 
# массива можно вот так,
# при этом нумерация начинается с 0!
a = arr[0]
b = arr[2]
print(a, b)
print(arr[0], arr[1], arr[2], arr[3])

# В массив можно класть переменные совершенно
# разных типов, но это нужно 
# использовать аккуратно
other_arr = ['a', True, 0, 15e3, [0, 0, 0]]
print(other_arr)

# Функцией len() можно узнать количество
# сохранённых элементов в массиве
print(len(other_arr))

# Также есть функции, позволяющие
# оперировать всем массивом: 
# просуммировать все значения -- sum()
print(sum(arr))
# Найти максимальное значение -- max()
print(max(arr))
# Найти минимальное значение -- min()
print(min(arr))

# Вот такой конструкцией можно вывести
# все элементы массива и их типы
for i in range(len(other_arr)):
    print(other_arr[i], type(other_arr[i]))

# Если в теле цикла не нужен
# индекс массива i, то можно 
# обойти массив вот так:
for elem in other_arr:
    print(elem, type(elem))
    

long_arr = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13]    

start = 3
stop = 10
step = 3

# Таким образом можно получить 
# элементы массива, индексы которых лежат 
# в определённом диапазоне (шаг тоже 
# можно подбирать)
short_arr = long_arr[start:stop:step]
print(short_arr)

# Это очень похоже на range():
for i in range(start, stop, step):
    print(i, end=' ')