'''
what is data wrangling?
Discovering
structuring
cleaning
enriching
validating
publishing
'''

'''
Missing Values
1. Identify
2. Drop
3. Impute
'''

import pandas as pd
import numpy as np
# Load titanic dataset
df_titanic = pd.read_csv("supportFiles/titanic.csv")
print(df_titanic.head())
print("=" * 60)
print("--- Missing Values Count Per Column ---")
print(df_titanic.isna().sum())
print("=" * 60)
median_age = df_titanic["Age"].median()
df_titanic["Age_Imputed"] = df_titanic["Age"].fillna(median_age)
df_titanic["Cabin_Filled"] = df_titanic["Cabin"].fillna("Unknown")
print("=" * 60)
print("After imputation Age ",df_titanic["Age_Imputed"].isna().sum())
print("After imputation Cabin ",df_titanic["Cabin_Filled"].isna().sum())
print("=" * 60)
print(df_titanic.head()[["Age","Age_Imputed","Cabin","Cabin_Filled"]])
df_titanic_cleaned = df_titanic.copy()

# 1
# df_titanic_cleaned["Age"]=df_titanic_cleaned["Age_Imputed"]
# df_titanic_cleaned["Cabin"]=df_titanic_cleaned["Cabin_Filled"]

# 2
# df_titanic_cleaned[["Age","Cabin"]] = df_titanic_cleaned[["Age_Imputed","Cabin_Filled"]]

# 3
df_titanic_cleaned = df_titanic_cleaned.assign(
        Age = df_titanic_cleaned['Age_Imputed'],
        Cabin = df_titanic_cleaned['Cabin_Filled']
        )
print(df_titanic_cleaned.isna().sum())
df_titanic_cleaned = df_titanic_cleaned.drop(columns=["Age_Imputed","Cabin_Filled"])
print("=" * 60)
print(df_titanic_cleaned.isna().sum())
print("=" * 60)
print(df_titanic_cleaned["Embarked"].value_counts())
print("=" * 60)
# most_used = df_titanic_cleaned["Embarked"].mode()
# print(most_used)
# print(most_used[0])
'''
Embarked
S    644    : Southampton (England)
C    168    : Cherbourg (France) — The first stopover.
Q     77    : Queenstown (Ireland)
'''
df_titanic_cleaned["Embarked"] = df_titanic_cleaned["Embarked"].fillna(df_titanic_cleaned["Embarked"].mode()[0])

print(df_titanic_cleaned.isna().sum())