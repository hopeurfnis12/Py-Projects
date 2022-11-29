import numpy as np
import matplotlib.pyplot as plt


def f(x, y):
    #return x**2 + y
    return x * y


def task1():
    k = 0
    x = 0
    y = 1

    print("k, x, y")
    while x < b:
        px1.append(x)
        py1.append(y)

        y = y + h * f(x, y)
        x = round(x + h, 1)
        k = k + 1
        print(k, ": ", x, " | ", y, sep='')


def task2():
    k = 0
    x = 0
    y0 = 1
 
    print("k, x, y^, y")
    while x < b:
        px2.append(x)
        py2.append(y0)

        y = y0 + h * f(x, y0)
        y0 = y0 + (h / 2) * (f(x, y0) + f(x+h, y)) 
        x = round(x + h, 1)
        k = k + 1
        print(k, ": ", x, " | ", y, " | ", y0, sep='')


def task3():
    k = 0
    x = 0
    y = 1
    
    print("k, x, k0, k1, k2, k3, y")
    while x < b:
        px3.append(x)
        py3.append(y)

        k0 = h*f(x, y)
        k1 = h*f(x + h/2, y + k0/2)
        k2 = h*f(x + h/2, y + k1/2)
        k3 = h*f(x + h, y + k2)
        y = y + (k0 + 2*k1 + 2*k2 + k3)/6

        x = round(x + h, 1)
        k = k + 1
        print(k, ": ", x, " | ", k0, " | ", k1, " | ", k2, " | ", k3, " | ", y, sep='')


def task4():
    k = 0
    x = 0
    y = 1

    print("k, x, y")
    while x < b:
        px4.append(x)
        py4.append(np.exp((x**2)/2))
        
        y = np.exp((x**2)/2)
        x = round(x + h, 1)
        k = k + 1
        print(k, ": ", x, " | ", y, sep='')


h = 0.1
b = 1
px1 = []
py1 = []
px2 = []
py2 = []
px3 = []
py3 = []
px4 = []
py4 = []

task1()
task2()
task3()
task4()
plt.plot(px1, py1, 'b--', label = 'Эйлера')
plt.plot(px2, py2, 'r*', label = 'Мод. Эйлера')
plt.plot(px3, py3, 'g-', label = 'Рунге')
plt.plot(px4, py4, 'c.', label = 'Точность')
plt.legend(loc = 0)
plt.grid(True)
plt.show()