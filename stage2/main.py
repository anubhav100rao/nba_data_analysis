import pandas as pd
import numpy as np
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
    return 'Not-USA'


def handle_draft_round(round):
    if round == 'Undrafted':
        return '0'
    return round


def clean_data(path):
    df = pd.read_csv(path)
    df['b_day'] = pd.to_datetime(df['b_day'])
    df['draft_year'] = pd.to_datetime(df['draft_year'], format='%Y')
    df['team'].fillna('No Team', inplace=True)
    df['height'] = df['height'].apply(get_height_in_metres)
    df['weight'] = df['weight'].apply(get_weight_in_kg)
    df['salary'] = df['salary'].apply(remove_dollar_sign)
    df['country'] = df['country'].apply(categorize_country)
    df['draft_round'] = df['draft_round'].apply(handle_draft_round)
    return df


data = clean_data(data_path)


def parse_version(version):
    year = version[-2:]
    return pd.to_datetime('20' + year)


def feature_data(df):
    df['version'] = df['version'].apply(parse_version)
    df['age'] = (df['version'] - df['b_day']) / np.timedelta64(1, 'Y')
    df['age'] = df['age'].astype(int)
    df['age'] += 1
    df['experience'] = (df['version'] - df['draft_year']) / np.timedelta64(1, 'Y')
    df['experience'] = df['experience'].astype(int)

    df['bmi'] = df['weight'] / (df['height'] ** 2)
    df.drop(['version', 'b_day', 'draft_year', 'weight', 'height'], axis=1, inplace=True)

    columns = df.columns.tolist()
    for col in columns:
        if df[col].dtype == object and df[col].nunique() > 50:
            df.drop(col, axis=1, inplace=True)

    return df


print(feature_data(data))
