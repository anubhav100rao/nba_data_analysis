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

X = df['rating']
y = df['salary']


def training_variable_dimension(dimension):
    X_train, X_test, y_train, y_test = train_test_split(
        X, y, test_size=0.3, random_state=100)

    X_train = np.array(X_train).reshape(-1, 1)
    X_test = np.array(X_test).reshape(-1, 1)

    X_train = np.power(X_train, dimension)
    X_test = np.power(X_test, dimension)

    model = LinearRegression()
    model.fit(X_train, y_train)

    predictions = model.predict(X_test)

    mape = mean_absolute_percentage_error(y_test, predictions)

    return np.round(mape, 5)


ans = 10000000

for i in range(1, 6):
    ans = min(ans, training_variable_dimension(i))

print(ans)
