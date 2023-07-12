from sklearn.preprocessing import Normalizer
from sklearn.preprocessing import MaxAbsScaler
from sklearn.preprocessing import MinMaxScaler
from sklearn.preprocessing import StandardScaler
import numpy as np
import pandas as pd
from sklearn.datasets import fetch_california_housing

data = fetch_california_housing(as_frame=True)
df = data.frame[['MedInc', 'Population']]


scaler_std = StandardScaler()
df_standard = scaler_std.fit_transform(df)
df_standard = pd.DataFrame(df_standard, columns=df.columns)


scaler_minmax = MinMaxScaler()
df_minmax = scaler_minmax.fit_transform(df)
df_minmax = pd.DataFrame(df_minmax, columns=df.columns)


scaler_maxabs = MaxAbsScaler()
df_maxabs = scaler_maxabs.fit_transform(df)
df_maxabs = pd.DataFrame(df_maxabs, columns=df.columns)


normalizer = Normalizer()
df_norm = normalizer.fit_transform(df)
df_norm = pd.DataFrame(df_norm, columns=df.columns)
