import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns 
# pip install jinja2
cricket_stats = {
    'cricketers': [
        'Sachin Tendulkar', 'Virat Kohli', 'Ricky Ponting', 
        'Kumar Sangakkara', 'Jacques Kallis', 'Hashim Amla', 
        'Mahendra Singh Dhoni', 'Joe Root', 'Kane Williamson', 'Steve Smith'
    ],
    'fifties': [164, 220, 146, 153, 149, 88, 108, 105, 96, 78],
    'hundreds': [100, 80, 71, 63, 62, 55, 16, 49, 45, 44]
}
# pd.set_option("display.colheader_justify",'right')
df_cricket = pd.DataFrame(cricket_stats)
print(df_cricket)
print("=" * 60)
# df_cricket.style.set_properties(subset=['cricketers'],**{'text-align':'left'}) \
# .set_properties(subset=['fifties','hundreds'],**{'text-align':'right'}) \
# .hide(axis='index')
# print("=" * 60)
# print(df_cricket)
# print("=" * 60)
# print(df_cricket.to_string(justify="left",index=False))
# print("=" * 60)

# unpivot the dataframe
df_long = df_cricket.melt(id_vars="cricketers",var_name="Score Type",value_name="Count")
print(df_long)

# visualization
# Render grouped bar plot via Seaborn
plt.figure(figsize=(10, 5))
sns.barplot(x="cricketers", y="Count", hue="Score Type", data=df_long)
plt.legend(title="Score Type")
plt.xticks(rotation=45, ha="right")
plt.xlabel("Cricketers")
plt.ylabel("Score Count")
plt.title("International Cricket Performance: Fifties vs Hundreds")
plt.tight_layout()
plt.show()