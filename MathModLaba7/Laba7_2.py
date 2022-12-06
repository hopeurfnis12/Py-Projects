import numpy as np
import matplotlib.pyplot as plt
from scipy.integrate import solve_ivp


def f(x):
    v, w = x
    return np.array([(a1 - a2 * w) * v, (-a3 + a4 * v) * w])


vw = np.array([1., 1.])
a1 = 1.5    # rabbit birth rate
a2 = 0.5    # rabbit hunted rate
a3 = 2      # foxes death rate
a4 = 0.2    # foxes birth rate
h = 0.1
b = 30
t = np.arange(0, b, h)
v0 = []
w0 = []

for i in t:
    v0.append(vw[0])
    w0.append(vw[1])

    k0 = h * f(vw)
    k1 = h * f(vw + k0/2)
    k2 = h * f(vw + k1/2)
    k3 = h * f(vw + k2)
    vw = vw + (k0 + 2*k1 + 2*k2 + k3)/6

    # print(round(i, 1), ": ", vw[0], " | ", vw[1], sep='')


def fun(t, z):
    v, w = z
    return [(a1 - a2 * w) * v, (-a3 + a4 * v) * w]

sol = solve_ivp(fun, [0, b], [1, 1], dense_output=True)
z = sol.sol(t)

plt.plot(t, v0, 'r-', label = 'v')
plt.plot(t, w0, 'c--', label = 'w')

plt.plot(t, z[0].T, 'bo', label = 'v: sol_ivp')
plt.plot(t, z[1].T, 'k.', label = 'w: sol_ivp')

plt.legend(loc = 0)
plt.grid(True)
plt.show()