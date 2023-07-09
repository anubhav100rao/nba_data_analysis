import pandas as pd
"""
+----+-----------+----------+---------+
|    | country   |   points |   price |
|----+-----------+----------+---------|
|  0 | Argentina |       89 |      26 |
|  1 | Argentina |       88 |      24 |
|  2 | Argentina |       88 |      25 |
|  3 | Argentina |       87 |      18 |
|  4 | Argentina |       83 |      13 |
+----+-----------+----------+---------+
"""

json_data = {
    "country": ["Argentina", "Argentina", "Argentina", "Argentina", "Argentina"],
    "points": [89, 88, 88, 87, 83],
    "price": [26, 24, 25, 18, 13]
}

wine_sample = pd.DataFrame(json_data)
print(wine_sample['country'].nunique())

countries_amount = wine_sample['country'].nunique()
print(countries_amount)
