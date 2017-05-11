import numpy as np

def soft_max(a):
    c = np.max(a)
    exp_a = np.exp(a - c)
    sum_exp_a = np.sum(exp_a)
    y = exp_a / sum_exp_a

    return y

y = soft_max(np.array([0.3, 2.9, 4.0]))

print(y)
print(np.sum(y))
