import numpy as np

x_0 = y_0 = -1
r1 = 4
n_points = 20
time = 1
h = 0.01

a = np.array([
    [0, 0, 0],       # первая строка
    [2/3, 0, 0],     # вторая строка
    [-1/3, 1, 0]     # третья строка
])

b = np.array([1/4, 2/4, 1/4])
c = np.array([0, 2/3, 2/3])
