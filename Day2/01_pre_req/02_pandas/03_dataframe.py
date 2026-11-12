import pandas as pd

# pip install openpyxl 

df_titanic = pd.read_csv("supportFiles/titanic.csv")
print("Loaded Titanic CSV Shape:", df_titanic.shape)
print(df_titanic.head(3))
print("=" * 60)

# Export DataFrame to Excel spreadsheet
df_titanic.to_excel("supportFiles/titanic.xlsx", sheet_name="passengers", index=False)

# Reload DataFrame from Excel spreadsheet
df_from_excel = pd.read_excel("supportFiles/titanic.xlsx", sheet_name="passengers")
print("\nReloaded Excel Passengers Shape:", df_from_excel.shape)