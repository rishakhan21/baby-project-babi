import pandas as pd

products = pd.read_csv("../data/product_info.csv")
brands = pd.read_csv("../data/brand_info.csv")

merged = pd.merge(products, brands, on="brand_name", how="left")

merged.to_csv("../clean_data/products_with_brand.csv", index=False)

print("Merge complete")

