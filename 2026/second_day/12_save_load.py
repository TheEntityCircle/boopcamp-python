"""
numpy массивы можно удобно сохранять на диск,
а потом загружать
"""
import numpy as np
import matplotlib.pyplot as plt

x = np.linspace(0, 100, 100)
y = np.sin(x)

np.save('x.npy', x)
np.save('y.npy', y)

#%%
a = np.load('x.npy')
b = np.load('y.npy')

plt.plot(a, b)
plt.show()
