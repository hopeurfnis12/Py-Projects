from scipy.linalg import lu
import numpy as np
import matplotlib.pyplot as plt
from numpy.linalg import qr
from numpy.linalg import cholesky
from numpy import linalg as LA

a = np.array([[7, 1, 1, 0],
              [1, 5, 2, 1],
              [2, 3, -3, 3],
              [3, 4, 5, 5]])

b = np.array([[7, 0, -1, -2]])

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


y = LA.solve(L,b.T)
x = LA.solve(U, y)
print(x)

y1 = LA.solve(Q,b.T)
x1 = LA.solve(R,y1)
print(x1)


