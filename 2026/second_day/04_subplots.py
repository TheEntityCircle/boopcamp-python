'''
Строим сразу несколько графиков на одном экране
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

# А теперь создадим одно изображение, на котором будет несколько графиков
fig, axs = plt.subplots(nrows=1, ncols=3)
# Теперь в axs - набор "осей", в которых мы построим свои y(x) по отдельности
axs[0].plot(x, y1, label='linear')
axs[1].plot(x, y2, label='quadratic')
axs[2].plot(x, y3, label='cubic')

# Можно при желании перебирать оси в цикле, иногда это удобно
for ax in axs:
    ax.set_xlabel('x label')
    ax.set_ylabel('y label')
    ax.legend()
    ax.set_title("Smth")

# Всё изображение целиком тоже подпишем
fig.suptitle("Several subplots", size=18)

plt.show()