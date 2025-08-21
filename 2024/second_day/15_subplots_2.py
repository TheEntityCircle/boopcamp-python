'''
После знакомства с двумерными массивами
попробуем сделать сетку из графиков
'''
import matplotlib.pyplot as plt

x = []
for i in range(100):
    x.append(2 * i / 100)

y1, y2, y3 = [], [], []
for i in x:
    y1.append(i)
    y2.append(i**2)
    y3.append(i**3)

# А теперь создадим изображение,
# на котором будет сразу несколько 
# строк и столбцов
fig, axs = plt.subplots(nrows=2, ncols=2)
# Теперь в axs - двумерный массив "осей", в которых мы построим свои y(x) по отдельности
axs[0][0].plot(x, y1, label='linear')
axs[1][0].plot(x, y2, label='quadratic')
axs[1][1].plot(x, y3, label='cubic')

# Всё изображение целиком тоже подпишем
fig.suptitle("Several subplots", size=18)

plt.show()







