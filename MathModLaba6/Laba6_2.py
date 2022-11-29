import numpy as np
import matplotlib.pyplot as plt
import scipy.optimize as optimize


x = -0.8
y = -0.6
e = 0.001
n = 100
X = 0.
Y = 0.
Dx = 0.
Dy = 0.
for i in range(1,n):
    F = np.sin(y)+2*x-2
    G = np.cos(x-1)+y-0.7
    Fx = 2.0
    Fy = np.cos(y)
    Gx = -np.sin(x-1)
    Gy = 1.0
    D = Fx*Gy-Gx*Fy
    dx1 = G*Fy
    Dx = (G*Fy-F*Gy)/D
    Dy = (F*Gx-G*Fx)/D
    xk = x + Dx
    yk = y + Dy
    if((abs(xk-x)<e) and (abs(yk-y)<e)):
        X = xk
        Y = yk
    x = xk
    y = yk
print("x, y:", X,Y)


def func(x):
    return [np.sin(x[1])+2*x[0]-2,
            np.cos(x[0]-1)+x[1]-0.7]
print("Optimize fsolve:", optimize.fsolve(func,[-1,-0.5]))