import matplotlib.pyplot as plt
import numpy as np


def plot_intro():
    fig, ax = plt.subplots()
    x = np.linspace(0, 10, 200)  # x data
    y = np.sin(x) + x + 1            # y data
    ax.plot(x, y)                # creates the plot
    fig.show()


def plot_bar():
    films = ['Wonder Woman', 'Sonic', '1917', 'Star Wars', 'Onward']
    box_office = [16.7, 26.1, 37.0, 34.5, 10.6]

    plt.bar(films, box_office)

    # add grid lines
    plt.grid(color='grey', linestyle=':', linewidth=1.0, axis='y', alpha=0.5)

    plt.ylabel('Box Office (mil. $)')
    plt.xlabel('Film title')
    plt.title('Box office of 5 different films of 2020 in the USA')

    plt.show()


def multi_plot_bar():
    years = ["2016", "2017", "2018", "2019"]
    cats = [57, 50, 47, 30]
    dogs = [43, 50, 53, 70]

    # create x-axis values depending on the number of years
    x_axis = np.arange(len(years))
    print(x_axis)
    # increase the figure size
    plt.figure(figsize=(10, 6))

    plt.bar(x_axis-0.2, cats, width=0.4, label='Cats')
    plt.bar(x_axis+0.2, dogs, width=0.4, label='Dogs')

    # set tick labels and their location
    plt.xticks(x_axis, years)

    plt.xlabel('Years', fontsize=14)
    plt.ylabel('Preference (%)', fontsize=14)
    plt.title('The results of cat/dog survey', fontsize=20)

    # add legend
    plt.legend()

    plt.show()


def quiz1():
    payment_method = ['Debit', 'Credit', 'Cash', 'Other']
    statistics = [48, 33, 9, 10]
    colors = ['lightblue', 'yellowgreen', 'coral', 'gold']

    # YOUR CODE HERE #
    plt.barh(payment_method, statistics, color=colors)

    plt.xlabel('Number of transactions (%)')
    plt.ylabel('Methods')
    plt.title('Preferred payment methods in 2014')
    plt.show()


quiz1()
