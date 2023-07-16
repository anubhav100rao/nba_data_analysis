from sklearn.linear_model import LinearRegression
from sklearn.datasets import fetch_california_housing
from sklearn.model_selection import train_test_split
from sklearn.metrics import mean_squared_error, mean_absolute_error

data = fetch_california_housing()

X = data['data']
Y = data['target']

X_train, X_test, Y_train, Y_test = train_test_split(
    X, Y, test_size=0.2, random_state=42
)

model = LinearRegression()

model.fit(X_train, Y_train)

print(model.coef_)
print(model.intercept_)


predictions = model.predict(X_test)

mse_train = mean_squared_error(Y_train, model.predict(X_train))
mse_test = mean_squared_error(Y_test, predictions)

print("MSE train: ", mse_train)
print("MSE test: ", mse_test)


mae_train = mean_absolute_error(Y_train, model.predict(X_train))
mae_test = mean_absolute_error(Y_test, predictions)