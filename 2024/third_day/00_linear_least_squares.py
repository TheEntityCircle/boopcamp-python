# Написать в отдельном файле функцию, 
# реализующую аппроксимацию прямой 
# Методом Наименьших Квадратов 
# (Формулы находятся в файлах 
# МНК1.png и МНК2.png)

import numpy as np

def lin_ls(x, y):
    xy = np.mean(x * y)
    x1y = np.mean(x) * np.mean(y)
    x2 = np.mean(x * x)
    x12 = np.mean(x) ** 2
    y2 = np.mean(y * y)
    y12 = np.mean(y) ** 2
    k = (xy - x1y) / (x2 - x12)
    b = np.mean(y) - k * np.mean(x)
    s_k = np.sqrt(1 / x.size) * np.sqrt((y2 - y12) / (x2 - x12) - k ** 2)
    s_b = s_k * np.sqrt(x2 - x12)
    return k, s_k, b, s_b
