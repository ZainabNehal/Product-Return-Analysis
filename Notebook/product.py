import pandas as pd

df = pd.read_csv("ecommerce_returns_synthetic_data.csv")

# Basi cleaning 
df.info()
df.isnull().sum()

df.to_csv("Cleaned_Product_Return_Data.csv", index=False)
