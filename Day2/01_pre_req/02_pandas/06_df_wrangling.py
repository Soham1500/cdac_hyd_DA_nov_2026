'''
what is data wrangling?
Discovering
structuring
cleaning
enriching
validating
publishing
'''
import pandas as pd
import numpy as np
# Load beverages dataset
df_drinks = pd.read_csv("supportFiles/drinks.csv")
print(df_drinks.head())
print("=" * 60)
print(df_drinks.sort_values(by='spirit_servings',ascending=False).head()[["country","spirit_servings","continent"]])

print("=" * 60)
print(df_drinks["continent"].value_counts())
print("=" * 60)
print("--- High Spirit Consumption(>200) (European Countries) ---")
mask_europe = (df_drinks["continent"] == "Europe") & (df_drinks["spirit_servings"] > 200)
df_high_spirit_eu = df_drinks[mask_europe]
print(df_high_spirit_eu[["country","spirit_servings","continent","total_litres_of_pure_alcohol"]])
print("=" * 60)
print("Countries from Aisa and Africa")
continent_mask  = df_drinks['continent'].isin(["Asia","Africa"])
df_selected_continent = df_drinks[continent_mask]
print(df_selected_continent[["country","continent"]]) 
print("=" * 60)
print("Shape : ",df_selected_continent.shape)
print("=" * 60)
print(df_selected_continent["continent"].value_counts())
print("=" * 60)
