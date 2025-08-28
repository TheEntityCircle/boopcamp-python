'''
Сохраним полученную фигуру в файл
'''
import matplotlib.pyplot as plt

x = [1, 2, 3, 4]
y = [7, 12, 56, 8]

plt.plot(x, y)

# Построенный график можно сохранить вместо показа на экране
plt.savefig("test.png")
