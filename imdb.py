import pandas as pd


df = pd.read_csv('movie_metadata.csv', index_col='movie_title')
print(df.describe())
