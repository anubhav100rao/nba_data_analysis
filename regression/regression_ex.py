from sklearn.datasets import load_diabetes
from sklearn.linear_model import LinearRegression
from sklearn.metrics import mean_squared_error
import numpy as np

diabetes = load_diabetes()

X = diabetes.data
y = diabetes.target

# leave last 50 rows for testing
X_train, X_test = X[:-50], X[-50:]
Y_train, Y_test = y[:-50], y[-50:]

model = LinearRegression()
model.fit(X_train, Y_train)

predictions = model.predict(X_test)
mse = mean_squared_error(Y_test, predictions)
print(mse, np.ceil(mse))
