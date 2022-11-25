from scipy.linalg import lu
import numpy as np
import matplotlib.pyplot as plt
from numpy.linalg import qr
from numpy.linalg import cholesky
from numpy import linalg as LA
from scipy.linalg import lu, lu_factor, lu_solve

n = int(input())


a = np.zeros((n,n), int)
a[range(n),range(n)]=2
a[range(n-1),range(1,n)]=-1
a[range(1,n),range(n-1)]=-1


b = np.zeros(n)
b[n-1] = -1
b[0] = 1

print(b)

#LU decomposition
P, L, U = lu(a)

print(P)
print(L)
print(U)

#QR decomposition

Q, R = qr(a, 'complete')
print(Q)
print(R)

k = 0
p = 0
# Cholesky decomposition

m=0
w, v = np.linalg.eig(a)
for i in range(len(w)):
    if (w[i]<0):
        m = 1
        break
if(m == 0):
    L = cholesky(a)
    print(L)
else:
    print("собственных значения матриы отриательное")

#Решение

LU, p = lu_factor(a)
x = lu_solve((LU, p), b.T)
print(x)

y1 = LA.solve(Q,b.T)
x1 = LA.solve(R,y1)
print(x1)