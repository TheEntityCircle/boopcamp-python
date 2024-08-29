'''
Теперь пробуем по-разному писать в файл
'''
# Небольшое повторение функций
def read_result():
    with open('new.txt', 'r') as file:
        print(file.read())

#%%
# Запишем всю информацию разом, 'w' значит,
# что файл открыт на запись
with open('new.txt', 'w') as file:
    file.write('Single_line')
    
# Посмотрим, что получилось
read_result()
    
#%%
# А теперь две строчки разом
s = 'First' + '\n' + 'Second'

with open('new.txt', 'w') as file:
    file.write(s)

read_result()

#%%
# Наконец, построчно сколько захотим
n = 10

with open('new.txt', 'w') as file:
    for i in range(n):
        file.write('b' + 'r' * i + '\n')
    
read_result()








