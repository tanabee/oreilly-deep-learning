import numpy as np

def numerical_gradient(f, x):
    h = 1e-4
    grad = np.zeros_like(x)

    for idx in range(x.size):
        tmp_val = x[idx]
        x[idx] = tmp_val + h
        fxh1 = f(x)

        x[idx] = tmp_val -h
        fxh2 = f(x)

        grad[idx] = (fxh1 - fxh2) / (2*h)
        x[idx] = tmp_val

    return grad

def function_2(x):
    return np.sum(x**2)

res01 = numerical_gradient(function_2, np.array([3.0, 4.0]))
res02 = numerical_gradient(function_2, np.array([0.0, 2.0]))
res03 = numerical_gradient(function_2, np.array([3.0, 0.0]))

print(res01)
print(res02)
print(res03)
