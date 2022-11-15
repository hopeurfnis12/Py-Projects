import numpy as np
import sympy as sy
from sympy import *
xs = symbols('x')

def F(x):
    match v:
        case '0': return x ** 3 + x - 1
        case 'a': return x ** 3 - 2 * x + 2
        case 'b': return np.sin(x) + x - 1 
        case 'c': return np.log(x) - 1 / x


def diff(x):
    match v:
        case '0': return float(sympify(sy.diff(xs ** 3 + xs - 1, xs)).subs(xs, x))
        case 'a': return float(sympify(sy.diff(xs ** 3 - 2 * xs + 2, xs)).subs(xs, x))
        case 'b': return np.cos(x) + 1
        case 'c': return 1 / x + 1 / x ** 2


def difff(x):
    match v:
        case '0': return float(sympify(sy.diff(xs ** 3 + xs - 1, xs, xs)).subs(xs, x))
        case 'a': return float(sympify(sy.diff(xs ** 3 - 2 * xs + 2, xs, xs)).subs(xs, x))
        case 'b': return -np.sin(x)
        case 'c': return -(1 / x ** 2) - 2 / x ** 3

def task1():
    i = 0
    a = a0
    b = b0
    while True:
        print(i)
        print("|b - a| =", np.abs(b - a))
        if np.abs(b - a) < 0.01: break

        x0 = (a + b) / 2

        Fa = F(a)
        print("F(a):", Fa)

        Fx0 = F(x0)
        print("F(x0):", Fx0)

        Fb = F(b)
        print("F(b):", Fb)

        if(Fa * Fx0 < 0): b = x0
        else: a = x0

        print("x(", i, "): ",  x0, sep = "")
        i = i + 1

        print()


def task2():
    i = 1
    
    if F(a0) * difff(a0) > 0: x0 = a0
    else: x0 = b0
    
    while True:
        if i == 1:
            x1 = x0 - F(x0)/diff(x0)
            x2 = x1 - F(x1)/diff(x1)
        else:
            x1 = x2
            x2 = x1 - F(x1)/diff(x1)

        xz = np.abs(x2 - x1)
        if xz < 0.01:
            print("|x(", x2, ") - x(", x1, ")| = ", xz, sep="")
            break
        i = i+1


def task3():
    return 0


v = '0'
match v:
    case '0':
        a0 = 0
        b0 = 1
    case 'a':
        a0 = -2
        b0 = -1
    case 'b':
        a0 = 0
        b0 = 1
    case 'c':
        a0 = 1
        b0 = 2

task2()