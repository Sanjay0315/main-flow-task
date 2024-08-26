#Importing all the libraries that we need.
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
#importing our dataset.
df = pd.read_csv('\\Users\\apple\\Desktop\\heart.csv')
#checking first five rows
df. head()
#checking last five rows
df.tail()
#take a Look at the colmun names.
df.columns.values()
#checking for null values
df.isna().sum()
#concise summary of our dataset.
df.info()
#plotting histogram of all numeric values
df.hist(bins=50, grid=False , figsize=(20, 15))
#Generating descriptive statistics.
df.describe()

questions = ["1. How many people have heart disease and how many people doesn't have heart disease? ",
             "2. People of which sex has most heart disease?",
             "3. People of which sex has which type of chest pain most?",
             "4. People with which chest pain are most pron to have heart disease?"]

#Let's find the answer of first question.
#1. How many people have heart disease and how many people doesn't have heart disease?'
#getting the values
df.target.value_counts()

#plotting bar chart.
df.target.value_counts().plot(kind='bar', color=["purple", "blue"])
plt.title("Heart Disease values")
plt.xlabel("1 = Heart Disease, 0 = No heart Disease")
plt.ylabel("Amount")

#pLotting a pie chart
df.target.value_counts().plot(kind='pie', figsize=(8, 6))
plt.legend(["Disease", "No disease"])

#'0'represent 'Female
#'1' represent 'Male'
#SEX column part
#'0' represent 'No disease'
#'1' represent 'Disease'
#Target column part
#Now let's check how many 'Male' and 'Female' are in the dataset
df.sex.value_counts()

#pLotting a pie chart
df.sex.value_counts().plot(kind='pie', figsize=(8, 6))
plt.title('Male Female ratio')
plt.legend(['Male', 'Female'])

#Let's find the answer of our 2nd question.
#2.People of which sex has most heart disease?'
pd.crosstab(df.target, df.sex)

sns.countplot(x='target', data=df, hue='sex')
pit.title("Heart Disease Frequency for Sex")
plt.xlabel("0 = No heart Disease, 1 = Heart Disease")

#Number of male is more than double in our dataset than female.
#More than '45% male' has heart disease and '75% female has heart disease.
#Let's move to question 3
#3. 'People of which sex has which type of chest pain most?'
#counting values for different chest pain
df.cp.value_counts()

#plotting a bar chart
df. cp. value_counts().plot(kind='bar', color=['red', 'skyblue', 'purple', 'green'])
plt. title('Chest pain type vs count')
pd.crosstab(df.sex, df.cp)
pd.crosstab(df.sex, df.cp).plot(kind='bar', color=['plum', 'skyblue', 'purple', 'green'])
plt.title('Type of chest pain for sex')
plt.xlabel('0 = Female,1 = Male')

#Most of 'male' has 'type @' chest pain and least of 'Male' has 'type 4' pain.
#in case of 'Female' 'type @' and 'type 2' percentage is almost same.
#Now question 4!
#4 People with which chest pain are most prom to have heart disease?"
pd.crosstab(df.cp, df.target)
sns.countplot(x='cp', data=df, hue='target')

#Most of the people who has 'type 0' chest pain has less chance of heart disease.
#And we see the opposite for other types.
#Now let's take look at ouf age column.
#create a distribution plot with normal distribution curve
sns.displot(x='age', data=df, bins=30, kde=True)

#'58-59 year old people are most in the dataset.
#Let's plot another distribution plot for "Maximum heart rate
sns.displot(x='thalach', data=df, bins=30, kde=True, color='chocolate')
#From this plot we get a clear overview about Maximum heart rate represented by 'thalach'
