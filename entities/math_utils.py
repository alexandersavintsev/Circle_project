import numpy as np

def func_x(t, x):
    return -np.exp(t) * x

def func_y(t, y):
    return np.exp(t) * y

def runge_method(x_0, h, n, func, a, b, c):
    x_t = []
    x_t.append(x_0)
    t = 1e-10

    for i in range(n):
        x_n = x_t[i]
        k1 = func(t, x_n)
        k2 = func(t + c[1] * h, x_n + a[1, 0] * h * k1)
        k3 = func(t + c[2] * h, x_n + a[2, 0] * h * k1 + a[2, 1] * h * k2)
        x_t.append(x_n + h * (k1 * b[0] + k2 * b[1] + k3 * b[2]))
        t += h

    return x_t
