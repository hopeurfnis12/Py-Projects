import numpy as np
import sympy as sy
from sympy import *
import matplotlib.pyplot as plt
ys = [symbols('y1'), symbols('y2'), symbols('y3'), symbols('y4')]


def diff_y(k):
    match k:
        case 0: return (ys[k+1] - ys[k])/h
        case 3: return (ys[k] - ys[k-1])/h
        case _: return (ys[k+1] - ys[k-1])/(2*h)

def diff_yy(k): return (ys[k+1] - (2 * ys[k]) + ys[k-1])/(h * h)

def task1_1():
    y.append(ys[0] - 0.5 * diff_y(0))
    b.append(2)
    for i in range(1, 3):
        y.append(diff_yy(i) - x[i] * diff_y(i) + 2 * ys[i])
        b.append(x[i] + 1)
    y.append(ys[3])
    b.append(1)
    for i in range(4):
        print(i+1, ': ', y[i], " = ", b[i], sep='')


def progon_u(a, b, c, u): return -c / (a*u + b)
def progon_v(a, b, d, u, v): return (d - a*v) / (a*u + b)

def task1_2(d):
    a = [0, 105, 105.5, 0]
    b = [6, -198, -198, 1]
    c = [-5, 95, 94.5, 0]
    u.append(-c[0]/b[0])
    v.append(d[0]/b[0])
    for i in range(1, 4):
        u.append(progon_u(a[i], b[i], c[i], u[i-1]))
        v.append(progon_v(a[i], b[i], d[i], u[i-1], v[i-1]))
    print('\nU:', u)
    print('V:', v)


def task1_3():
    y0 = []
    y0.append(v[3])
    for i in range(2, -1, -1):
        y0.append(u[i] * y0[2 - i] + v[i])
    print('\nx | y')
    for i in range(4):
        print(x[i], '|', y0[3 - i])
    print()
    for i in range(4):    
        print('y', i+1, ': ', solve_y(y[i], y0[3], y0[2], y0[1], y0[0]), sep='')
    # plt.plot(x, y0, 'r-')
    # plt.plot(x, y0, 'b.')
    # plt.xlabel('x')
    # plt.ylabel('y')
    # plt.grid()
    # plt.show()


def solve_y(y, x0, x1, x2, x3):
    # print(y)
    return float(sympify(y).subs([(ys[0], x0), (ys[1], x1), (ys[2], x2), (ys[3], x3)]))

eps = 10 ** -3
h = 0.1
x = [0.9, 1.0, 1.1, 1.2]
y = []
b = []
u = []
v = []

task1_1()
task1_2(b)
task1_3()