import matplotlib.pyplot as plt

item = ['oil', 'yogurt', 'sugar', 'milk']
number = [2, 4, 1, 3]

# Your Code Here
plt.scatter(item, number, s=100, c=number, cmap='Spectral')
plt.show()
