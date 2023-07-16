import numpy as np


"""
advanatages of MAPE:
1. Scale independent

"""


def mean_absolute_percentage_error(y_true, y_pred):
    return min(100, np.mean(np.abs((y_true - y_pred) / y_true)) * 100)


def symmetric_mean_absolute_percentage_error(y_true, y_pred):
    return min(100, np.mean(np.abs((y_true - y_pred) / ((np.abs(y_true) + np.abs(y_pred))))) * 100)


def symmetric_mean_absolute_percentage_error2(y_true, y_pred):
    return min(100, np.mean(np.abs((y_true - y_pred) / ((np.abs(y_true) + np.abs(y_pred)) / 2))) * 100)


print(mean_absolute_percentage_error(np.array([90]), np.array([70])))
print(mean_absolute_percentage_error(np.array([70]), np.array([90])))


print(symmetric_mean_absolute_percentage_error(
    np.array([100]), np.array([85])))
print(symmetric_mean_absolute_percentage_error(
    np.array([100]), np.array([115])))
