import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression

df = pd.read_csv('dataset.csv')

X_train = df.iloc[:-70, :4]
X_test = df.iloc[-70:, :4]
y_train = df.target[:-70]
y_test = df.target[-70:]


model = LinearRegression()
model.fit(X_train, y_train)
print(model.coef_)
print(model.intercept_)
