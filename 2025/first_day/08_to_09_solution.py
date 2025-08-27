# Задача:
# Ввести с клавиатуры номер года.
# Вывести, является ли он високосным, или нет.
# Как считать:
# https://ru.wikipedia.org/wiki/%D0%92%D0%B8%D1%81%D0%BE%D0%BA%D0%BE%D1%81%D0%BD%D1%8B%D0%B9_%D0%B3%D0%BE%D0%B4

year_as_str = input('Введите год: ')
year = int(year_as_str)

is_leap_year = ((year % 4 == 0 and year % 100 != 0) or year % 400 == 0)
if is_leap_year:
    print('Високосный')
else:
    print('Не високосный')