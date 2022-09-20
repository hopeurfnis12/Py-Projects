import math
import copy


a = [
    [6, 3, -2],
    [3, 8, 3],
    [-3, 4, 7]
]

b = [3, 4, 11]


def isCorrectArray(a):
    for row in range(0, len(a)):
        if len(a[row]) != len(b):
            print('Не соответствует размерность')
            return False

    for row in range(0, len(a)):
        if a[row][row] == 0:
            print('Нулевые элементы на главной диагонали')
            return False
    return True


def isNeedToComplete(x_old, x_new):
    eps = 0.0001
    sum_up = 0
    sum_low = 0
    for k in range(0, len(x_old)):
        sum_up += (x_new[k] - x_old[k]) ** 2
        sum_low += (x_new[k]) ** 2

    return math.sqrt(sum_up / sum_low) < eps


def solution(a, b):
    if not isCorrectArray(a):
        print('Ошибка в исходных данных')
    else:
        count = len(b)

        x = [1 for k in range(0, count)]

        numberOfIter = 0
        MAX_ITER = 100
        while numberOfIter < MAX_ITER:

            x_prev = copy.deepcopy(x)

            for k in range(0, count):
                S = 0
                for j in range(0, count):
                    if j != k: S = S + a[k][j] * x[j]
                x[k] = b[k] / a[k][k] - S / a[k][k]

            if isNeedToComplete(x_prev, x):
                break

            numberOfIter += 1

        print('Количество итераций на решение:', numberOfIter)

        return x


print('Решение:', solution(a, b))
