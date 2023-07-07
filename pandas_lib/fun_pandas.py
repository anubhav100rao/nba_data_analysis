import pandas as pd

def basics():
    ages_list = [21, 20, 25, 22]
    names_list = ['Anna', 'Bob', 'Maria', 'Jack']

    ages_series = pd.Series(ages_list, index=names_list, name='Age')


    algebra_series = pd.Series({'Anna': 5, 'Bob': 4, 'Maria': 3, 'Jack': 5}, name='Algebra')
    calculus_series = pd.Series({'Anna': 4, 'Bob': 5, 'Maria': 3, 'Jack': 4}, name='Calculus')

    average = (algebra_series + calculus_series) / 2
    print(average)

    total = algebra_series + calculus_series
    print(total)

def pets():
    pets = {
        'species': ['cat', 'dog', 'parrot', 'cockroach'], 
        'name': ['Dr. Mittens Lamar', 'Diesel', 'Peach', 'Richard'], 
        'legs': [4, 4, 2, 6],
        'wings': [0, 0, 2, 4],
        'looking_for_home': ['no', 'no', 'no', 'yes']
    }
    df = pd.DataFrame(pets)
    print(df.head())

    print(df.axes)

    df.set_index

def github():
    df = pd.read_csv('https://raw.githubusercontent.com/mwaskom/seaborn-data/master/penguins.csv')
    print(df.head())
    print(df.columns)
    print(df.flipper_length_mm.mean())
github()