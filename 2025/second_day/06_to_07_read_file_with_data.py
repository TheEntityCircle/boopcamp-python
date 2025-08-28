# Задача:
# Считать из любого файла из папки plot_files
# координаты точек (х, у) и построить по ним график


# Решение:
x = []
y = []

with open('./plot_files/file_1.txt', 'r') as f:
    for line in f:
        s = line.split(sep=' ')
        x.append(float(s[0]))
        y.append(float(s[1]))

import matplotlib.pyplot as plt

plt.plot(x, y)
plt.show()
