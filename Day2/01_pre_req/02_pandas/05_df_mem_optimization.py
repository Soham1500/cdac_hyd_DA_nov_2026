import pandas as pd
import numpy as np
# Setting explicit index column on load
df_indexed = pd.read_csv("supportFiles/drinks.csv", index_col="country")
print("Custom Country Index Preview:\n", df_indexed.head(3))

# look at ram footprint
mem_original_surface = df_indexed.memory_usage().sum()
print("Original memory used : ", mem_original_surface)
mem_original_element_level = df_indexed.memory_usage(deep=True).sum()
print("Original memory used : ", mem_original_element_level)
print("=" * 60)
print(df_indexed.info())
print("=" * 60)
print("{0:35}{1:15}{2:15}{3:<15}{4:<15}".format("Column Name","Min","Max","type","Can hold"))
print("_" * 60)
for col in df_indexed.select_dtypes(include='number').columns:
# for col in df_indexed.select_dtypes(include=[np.number]).columns:
# for col in df_indexed.select_dtypes(include=['int64','float64']).columns:
    dt = df_indexed[col].dtype
    max_can_hold = np.iinfo(dt).max if np.issubdtype(dt,np.integer) else np.finfo(dt).max
    print("{0:<35}{1:<15}{2:<15}{3:<15}{4:<15}".format(col.capitalize(),
                                         df_indexed[col].min(), 
                                         df_indexed[col].max(),
                                         dt.__str__(),
                                         max_can_hold
                                         
                                         ))
print("=" * 60)
# downcasting
df_optimized = df_indexed.copy()
for col in df_optimized.select_dtypes(include=[np.number]).columns:
    dt = df_optimized[col].dtype
    cast_to_str = "integer" if np.issubdtype(dt,np.integer) else "float" 
    df_optimized[col] = pd.to_numeric(df_optimized[col],downcast=cast_to_str)
    # convert dtype of a column
print("=" * 60)

print(df_optimized.info())
print("=" * 60)
mem_optimized_surface = df_optimized.memory_usage().sum()
print("Optimized memory used : ", mem_optimized_surface)
mem_optimized_element_level = df_optimized.memory_usage(deep=True).sum()
print("Optimized memory used : ", mem_optimized_element_level)