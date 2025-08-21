'''
Попробуем срезы массивов
'''
#%%
import numpy as np

a = np.array([[1., 2, 3], [2, 3, 4]])

print(a)
print("Dims:", a.ndim)
print("Shape:", a.shape)

#%%
a = np.array([[1., 2, 3], [5, 6, 7]])
b = np.array([3.0, 2.0, 1.0])

print(b)
print("Dims:", b.ndim)
print("Shape:", b.shape)

# Сначала номер строки, потом номер столбца
print(f'{a=}')
print(a[0, 2])
print("Slice 1: ", a[:, 0])
print("Slice 2: ", a[1, :])
print("Slice n: ", a[:, :])

print("Slice 3: ", b[1:])
print("Slice 4: ", b[1::-1])
print("Slice 5: ", b[:-1])

x = np.array([1, 2, 3, 4, 0, 5, 6, 7])
print(x[::3])







