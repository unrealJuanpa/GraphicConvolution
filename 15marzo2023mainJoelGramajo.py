import numpy as np
import matplotlib.pyplot as plt

# Joel Gramajo 202008025
#              array        , index in array of pointer
x1 = np.array([-1, 2, 0, 1]), 3
h1 = np.array([2, 1, 2, 3, 1]), 1

x2 = np.array([-5, 2, -1, 0]), 1
h2 = np.array([1, 3, 1, 2, 4]), 3

x3 = np.array([-10, 1, 1, 1, 0, 1, 1, 1]), 0
h3 = np.array([-1, 3, 4, 2, -3, 2, 2, 1]), 7


def myConv(data1, data2):
    res = np.convolve(data1[0], data2[0])
    idxa = data1[1]+data2[1]
    n = np.arange(start=-idxa, stop=data1[0].size+data2[0].size-1-idxa)
    return n, res

plt.subplot(3, 3, 1)
plt.stem(x1[0])
plt.subplot(3, 3, 2)
plt.stem(h1[0])
plt.subplot(3, 3, 3)
plt.stem(*myConv(x1, h1))

plt.subplot(3, 3, 4)
plt.stem(x2[0])
plt.subplot(3, 3, 5)
plt.stem(h2[0])
plt.subplot(3, 3, 6)
plt.stem(*myConv(x2, h2))

plt.subplot(3, 3, 7)
plt.stem(x3[0])
plt.subplot(3, 3, 8)
plt.stem(h3[0])
plt.subplot(3, 3, 9)
plt.stem(*myConv(x3, h3))

plt.show()