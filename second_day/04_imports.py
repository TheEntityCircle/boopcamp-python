"""
Знакомимся с пакетами
"""

#%%
# Например, мы хотим узнать сколько сейчас времени.
# За нас кто-то уже написал функцию, которая это делает.
# Давайте теперь её используем.
import time
print(time.gmtime())


#%%
# Но нам нужна только одна функция, 
# давайте импортируем только её
from time import gmtime
print(gmtime())


#%%
# Если нас не устраивает название функции
# или пакета, то можно их переименовать:  
import time as custom_name
print(custom_name.gmtime())

from time import gmtime as func
print(func())

#%%
# Можно использовать и собственноручно написанный
# код из соседнего файла other_file.py
from other_file import read_result

read_result()






