import pandas as pd
import os
import requests

# Checking ../Data directory presence
if not os.path.exists('../Data'):
    os.mkdir('../Data')

# Download data if it is unavailable.
if 'nba2k-full.csv' not in os.listdir('../Data'):
    print('Train dataset loading.')
    url = "https://www.dropbox.com/s/wmgqf23ugn9sr3b/nba2k-full.csv?dl=1"
    r = requests.get(url, allow_redirects=True)
    open('../Data/nba2k-full.csv', 'wb').write(r.content)
    print('Loaded.')

data_path = "../Data/nba2k-full.csv"

# write your code here


def get_height_in_metres(height):
    feets, meters = height.split('/')
    return float(meters)


def get_weight_in_kg(weight):
    lbs, kgs = weight.split('/')
    kgs = kgs.strip()
    val, units = list(kgs.split(' '))
    return float(val)


def remove_dollar_sign(value):
    value = value.replace('$', '')
    return float(value)


def categorize_country(country):
    if country == 'USA':
        return 'USA'
    return 'NON-USA'


def handle_draft_round(round):
    if round == 'Undrafted':
        return '0'
    return round


def clean_data(path):
    df = pd.read_csv(path)
    df['b_day'] = pd.to_datetime(df['b_day'])
    df['draft_year'] = pd.to_datetime(df['draft_year'])
    df['team'].fillna('No team', inplace=True)
    df['height'] = df['height'].apply(get_height_in_metres)
    df['weight'] = df['weight'].apply(get_weight_in_kg)
    df['salary'] = df['salary'].apply(remove_dollar_sign)
    df['country'] = df['country'].apply(categorize_country)
    df['draft_round'] = df['draft_round'].apply(handle_draft_round)

    return df


clean_data(data_path)
