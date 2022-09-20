import numpy as np


def Gauss(a, b):
    cout = 0
    m, n = a.shape
    if m < n:
        print("Есть пространство для решения")
    else:
        l = np.zeros((n, n))
        for i in range(n):

            if a[i][i] == 0:
                print("Нет ответа")

        for k in range(n - 1):
            for i in range(k + 1, n):
                l[i][k] = a[i][k] / a[k][k]
                cout += 1
                for j in range(m):
                    a[i][j] = a[i][j] - l[i][k] * a[k][j]
                    cout += 1
                b[i] = b[i] - l[i][k] * b[k]

        x = np.zeros(n)
        x[n - 1] = b[n - 1] / a[n - 1][n - 1]

        for i in range(n - 2, -1, -1):
            for j in range(i + 1, n):
                b[i] -= a[i][j] * x[j]
            x[i] = b[i] / a[i][i]
        for i in range(n):
            print("x" + str(i + 1) + " =", x[i])
        print("x =", x)
        print("Расчеты", "=", cout)


a = np.array([
    [0.5, 1.1, 3.1],
    [2.0, 4.5, 0.36],
    [5.0, 0.96, 6.5]
])
b = np.array([
    -6.0,
    0.020,
    0.96
])

Gauss(a, b)
