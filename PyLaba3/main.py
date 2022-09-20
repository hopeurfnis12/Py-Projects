import numpy as np
import cmath as cm


a = np.array([
    [4, 1, 2, 0.5, 2, 7],
    [1, 0.5, 0, 0, 0, 3],
    [2, 0, 3, 0, 0, 7],
    [0.5, 0, 0, 0.625, 0, -4],
    [2, 0, 0, 0, 16, -4]
])
n = len(a)
b = np.zeros(a.shape, dtype = complex)
b[0] = a[0] / cm.sqrt(a[0][0])
for i in range(1, n):
    b[i][i] = cm.sqrt(a[i][i] - (b[:, i] ** 2).sum())
    b[i, i + 1:] = (a[i, i + 1:] - (b[:i, i].reshape(-1, 1) * b[:i, i + 1:]).sum(0)) / b[i][i]
y = b[:, n].reshape(-1, 1)
b = b[:, :n]
x = np.zeros((n, 1), dtype = complex)
for i in range(1, n + 1):
    x[-i, 0] = (y[-i] - (b[-i, -i:] * x[-i:, 0]).sum()) / b[-i, -i]
for i in range(1, n+1):
    print("x", i, " = ", x[i - 1][0].real, sep= '')
