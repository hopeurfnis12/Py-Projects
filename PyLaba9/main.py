import math
from math import sin
import numpy as np
import matplotlib.pyplot as plt

def lagranz(x, y, t):
    z = 0
    for i in range(len(y)):
        p = 1
        for j in range(len(x)):
            if i != j:
                p *= (t - x[j])/(x[i] - x[j])
        z += p * y[i]
    return z


x = np.array([], dtype=np.float_)
y = np.array([], dtype=np.float_)

for i in np.arange(0, math.pi, math.pi/2):
    x = np.append(x, round(i, 2))
    y = np.append(y, round(sin(i), 2))
x = np.append(x, round(math.pi, 2))
y = np.append(y, round(sin(math.pi), 2))

xnew = np.linspace(x.min(), x.max(), 5)
ynew = [lagranz(x, y, i) for i in xnew]
plt.plot(x, y, 'o', xnew, ynew)
plt.grid(True)
plt.show()
