"""
Базовая работа с файлами может быть устроена
примерно так
"""
#%%
# Откроем test.txt на чтение ('r' от 'read')
file = open("text.txt", 'r')

# Прочитаем весь файл разом в одну строку,
# тут же выведем её на экран
# read() возвращает строку str, это ВАЖНО помнить,
# если вы собираетесь считывать числа из файла вручную.
print(file.read())

# Закроем файл
file.close()

# Этот пример, конечно, не очень хорош - мы
# почему-то считаем, что файл точно откроется.
# А если он не откроется, то этот код некрасиво упадёт.

#%%
# Более красиво написать так:
with open("text.txt", 'r',
          encoding='utf8') as f:
    print(f.read())



# Это такой типовой блок:
# with ... as ...:
#     ...
# Мы пытаемся захватить ресурс 
# (открыть файл в данном случае)
# и выполняем тело блока только в том случае, если захватить ресурс удалось.
# В конце блока ресурс освободится (в данном случае файл закроется).


#%%
# Можно считать построчно:
with open('text.txt', 'r') as f:
    for line in f:
        print(line, end='')
        print('Мы считали строчку файла.')









