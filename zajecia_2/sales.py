import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
from sklearn import preprocessing


sales_data = pd.read_csv('~/sales_data')

print(sales_data.head())
print(sales_data.dtypes)

# sns.set(style='whitegrid', color_codes=True)
# sns.set(rc={'figure.figsize': (11.7, 8.27)})
# sns.countplot('Route To Market', data=sales_data, hue='Opportunity Result')
# plt.show()

le = preprocessing.LabelEncoder()
encoded_value = le.fit_transform(["paris", "paris", "tokyo", "amsterdam"])
print(encoded_value)

print("Supplies Subgroup' : ", sales_data['Supplies Subgroup'].unique())
print("Region : ", sales_data['Region'].unique())
print("Route To Market : ", sales_data['Route To Market'].unique())
print("Opportunity Result : ", sales_data['Opportunity Result'].unique())
print("Competitor Type : ", sales_data['Competitor Type'].unique())
print("'Supplies Group : ", sales_data['Supplies Group'].unique())

sales_data['Supplies Subgroup'] = le.fit_transform(sales_data['Supplies Subgroup'])
sales_data['Region'] = le.fit_transform(sales_data['Region'])
sales_data['Route To Market'] = le.fit_transform(sales_data['Route To Market'])
sales_data['Opportunity Result'] = le.fit_transform(sales_data['Opportunity Result'])
sales_data['Competitor Type'] = le.fit_transform(sales_data['Competitor Type'])
sales_data['Supplies Group'] = le.fit_transform(sales_data['Supplies Group'])
