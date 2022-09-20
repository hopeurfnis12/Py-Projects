a = 0
b = 1
w = 4
e = 8

def trapez(a, b, N):
    H = (b - a) / N
    s = f(a) + f(b)
    for i in range(1, N):
        x = (a + i * H)
        s += (2 * f(x))
    s = s * H / 2
    return s

def f(x):
    return x ** 3

def summ(a, b, N):
    H = (b-a)/N
    s = 0
    for i in range(0,N):
        s += H * f(a + i * H + H / 2)
    return s


k2n = [0] * 3
kI = [0] * 3
for i in range(0, 3):
    k2n[i] = abs((trapez(a, b, e) - trapez(a, b, w)))
    k2n[i] = k2n[i] / 3
    kI[i] = abs((1 / 5) - trapez(a, b, e))
print(k2n)
print(kI)
print(trapez(0, 1, 4))
