import pandas as pd
import numpy as np

# illustration 1
# Sample raw text dataset
df_raw = pd.DataFrame({
    'raw_title': ['  PROD_101_Laptop_v2  ', 'prod_102_Mobile_v1', '  PROD_103_Tablet_v3 ', 'prod_104_Monitor_v2']
})
print(df_raw)
print("=" * 60)
# Clean whitespace and standardize casing
df_raw['clean_title'] = df_raw['raw_title'].str.strip().str.upper()
print(df_raw)
print("=" * 60)
# Extract structured components using regular expressions
regex_pattern = r"PROD_(?P<ID>\d+)_(?P<Category>\w+)_(?P<Version>V\d+)"
df_extracted = df_raw['clean_title'].str.extract(regex_pattern)
print(df_extracted)
print("=" * 60)
df_strings = pd.concat([df_raw[['clean_title']], df_extracted], axis=1)
print("--- Vectorized String Extraction (.str.extract) ---")
print(df_strings)
print("=" * 60)

# illustration 2
print("=" * 60)
df_events = pd.DataFrame({
    'timestamp_str': ['2026-01-15 08:30:00', '2026-03-22 14:45:00', '2026-06-10 20:15:00'],
    'registration_date': ['2025-12-01', '2026-02-15', '2026-05-01']
})

# Convert string columns to datetime
df_events['event_time'] = pd.to_datetime(df_events['timestamp_str'])
df_events['reg_date'] = pd.to_datetime(df_events['registration_date'])

# Extract calendar properties via .dt
df_events['year'] = df_events['event_time'].dt.year
df_events['day_name'] = df_events['event_time'].dt.day_name()
df_events['month_name'] = df_events['event_time'].dt.month_name()
df_events['hour'] = df_events['event_time'].dt.hour

# Calculate timedelta difference
df_events['days_to_event'] = (df_events['event_time'] - df_events['reg_date']).dt.days

print("--- Datetime Parsing & Timedelta Output (.dt) ---")
print(df_events[['event_time', 'month_name', 'days_to_event']])
print("=" * 60)

df_feedback = pd.DataFrame({
    'priority': ['Medium', 'High', 'Low', 'High', 'Low', 'Medium']
})
# Define logical ordinal ordering
priority_order = ['Low', 'Medium', 'High']
df_feedback['priority'] = pd.Categorical(
    df_feedback['priority'], 
    categories=priority_order, 
    ordered=True
)
print("--- Ordinal Sorting Output ---")
print(df_feedback.sort_values(by='priority'))
print("=" * 60)

# illustration 3
np.random.seed(42)
df_scores = pd.DataFrame({
    'experience_years': np.random.randint(1, 20, 10)
})


# Fixed-value interval binning
df_scores['exp_group_cut'] = pd.cut(
    df_scores['experience_years'], 
    bins=[0, 5, 12, 20], 
    labels=['Junior', 'Mid-Level', 'Senior']
)

# Quantile (equal population) binning
df_scores['exp_group_qcut'] = pd.qcut(
    df_scores['experience_years'], 
    q=3, 
    labels=['Low_Tiers', 'Mid_Tiers', 'High_Tiers']
)

print(df_scores)
print("=" * 60)

# illustration 4 # pip install pyarrow
df_data = pd.DataFrame({'value': [-5, 10, 25, 50, 120]})
df_data['clipped_value'] = df_data['value'].clip(lower=0,upper=100)
print(df_data)
print("=" * 60)
# Save optimized DataFrame to Parquet
df_scores.to_parquet("supportFiles/binned_scores.parquet")

df_reloaded = pd.read_parquet("supportFiles/binned_scores.parquet")
print("\nReloaded Parquet Shape:", df_reloaded.shape)
print(df_reloaded)
print("=" * 60)
