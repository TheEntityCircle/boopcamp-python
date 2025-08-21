'''
Здесь просто определена функция из кусочка про
запись в файл.
'''
def read_result():
    with open('new.txt', 'r') as file:
        print(file.read())
