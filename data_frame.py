import pandas as pd
import numpy as np


df = pd.DataFrame({
     'one': pd.Series(np.random.randn(3), index=['a', 'b', 'c']),
     'two': pd.Series(np.random.randn(4), index=['a', 'b', 'c', 'd']),
     'three': pd.Series(np.random.randn(3), index=['b', 'c', 'd'])
})


print(df.groupby('two').tail())
























print(df)
row = df.iloc[1]
print(row)
column = df['two']
print(column)
df.sub(row, axis='columns')
print(df)
df.sub(row, axis=1)
print(df)
df.sub(column, axis='index')
print(df)
df.sub(column, axis=0)
print(df)


print(df.max())
print(df.std())
