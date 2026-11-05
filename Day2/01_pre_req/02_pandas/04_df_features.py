import pandas as pd
df_drinks = pd.read_csv("supportFiles/drinks.csv")

print("--- Dataset Preview (Head) ---")
print(df_drinks.head(3))
print("=" * 60)

print("\n--- Index Object ---")
print(df_drinks.index)
print("=" * 60)

print("\n--- Column Names ---")
print(df_drinks.columns)
print("=" * 60)

print("\n--- Data Types ---")
print(df_drinks.dtypes)
print("=" * 60)

print("\n--- Underlying Matrix Shape & Axes ---")
print("Shape:", df_drinks.shape)
print("Axes: ", df_drinks.axes) # axes gives : column names
print("=" * 60)

print("\n--- Concise Schema Summary (`.info()`) ---")
df_drinks.info()
print("=" * 60)

print(df_drinks.describe())
print("=" * 60)
print(df_drinks.describe().T[["mean","std","min","max"]])
print("=" * 60)

df_subset = df_drinks[["country","continent","total_litres_of_pure_alcohol"]].copy()
print(df_subset.head())
print("=" * 60)
df_subset["status"] = "Evaluated"
print(df_subset.head())
print("=" * 60)
df_subset.insert(1,"region_category",value="Standard Market")
print(df_subset.head())
print("=" * 60)
df_subset["boosted_litres"] = df_subset["total_litres_of_pure_alcohol"].add(2.5)
print("=" * 60)
print(df_subset.head())
