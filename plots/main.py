import matplotlib.pyplot as plt
import numpy as np


fig, ax = plt.subplots()
x = np.linspace(0, 10, 200)  # x data
y = np.sin(x) + x + 1            # y data
ax.plot(x, y)                # creates the plot
fig.show()
