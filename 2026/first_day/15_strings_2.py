# Рассмотрим ещё некоторые способы
# работы со строками
string = 'Do re mi fa sol la si'

# Так можно разделить строку на 
# массив строк, используя пробел ' '
# как разделитель
splitted = string.split(' ')
print(splitted, type(splitted))

# Так можно ввести несколько значений в 
# одну строчку через пробел
inp_string = input()
print(inp_string.split(' '))

# И, на самом деле, строка
# это массив символов, поэтому 
# с ней можно делать аналогичные операции:
print(string[3], string[3:6], string[::-1], sep='\n')
print(len(string))
