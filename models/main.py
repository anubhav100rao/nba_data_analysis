import numpy as np


def mean_square_error(real, predict):
    return np.mean((real - predict) ** 2)


def predict(X1, X2, coefficients):
    return coefficients[0] + coefficients[1] * X1 + coefficients[2] * X2


functions = np.array([
    [0, 2, 3],
    [0, 3, 2],
    [-0.5, 2, 3],
    [0.5, 2, 3]
])

real = np.array([1.5, 1, 0, -0.5, 9])
X1 = np.array([-2, -1, 0, 1, 2])
X2 = np.array([2, 1, 0, -1, 2])


for coefficients in functions:
    print(mean_square_error(real, predict(X1, X2, coefficients)))
