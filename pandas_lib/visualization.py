import pandas as pd
import matplotlib.pyplot as plt
df = pd.read_csv('../Data/2015.csv')

print(df.head())
# prevent this from automatically closing
df.plot(kind='hist', bins=15, y='Generosity')
plt.show(block=True)