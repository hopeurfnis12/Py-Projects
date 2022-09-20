import numpy

print("input \'n\' = ", end=' ')
n = int(input())
e = 1 / (4 * (n ** 2))

def fun_rect(j):
    s = ((j - (1 / 2)) / n) ** 2
    return s

def fun_trap(j):
    s = ((j / n) ** 2 + ((j - 1) / n) ** 2) / 2
    return s


sum_rect = 0
sum_trap = 0

for i in range(1, n + 1):
    sum_rect += fun_rect(i)
    sum_trap += fun_trap(i)

print("Rect = ", (abs((1 / 3) - sum_rect * (1 / n))))
print("Trap = ", (abs((1 / 3) - sum_trap * (1 / n))))
print("e = ", e)
