import numpy as np
import matplotlib.pyplot as plt
from scipy.integrate import solve_ivp


def f(x, a1, a2, a3, a4):
    v, w = x
    return np.array([(a1 - a2 * w) * v, (-a3 + a4 * v) * w])

def solve(vw, a1, a2, a3, a4):
    v0 = []
    w0 = []

    for i in t:
        v0.append(vw[0])
        w0.append(vw[1])

        k0 = h * f(vw, a1, a2, a3, a4)
        k1 = h * f(vw + k0/2, a1, a2, a3, a4)
        k2 = h * f(vw + k1/2, a1, a2, a3, a4)
        k3 = h * f(vw + k2, a1, a2, a3, a4)
        vw = vw + (k0 + 2*k1 + 2*k2 + k3)/6

        # print(round(i, 1), ": ", vw[0], " | ", vw[1], sep='')
    return v0, w0

# vw = np.array([1., 1.])
# a1 = 1.5    # rabbit birth rate
# a2 = 0.5    # rabbit hunted rate
# a3 = 2      # foxes death rate
# a4 = 0.2    # foxes birth rate

h = 0.1
b = 30
t = np.arange(0, b, h)

v1, w1 = solve([1,1], 1.5, 0.5, 2, 0.2)
v2, w2 = solve([1,1], 1, 1, 1, 0.5)
v3, w3 = solve([2,2], 1.5, 0.5, 2, 0.2)

plt.plot(t, v1, 'r-', label = 'v1')
plt.plot(t, w1, 'c-', label = 'w1')

plt.plot(t, v2, 'b--', label = 'v2')
plt.plot(t, w2, 'k--', label = 'w2')

plt.plot(t, v3, 'y:', label = 'v3')
plt.plot(t, w3, 'g:', label = 'w3')


plt.legend(loc = 0)
plt.grid(True)
plt.show()