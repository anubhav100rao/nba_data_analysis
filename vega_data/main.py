from vega_datasets import data
import matplotlib.pyplot as plt
import numpy as np
import pandas as pd

weather = data.seattle_weather()
print(weather.head())
weather = weather[['precipitation', 'temp_max', 'temp_min', 'wind']]
plt.imshow(weather.corr(), cmap='Spectral',
           interpolation='none', aspect='auto')
plt.colorbar()
plt.xticks(range(len(weather.corr().columns)), weather.corr().columns)
plt.yticks(range(len(weather.corr().columns)), weather.corr().columns)

labels = weather.corr().values
for a in range(labels.shape[0]):
    for b in range(labels.shape[1]):
        plt.text(a, b, '{:.2f}'.format(
            labels[b, a]), ha='center', va='center', color='black')
plt.show()
