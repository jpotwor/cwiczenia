import seaborn
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt


iris = seaborn.load_dataset("iris")
print(iris.head())
plt.scatter(iris.petal_length, iris.petal_width)
plt.show()

print(iris.dtypes)
# rows from 1:10, columns 3, 4
print(iris.iloc[1:10, [3, 4]])
print(pd.Categorical(iris.iloc[:, 4]))
print(pd.Categorical(iris.loc[:, "species"]))

s = pd.Series(pd.Categorical(iris.loc[:, "species"]))
print(s)

colors = np.array(["#f442bf", "#6e41f4", "#f4dc41"])[s.cat.codes]
plt.scatter(iris.petal_length, iris.petal_width, c=colors)
plt.show()


