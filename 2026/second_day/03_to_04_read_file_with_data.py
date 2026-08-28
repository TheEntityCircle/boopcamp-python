x = []
y = []

with open('./plot_files/file_with_data.txt', 'r') as f:
    for line in f:
        s = line.rstrip().split(sep=' ')
        x.append(float(s[0]))
        y.append(float(s[1]))

import matplotlib.pyplot as plt

plt.plot(x, y)
plt.show()