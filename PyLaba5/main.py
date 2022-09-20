from math import sqrt
import numpy as np
from numpy import array

A = array([
    [6, 3, -2],
    [3, 8, 3],
    [-3, 4, 7],
])

b = array([
    [3],
    [4],
    [11]
])
m = len(A)
x = [.0 for i in range(m)]
Iteration = 0
converge = False
pogr = 0.
while not converge:
    x_new = np.copy(x)
    for i in range(m):
        s1 = sum(A[i][j] * x_new[j] for j in range(i))
        s2 = sum(A[i][j] * x[j] for j in range(i + 1, m))
        x_new[i] = (b[i] - s1 - s2) / A[i][i]
    pogr = sum(abs(x_new[i] - x[i]) for i in range(m))
    converge = pogr < 1e-6
    Iteration += 1
    x = x_new
print('Количество итераций на решение:', Iteration)
print('Решение:', x)
print('Погрешность:', pogr)
