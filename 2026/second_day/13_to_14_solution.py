# Задача: считать из любого excel файла из папки
# funny_plots данные, построить по ним график
import pandas as pd
import matplotlib.pyplot as plt


d = pd.read_excel('creature6.xlsx', header=None).to_numpy()
plt.plot(d[:, 0], d[:, 1], 'o')
