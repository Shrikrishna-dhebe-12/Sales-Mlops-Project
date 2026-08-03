# ===============================
# STEP 3 : DATA CLEANING
# ===============================

import pandas as pd
import warnings
warnings.simplefilter("ignore", UserWarning)

# Load Dataset
df = pd.read_excel("Data_Analyst_Practice_Sales_100_Rows.xlsx", skiprows=2)

# Normalize column names (strip spaces, lowercase, replace spaces with underscores)
df.columns = df.columns.str.strip().str.lower().str.replace(" ", "_")

# ===============================
# 1. Check Missing Values
# ===============================
print("Missing Values")
print(df.isnull().sum())

# Fill numerical columns safely
num_fill_map = {
    "quantity": "median",
    "unit_price": "median",
    "discount": 0,
    "Sales": "median",
    "cost": "median",
    "profit": "median"
}

for col, fill_strategy in num_fill_map.items():
    if col in df.columns:
        if fill_strategy == "median":
            df[col] = df[col].fillna(df[col].median())
        else:
            df[col] = df[col].fillna(fill_strategy)
    else:
        print(f"⚠️ Column '{col}' not found, skipping fill")

# Fill categorical columns safely
cat_fill_map = ["city", "state", "category", "product", "payment_mode", "salesperson"]

for col in cat_fill_map:
    if col in df.columns:
        df[col] = df[col].fillna("Unknown")
    else:
        print(f"⚠️ Column '{col}' not found, skipping fill")

# ===============================
# 2. Remove Duplicate Rows
# ===============================
print("\nDuplicate Rows Before :", df.duplicated().sum())
df = df.drop_duplicates()
print("Duplicate Rows After :", df.duplicated().sum())

# ===============================
# 3. Convert Data Types
# ===============================
if "date" in df.columns:
    df["date"] = pd.to_datetime(df["date"], dayfirst=True, errors="coerce")

for col in ["quantity", "unit_price", "discount", "sales", "cost", "profit"]:
    if col in df.columns:
        if col == "quantity":
            df[col] = df[col].astype(int, errors="ignore")
        else:
            df[col] = df[col].astype(float, errors="ignore")

# ===============================
# 4. Remove Negative Values
# ===============================
for col in ["quantity", "unit_price", "sales", "cost"]:
    if col in df.columns:
        df = df[df[col] >= 0]

# ===============================
# 5. Remove Invalid Discounts
# ===============================
if "discount" in df.columns:
    df = df[(df["discount"] >= 0) & (df["discount"] <= 1)]

# ===============================
# 6. Remove Extra Spaces
# ===============================
text_columns = ["customer_name", "city", "state", "category", "product", "payment_mode", "salesperson"]

for col in text_columns:
    if col in df.columns:
        df[col] = df[col].astype(str).str.strip()

# ===============================
# 7. Check Missing Values Again
# ===============================
print("\nMissing Values After Cleaning")
print(df.isnull().sum())

# ===============================
# 8. Final Shape
# ===============================
print("\nDataset Shape :", df.shape)

# ===============================
# 9. Save Clean Dataset
# ===============================
df.to_excel("Clean_Sales_Data.xlsx", index=False)
print("\n✅ Clean dataset saved successfully.")
