import scipy as sc
import matplotlib.pyplot as plt
import numpy as np

m = int(input('Введите m: '))
a = np.random.randint(0, 10, size=(m, m))
aT = sc.linalg.inv(a)
b = np.ones(m)
print('A = \n', a, sep = '')
print('\nОпределитель = ', sc.linalg.det(a), sep = '')
print('\nA^(T)*y = b \n', sc.linalg.solve(aT, b), sep = '')

plt.matshow(a)
plt.colorbar()
plt.title('Матрица')

plt.matshow(a)
plt.colorbar()
plt.title('Обратная матрица')

plt.show()

