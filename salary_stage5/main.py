import numpy as np
from sklearn.metrics import mean_absolute_percentage_error
import os
import requests

import pandas as pd
from sklearn.linear_model import LinearRegression
from sklearn.model_selection import train_test_split
from sklearn.metrics import mean_absolute_percentage_error

# checking ../Data directory presence
if not os.path.exists('../Data'):
    os.mkdir('../Data')

# download data if it is unavailable
if 'data.csv' not in os.listdir('../Data'):
    url = "https://www.dropbox.com/s/3cml50uv7zm46ly/data.csv?dl=1"
    r = requests.get(url, allow_redirects=True)
    open('../Data/data.csv', 'wb').write(r.content)

# read data
df = pd.read_csv('../Data/data.csv')

# write your code here

y = df['salary']
df.drop(['salary'], axis=1, inplace=True)
# drop headers from df
X = df.values


def training_variable_dimension(dimension=1):
    X_train, X_test, y_train, y_test = train_test_split(
        X, y, test_size=0.3, random_state=100)

    model = LinearRegression()
    model.fit(X_train, y_train)

    predictions = model.predict(X_test)
    mape = mean_absolute_percentage_error(y_test, predictions)
    return mape


"""
ans = 10000000

for i in range(1, 6):
    ans = min(ans, training_variable_dimension(i))

print(ans)

# best result for dimension = 3
"""

# print(training_variable_dimension(1))
# coefficients = training_variable_dimension(1)
# # print ", " sepated coeficients
# print(*coefficients, sep=', ')


def get_mape_after_dropping_columns_handle_negative_with_zero(columnsToDrop, dimension=1):
    new_df = df.drop(columnsToDrop, axis=1)
    X = new_df.values
    X_train, X_test, y_train, y_test = train_test_split(
        X, y, test_size=0.3, random_state=100)

    X_train = np.power(X_train, dimension)
    X_test = np.power(X_test, dimension)

    model = LinearRegression()
    model.fit(X_train, y_train)

    predictions = model.predict(X_test)
    # replace all negative predictions with 0
    predictions[predictions < 0] = 0
    mape = mean_absolute_percentage_error(y_test, predictions)
    return mape


def get_mape_after_dropping_columns_handle_negative_with_median(columnsToDrop, dimension=1):
    new_df = df.drop(columnsToDrop, axis=1)
    X = new_df.values
    X_train, X_test, y_train, y_test = train_test_split(
        X, y, test_size=0.3, random_state=100)

    X_train = np.power(X_train, dimension)
    X_test = np.power(X_test, dimension)

    model = LinearRegression()
    model.fit(X_train, y_train)

    predictions = model.predict(X_test)
    # replace all negative predictions with median
    predictions[predictions < 0] = np.median(y)
    mape = mean_absolute_percentage_error(y_test, predictions)
    return mape


def get_mape_after_dropping_columns_handle_negative(columnsToDrop):
    new_df = df.drop(columnsToDrop, axis=1)
    X = new_df.values
    X_train, X_test, y_train, y_test = train_test_split(
        X, y, test_size=0.3, random_state=100)

    X_train = np.power(X_train, dimension)
    X_test = np.power(X_test, dimension)

    model = LinearRegression()
    model.fit(X_train, y_train)

    predictions = model.predict(X_test)

    # try all possible ways to handle negative predictions
    # either replace them with 0 or with median
    median = np.median(y)

    mape = mean_absolute_percentage_error(y_test, predictions)
    return mape


combinations = [
    ['age', 'experience']
]
ans = 100000000

for combination in combinations:
    ans = min(ans, min(get_mape_after_dropping_columns_handle_negative_with_zero(
        combination), get_mape_after_dropping_columns_handle_negative_with_median(combination)))

    print(ans)
print(np.round(ans, 5))
