'''
Попробуем всё немного усложнить
'''
import matplotlib.pyplot as plt

# Зададим X
x = []
for i in range(100):
    x.append(2 * i / 100)


# А это -- три штуки y(x)
y1, y2, y3 = [], [], []
for i in x:
    y1.append(i)
    y2.append(i**2)
    y3.append(i**3)


# Построим графики, указав названия
plt.plot(x, y1, label='linear')
plt.plot(x, y2, label='quadratic')
plt.plot(x, y3, label='cubic')

# Подпишем оси
plt.xlabel('x label')
plt.ylabel('y label')
# И график целиком
plt.title("Simple Plot")
# И легенду нарисуем, чтобы было ясно, кто есть кто
plt.legend()

plt.show()



