import matplotlib.pyplot as plt
import numpy as np
from mpl_toolkits.mplot3d import Axes3D


def task1():
    x = np.array([1, 2, 5, 6, 8])
    y = np.array([1, 4, -6, 0, -4])
    plt.plot(x, y, '-.r*', label = 'График 1', linewidth=2)

    x2 = np.array([1, 3, 6, 7])
    y2 = np.array([0, 5, -5, 3])
    plt.plot(x2, y2, ':cv', label = 'График 2', linewidth=4)

    plt.title('ЗаГоЛоВоК')
    plt.xlabel("Ось X")
    plt.ylabel("Ось Y")
    plt.legend()
    plt.show()


def task2():
    x = [1, 5, 10, 15, 20]
    y1 = [1, 7, 3, 5, 11]
    y2 = [i * 1.2 + 1 for i in y1]
    y3 = [i * 1.2 + 1 for i in y2]
    y4 = [i * 1.2 + 1 for i in y3]
    # Настройка размеров подложки
    plt.figure(figsize = (12, 7))
    # Вывод графиков
    plt.subplot(2, 2, 1)
    plt.plot(x, y1, '-r', label = 'Граф 1')
    plt.title('TITLE1')
    plt.legend()
    plt.xlabel("Ось X 1")
    plt.ylabel("Ось Y 1")

    plt.subplot(2, 2, 2)
    plt.plot(x, y2, '--g', label = 'Граф 2')
    plt.title('TITLE2')
    plt.legend()
    plt.xlabel("Ось X 2")
    plt.ylabel("Ось Y 2")

    plt.subplot(2, 2, 3)
    plt.plot(x, y3, '-.b', label = 'Граф 3')
    plt.title('TITLE3')
    plt.legend()
    plt.xlabel("Ось X 3")
    plt.ylabel("Ось Y 3")

    plt.subplot(2, 2, 4)
    plt.plot(x, y4, ':c', label = 'Граф 4')
    plt.title('TITLE4')
    plt.legend()
    plt.xlabel("Ось X 4")
    plt.ylabel("Ось Y 4")

    plt.show()


def task3():
    fig = plt.figure()
    ax_3d = Axes3D(fig)
    x = np.linspace(0, 10, 50)
    y = np.linspace(0, 50, 50)
    X, Y = np.meshgrid(x, y)
    z = np.cos(X) - np.sin(Y)
    ax_3d.contourf(X, Y, z, 15)

    plt.show()


task3()