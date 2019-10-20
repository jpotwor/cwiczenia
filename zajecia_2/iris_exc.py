import seaborn
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt


iris = seaborn.load_dataset("iris")
print(iris.head())
# plt.scatter(iris.petal_length, iris.petal_width)
# plt.show()

print(iris.dtypes)
# rows from 1:10, columns 3, 4
print(iris.iloc[1:10, [3, 4]])
print(pd.Categorical(iris.iloc[:, 4]))
print(pd.Categorical(iris.loc[:, "species"]))

s = pd.Series(pd.Categorical(iris.loc[:, "species"]))
print(s)

# colors = np.array(["#f442bf", "#6e41f4", "#f4dc41"])[s.cat.codes]
# plt.scatter(iris.petal_length, iris.petal_width, c=colors)
# plt.show()


# przetrenowac trzy modele z sales.py dla danych iris
from sklearn import preprocessing
le = preprocessing.LabelEncoder()
classes = le.fit_transform(s)
print(classes)

labels = classes
data = iris.drop(columns='species')
print(data)


from sklearn.model_selection import train_test_split
data_train, data_test, target_train, target_test = train_test_split(
    data, labels, test_size=0.20, random_state=10
)


from sklearn.naive_bayes import GaussianNB
from sklearn.metrics import accuracy_score

gnb = GaussianNB()
pred = gnb.fit(data_train, target_train).predict(data_test)
print("Naive-Bayes accuracy : ", accuracy_score(target_test, pred, normalize=True))


from sklearn.svm import LinearSVC
from sklearn.metrics import accuracy_score


svc_model = LinearSVC(random_state=0)
pred = svc_model.fit(data_train, target_train).predict(data_test)
print("LinearSVC accuracy : ", accuracy_score(target_test, pred, normalize=True))


from sklearn.neighbors import KNeighborsClassifier
from sklearn.metrics import accuracy_score


neigh = KNeighborsClassifier(n_neighbors=3, weights='distance')
neigh.fit(data_train, target_train)
pred = neigh.predict(data_test)
print("KNeighbors accuracy score : ", accuracy_score(target_test, pred))
