import pandas as pd
from sklearn.linear_model import LinearRegression
import numpy as np
"""

Cost of advertising campaign, $	Number of new customers
4	2
6	2
8	3
10	5
12	5
14	6
16	6
"""

data = {
    "cost": [4, 6, 8, 10, 12, 14, 16],
    "customers": [2, 2, 3, 5, 5, 6, 6]
}

df = pd.DataFrame(data)
X = np.array(df.cost).reshape(-1, 1)
Y = np.array(df.customers)
print(X, Y)

model = LinearRegression()

model.fit(X, Y)
print(model.predict([[23]])) # need 2D array for predictions
