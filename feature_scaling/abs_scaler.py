"""
Suppose you have a variable X as show below. 
Scale each feature individually to its maximum absolute value. Use the default parameters. Print out the result after the transformation.
"""

from sklearn.preprocessing import MaxAbsScaler
X = [[8, -2, 3], [2, 25, 0], [4, 0, -2]]

scaler = MaxAbsScaler()
df = scaler.fit_transform(X)
print(df)
