import pandas as pd


df = pd.read_csv('https://covid19.who.int/WHO-COVID-19-global-data.csv')
df.drop(['Country_code', 'WHO_region'], axis=1, inplace=True)

df.to_csv("covid19_data.csv", index=False)