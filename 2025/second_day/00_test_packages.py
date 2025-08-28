import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
import scipy


df = pd.DataFrame([[1, 2], [2, 3]])

arr = df.to_numpy()

b1 = arr.size == 4
b2 = np.sum(arr) == 8

arr2 = scipy.linalg.inv(arr)
b3 = np.isclose(np.sum(np.diag(arr2)), -4.0)
plt.figure(dpi=200)

if b1 and b2 and b3:
    plt.text(0.4, 0.4, 'ALL OK!')
    print('OK!')
    plt.show()
else:
    plt.text(0.3, 0.4, 'SMTH WENT WRONG!')
    print('NOT OK!')
    plt.show()