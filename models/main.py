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


"""
Real score	Predicted score
95	92
60	55
70	70
80	81
100	99
"""
real_score = np.array([95, 60, 70, 80, 100])
predicted_score = np.array([92, 55, 70, 81, 99])
print(mean_square_error(real_score, predicted_score))

"""
Secret X	Secret Y
1	18
3	17
5	13
7	8
9	4
The resulting model is as follows:

y=-1.85x+21.25
"""


def fun(x):
    return -1.85 * x + 21.25


def error(x, y):
    return np.sum((y - fun(x)) ** 2)


X = np.array([1, 3, 5, 7, 9])
real = np.array([18, 17, 13, 8, 4])

print(error(X, real))


"""

given x and y, y = ax + b
we need to find a using least square method

X   Y
4	2
6	2
8	3
10	5
12	5

"""

X = np.array([4, 6, 8, 10, 12])
Y = np.array([2, 2, 3, 5, 5])


def get_sigma_x2(x):
    return np.sum(x ** 2)


def get_sigma_y2(x):
    return np.sum(x ** 2)


def get_sigma_xy(x, y):
    return np.sum(x * y)


def get_sigma_x(x):
    return np.sum(x)


def get_sigma_y(y):
    return np.sum(y)


def get_coefficient(X, Y):
    n = len(X)
    return (n * get_sigma_xy(X, Y) - get_sigma_x(X) * get_sigma_y(Y)) / (n * get_sigma_x2(X) - get_sigma_x(X) ** 2)


print(get_coefficient(X, Y))
