import numpy as np
import matplotlib.pyplot as plt
import scipy.optimize as optimize


def res(p, y, x):
    a, b, c = p
    err = y - a * np.exp(b * x)
    return err


n = 10    #int(input('Введеите n: '))
h = 1 / n
x = []
y = []
for i in range(n):
    x.append(i * h)
    y.append(x[i] + np.cos(2 * x[i]))

a, b, c = 2, 1, 3
np.random.seed(0)
y0 = y + 0.1 * np.random.randn(len(x))

plt.plot(x, y, '-', label='exact')
#plt.plot(x, y0, '.', label='perturbation')
p0 = [0, 0, 0]
plsq = optimize.leastsq(res, p0, args = (y0, x))
p1 = plsq[0]
print('a, b, c:', p1)
y1 = p1[0] + p1[1] * np.exp(-p1[2] * x)
plt.plot(x, y1, '--', label = 'solution')
plt.legend(loc = 0)
plt.xlabel('x')
plt.ylabel('f(x)')
plt.grid(True)
plt.show()
