from scipy.linalg import lu
import numpy as np
import matplotlib.pyplot as plt
from numpy.linalg import qr
from numpy.linalg import cholesky
from numpy import linalg as LA
from scipy.linalg import lu, lu_factor, lu_solve


a = np.array([[4,-6,0,8,0,0],
[-6,8,-12,0,16,0],
[0,-12,16,0,0,10],
[8,0,0,20,-8,0],
[0,16,0,-8,24,-8],
[0,0,10,0,-8,28]])

b = np.array([[24,54,84,48,72,158]])

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
print(x.T)

y1 = LA.solve(Q,b.T)
x1 = LA.solve(R,y1)
print(x1.T)





