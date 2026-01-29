import pandas as pd
titanic = pd.read_csv("day_3/titanic.csv")
print(titanic)

titanic= pd.read_csv("day_3/titanic.csv")
"""print(titanic)
print(titanic['Age'].fillna(titanic['Age'].mean(), inplace=True))
print(titanic.isnull().sum())
print(titanic["Age"].isnull().sum())"""
print(titanic.drop("Cabin",inplace=True))
