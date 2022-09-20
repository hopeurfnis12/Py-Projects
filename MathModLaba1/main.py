import scipy as sp
import numpy as np

# 1.
def task1():
    print('#1#')
    print("A =\n", np.zeros((2, 3)), end = "\n\n")

    print("B =\n", np.eye(3), end = "\n\n")

    print("C =\n", np.ones((2, 2)), end = "\n\n")

    D = np.array([
        [1, 0, 0, 0],
        [3, 1, 0, 0],
        [3, 1, 4, 0],
        [1, 2, 4, 3],
    ])
    print("D =\n", D, end = "\n\n")

    F = np.array([
        [1, 2, 3],
        [7, 1, 8],
    ])
    print("F =\n", F, end = "\n\n")

    G = np.array([
        [1, 5, 0, 0],
        [5, 2, 4, 0],
        [0, 4, 1, 1],
        [0, 0, 1, 3],
    ])
    print("G =\n", G, end = "\n\n")

# 2.
def task2():
    print('#2#')
    arr = np.linspace(1.0, 10.0, 10)
    print(arr)
    print("a =\n", np.resize(arr, (2, 5)), end = "\n\n")

    b = np.resize(arr, 9)
    print("b =", b, "\n", np.resize(b, (3, 3)), end = "\n\n")

    c = np.resize(arr, (5, 2))
    c[-1] = 1.0
    print("c =\n", c, end = "\n\n")

# 3.
def summat(matrixA, matrixB):
    if len(matrixA) == len(matrixB) and len(matrixA[0]) == len(matrixB[0]):
        print("A + B =\n", matrixA + matrixB, end = "\n\n")
    else:
        print('Невозможно найти сумму\n')


def umnozhmat(matrixA, matrixB, alpha):
    print("A *", alpha, "=\n", matrixA.dot(alpha), end = "\n\n")
    print("B *", alpha, "=\n", matrixB.dot(alpha), end = "\n\n")


def proizmat(matrixA, matrixB):
    if len(matrixA) == len(matrixB[0]) and len(matrixA[0]) == len(matrixB):
        print("A * B =\n", matrixA.dot(matrixB), end = "\n\n")
        print("B * A =\n", matrixB.dot(matrixA), end = "\n\n")
    else:
        print('Невозможно вычислить произведения AB и BA\n')


def task3():
    print('#3#')
    print('a)')
    aAm = np.array([
        [0, 1, 3],
        [1, 5, 6],
    ])

    aBm = np.array([
        [1, 2, 3],
        [0, 1, 3],
    ])

    print('A =\n', aAm, end = '\n\n')
    print('B =\n', aBm, end = '\n\n')
    summat(aAm, aBm)
    umnozhmat(aAm, aBm, 5)
    proizmat(aAm, aBm)


    print('b)')
    bAm = np.array([
        [1, 3, 2],
        [8, 0, 3],
    ])

    bBm = np.array([
        [1, 0, 0],
        [3, 1, 0],
        [0, 2, 4],
    ])

    print('A =\n', aAm, end = '\n\n')
    print('B =\n', aBm, end = '\n\n')
    summat(bAm, bBm)
    umnozhmat(bAm, bBm, 2)
    proizmat(bAm, bBm)


    print('c)')
    cAm = np.array([
        [0, 0, 1],
        [0, 1, 0],
        [1, 0, 0],
    ])

    cBm = np.array([
        [0, 2, -3],
        [-2, 0, 6],
        [3, -6, 0],
    ])

    print('A =\n', aAm, end = '\n\n')
    print('B =\n', aBm, end = '\n\n')
    summat(cAm, cBm)
    umnozhmat(cAm, cBm, 4)
    proizmat(cAm, cBm)


    print('d)')
    dAm = np.array([
        [1, 3+2j],
        [3-2j, 5],
    ])

    dBm = np.array([
        [3, 2, 1],
        [7, 1, 4],
    ])

    print('A =\n', dAm, end = '\n\n')
    print('B =\n', dBm, end = '\n\n')
    summat(dAm, dBm)
    umnozhmat(dAm, dBm, -2)
    proizmat(dAm, dBm)


# 4.
def soprmat(matrixD, matrixC):
    conjD = (matrixD.transpose()).conjugate()
    conjC = (matrixC.transpose()).conjugate()
    print("Сопряженная D =", conjD, "\nСопряженная C =", conjC, sep = '\n', end = '\n\n')


def obrmat(matrixD, matrixC):
    if len(matrixD) == len(matrixD[0]):
        print("Обратная D =\n", np.linalg.inv(matrixD), end = "\n\n")
    if len(matrixC) == len(matrixC[0]):
        print("Обратная C =\n", np.linalg.inv(matrixC), end = "\n\n")

def task4():
    print("#4#")
    print('a)')
    aDm = np.array([
        [1+1j, 3, 2],
        [8, -5j, 3-2j],
    ])

    aCm = np.array([
        [1, 0, 0],
        [3, 1, 0],
        [0, 2, 4],
    ])

    print('D =\n', aDm, end = '\n\n')
    print('C =\n', aCm, end = '\n\n')
    soprmat(aDm, aCm)
    obrmat(aDm, aCm)


    print('b)')
    bDm = np.array([
        [3, 2],
        [2, 3],
    ])

    bCm = np.array([
        [3, 9+1j, 2],
        [1j, 7, 1],
        [0, 0, 1],
    ])

    print('D =\n', bDm, end = '\n\n')
    print('C =\n', bCm, end = '\n\n')
    soprmat(bDm, bCm)
    obrmat(bDm, bCm)


    print('c)')
    cDm = np.array([
        [2+1j, 1, 0, 0],
        [1, 2-1j, 0, 0],
        [0, 0, 1+1j, 1],
        [0, 0, 1, 1-1j],
    ])

    cCm = np.array([
        [3, 0, 0, 1],
        [5, 7, 0, 0],
        [4, 3, 1, 1],
    ])

    print('D =\n', cDm, end = '\n\n')
    print('C =\n', cCm, end = '\n\n')
    soprmat(cDm, cCm)
    obrmat(cDm, cCm)


# 5.
def task5():
    print('#5#')
    print('a)')
    Am = np.array([
        [9, 2, 3, 5],
        [3, 1, 3, 5],
        [3, 1, 4, 2],
        [1, 2, 4, 3],
    ])
    print('A =', Am, sep = '\n', end = '\n\n')
    print('Определитель A =', np.linalg.det(Am), sep = '\n', end = '\n\n')
    znA, vecA = np.linalg.eig(Am)
    radA = np.abs(np.linalg.eigvals(Am))
    print('Собсвтвенные значения = ', znA, '\nСобственные векторы = ', vecA, '\nСпектральный радиус = ', max(radA),
          sep = '\n', end = '\n\n')
    print()

    print('b)')
    Bm = np.array([
        [14, 2, 2, 5],
        [8, 1, 8, 0],
        [3, 4, 4, 3],
        [6, 2, 4, 2],
    ])
    print('A =', Bm, sep = '\n', end = '\n\n')
    print('Определитель A =', np.linalg.det(Bm), sep = '\n', end = '\n\n')
    znB, vecB = np.linalg.eig(Bm)
    radB = np.abs(np.linalg.eigvals(Bm))
    print('Собсвтвенные значения = ', znB, '\nСобственные векторы = ', vecB, '\nСпектральный радиус = ', max(radB),
          sep = '\n', end = '\n\n')


# Start
print('Чтобы остановить программу, напишите \'0\'')
while True:
    task = input('Выберите задание: ')
    if task == '1':
        task1()
    elif task == '2':
        task2()
    elif task == '3':
        task3()
    elif task == '4':
        task4()
    elif task == '5':
        task5()
    elif task == '0':
        break
    else:
        print('Нет такого задания')
