import numpy as np
import sympy as sy
from sympy import *
y1 = symbols('y1')
y2 = symbols('y2')
y3 = symbols('y3')
y4 = symbols('y4')


# def f1(y, )

# return float(sympify(sy.diff(xs ** 3 - 2 * xs + 2, xs)).subs(xs, x))
def task1():
    # y** - x * y* + 2y = x + 1
    # y(0.9) - 0.5*y*(0.9) = 2
    # y(1.2) = 1
    x = np.arange(0.9, 1.2 + h, h)
    for i in x:
        return 0



eps = 10 ** -3
h = 0.1
task1()