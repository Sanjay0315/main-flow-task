import pandas as pd

data = pd.read_csv('/Users/apple/Desktop/01.Data Cleaning and Preprocessing.csv')
print(data)
type(data)
# concise summary
data.info()
# descriptive statistics
data.describe()
data = data.drop_duplicates()
print(data)
data.isnull()
data.isnull().sum()
data.notnull()
data.isnull().sum().sum()
data2 = data.fillna(value=0)
print(data2)
data2.isnull().sum().sum()
# filling null values with the before value
data3 = data.fillna(method='pad')
print(data3)
# filling null values with the next value
data4 = data.fillna(method='bfill')
print(data4)
import numpy as np
from scipy import stats

# detect the outliers using IQR
print(data2.columns)
data2.drop(['Observation'], axis=1, inplace=True)
print(data2.columns)
Q1 = data2.quantile(0.25)
Q3 = data2.quantile(0.75)
IQR = Q3 - Q1
print(IQR)
data2 = data2[~((data2 < (Q1 - 1.5 * IQR)) | (data2 > (Q3 + 1.5 * IQR))).any(axis=1)]
print(data2)
data2.describe()
