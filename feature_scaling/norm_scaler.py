"""
Normalize each sample individually to a unit norm. Use the default norm. Print out the transformed values for the 4th sample of the dataframe.


"""
import pandas as pd
from sklearn.preprocessing import Normalizer

data = {'alcohol': [14.23, 13.2, 13.16, 14.37, 13.24, 14.2, 14.39, 14.06, 14.83, 13.86, 14.1, 14.12, 13.75, 14.75, 14.38, 13.63, 14.3, 13.83, 14.19, 13.64],
        'malic_acid': [1.71, 1.78, 2.36, 1.95, 2.59, 1.76, 1.87, 2.15, 1.64, 1.35, 2.16, 1.48, 1.73, 1.73, 1.87, 1.81, 1.92, 1.57, 1.59, 3.1],
        'ash': [2.43, 2.14, 2.67, 2.5, 2.87, 2.45, 2.45, 2.61, 2.17, 2.27, 2.3, 2.32, 2.41, 2.39, 2.38, 2.7, 2.72, 2.62, 2.48, 2.56],
        'alcalinity_of_ash': [15.6, 11.2, 18.6, 16.8, 21.0, 15.2, 14.6, 17.6, 14.0, 16.0, 18.0, 16.8, 16.0, 11.4, 12.0, 17.2, 20.0, 20.0, 16.5, 15.2],
        'magnesium': [127.0, 100.0, 101.0, 113.0, 118.0, 112.0, 96.0, 121.0, 97.0, 98.0, 105.0, 95.0, 89.0, 91.0, 102.0, 112.0, 120.0, 115.0, 108.0, 116.0]}
df = pd.DataFrame(data)

scaler = Normalizer()
df_norm = scaler.fit_transform(df)
print(df_norm[3])
# df_norm = pd.DataFrame(df_norm, columns=df.columns)
# print(df_norm.iloc[3])
