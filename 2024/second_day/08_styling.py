"""
Попробуем поиграться с оформлением графиков
"""
import matplotlib.pyplot as plt

x = []
for i in range(100):
    x.append(2 * i / 100)

y1, y2, y3 = [], [], []
for i in x:
    y1.append(i)
    y2.append(i**2)
    y3.append(i**3)


# # Немного поэкспериментируем со стилями самих графиков
plt.plot(x, y1, label='linear',
          marker='o', linestyle='-',
          color='red', linewidth=2,
          ms=3)
plt.plot(x, y2, label='quadratic',
          marker='v', linestyle='--',
          color='green', linewidth=1,
          ms=3)
plt.plot(x, y3, label='cubic', marker='^',
          linestyle='-.', color='black',
          linewidth=1,
          ms=3)

# Все возможные варианты стилей можно найти на сайте с
# документацией к matplotlib:
# Маркеры: https://matplotlib.org/stable/api/markers_api.html
# Цвета: https://matplotlib.org/stable/users/explain/colors/colors.html
# Стили линий: https://matplotlib.org/stable/gallery/lines_bars_and_markers/linestyles.html

# Альтернатива: третьим аргументом передаём 
# строку с нужным форматированием цвета, линии и маркера
# plt.plot(x, y3, 'k^-.',
#          label='cubic', linewidth=1)

plt.legend()

plt.show()







