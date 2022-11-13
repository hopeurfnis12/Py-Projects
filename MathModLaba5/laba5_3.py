import matplotlib.pyplot as plt
import numpy as np
import scipy.optimize as optimize


def res(p, N, t):
    a, b = p
    err = N - a * np.exp(b * t)
    return err


n = 10    #int(input('Введеите n: '))
t = np.linspace(0., 1., n, endpoint = False)
N = 110 + t * 10 + 5 
N0 = N + 0.1 * np.random.randn(len(t))

plt.plot(t, N, '-', label='exact')
plt.plot(t, N0, '.', label='perturbation')

p0 = [0, 0]
plsq = optimize.leastsq(res, p0, args = (N0, t))
p1 = plsq[0]

print('a, b:', p1)
y1 = p1[0] * np.exp(p1[1] * t)

plt.plot(t, y1, '--', label = 'solution')
plt.legend(loc = 0)
plt.xlabel('t')
plt.ylabel('f(t)')
plt.grid(True)
plt.show()
