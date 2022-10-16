import scipy as sc
import matplotlib.pyplot as plt
import numpy as np

m = 4
a = np.random.randint(0, 10, size=(m, m))
A = sc.linalg.inv(a)
b = np.ones(m)
print('A = \n', a, sep = '')
print('\nОпределитель = ', sc.linalg.det(a), sep = '')
print('\nA^(-1)* b \n', np.dot(A, b), sep = '')
print('\nA*y = b \n', sc.linalg.solve(a, b), sep = '')
plt.matshow(a)
plt.title('Матрица')
plt.matshow(a)
plt.title('Обратная матрица')

plt.show()

