import numpy as np
import matplotlib.pyplot as plt
import scipy.optimize as optimize


def res(p, N, t):
    a, b = p
    err = N - a * np.exp(b * t)
    return err


n = 10    #int(input('Введеите n: '))
t = np.array([0, 1, 3, 5])
N = np.array([110, 120, 135, 148])

plt.plot(t, N, '-', label='exact')

p0 = [0, 0]
plsq = optimize.leastsq(res, p0, args = (N, t))
p1 = plsq[0]

print('a, b:', p1)
N1 = p1[0] * np.exp(p1[1] * t)
N2 = p1[0] * np.exp(p1[1] * 7)
print('t[7] =', N2)

plt.plot(t, N1, '--', label = 'solution')
plt.plot(7, N2, '*', label = 't[7]')

plt.legend(loc = 0)
plt.xlabel('t')
plt.ylabel('f(t)')
plt.grid(True)
plt.show()
