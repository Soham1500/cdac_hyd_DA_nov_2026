import numpy as np
import pandas as pd

'''
What is a DataFrame?
A DataFrame is a two-dimensional, size-mutable, and heterogeneous tabular data structure with labeled axes (rows and columns). 

'''

df_cricket = pd.DataFrame({
    "name": ["Shubman Gill", "Deepti Sharma", "Mohammed Siraj", "Virat Kohli", "Smriti Mandhana", "Jasprit Bumrah", "Richa Ghosh", "Hardik Pandya"],
    "age": [25, 27, 31, 36, 28, 31, 21, 31],
    "gender": ["Male", "Female", "Male", "Male", "Female", "Male", "Female", "Male"]
})

print("--- In-Memory DataFrame ---")
print(df_cricket)

print("Extract the age column as a Series:")
age_series = df_cricket["age"]
print(age_series)
print(type(age_series))
print("describe the age column:")
print(age_series.describe())
print("Info about the DataFrame:")
print(df_cricket.info())
print("Shape of the DataFrame:",df_cricket.shape)
print("Data type of name column :",df_cricket['name'].dtype)
