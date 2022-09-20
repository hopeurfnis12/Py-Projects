# Встроенная функция
def fun(x):
    return x ** 3
def symps(a, b, n):
    h = (b-a)/n
    x = a
    s = fun(x)-fun(b)
    for k in range(1, n+1):
        x = x+h/2
        s = s+4*fun(x)
        x = x+h/2
        s = s+2*fun(x)
    result = (h / 6) * s
    return result
a = 0
b = 0
n = 9
p = symps(a, b, n)
print(p)
