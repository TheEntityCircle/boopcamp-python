# Также распространённым контейнером
# является словарь (dict). В нём хранятся
# данные в формате `ключ`--`значение`

# Таким образом задаётся словарь:
# слева от двоеточия стоит ключ, справа
# значение
d = {'item_1': 42.0, 'my_item': 15}
print(d)
print(type(d))

# По ключу можно получить значение 
# элемента словаря
a = d['item_1']
b = d['my_item']
print(a, b)

# В качестве ключа может выступать
# не только строка:
d2 = {'r2': 500, 3: 15, 'po': -1}
print(d2)
print(d2[3])