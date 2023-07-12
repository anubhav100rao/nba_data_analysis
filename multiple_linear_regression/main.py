import numpy as np


# calculate weight w = (X^T * X)^-1 * X^T * y

def calculate_weights(X, y):
    X_transpose = np.transpose(X)
    X_transpose_dot_X = np.dot(X_transpose, X)
    X_transpose_dot_X_inverse = np.linalg.inv(X_transpose_dot_X)
    X_transpose_dot_y = np.dot(X_transpose, y)
    weights = np.dot(X_transpose_dot_X_inverse, X_transpose_dot_y)
    return weights


weights = np.array([[-1.8, 2, -4, 0.2]]).transpose()
X = np.array(
    [
        [1, 2, -3, 5],
        [1, 0.2, -3, 4],
        [1, 1, 0, 6]
    ]
)
predict = np.dot(X, weights)
print(predict.sum())


weights = np.array([[4, 0.5, 3, 0.2, -1, -4, 17]]).transpose()
X = np.array([[1, 3, 0.5, 20, 4, 0.3, 0.1]])
print(np.dot(X, weights))


y = np.array([[1, 1, 3]]).transpose()
X = np.array([
    [1, 2, 5],
    [1, 3, 5],
    [1, 4, 7]
])

print(calculate_weights(X, y))
