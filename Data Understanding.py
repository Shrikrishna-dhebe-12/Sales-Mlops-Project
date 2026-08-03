# ===============================
# STEP 2 : DATA UNDERSTANDING
# ===============================

import pandas as pd

import warnings
warnings.simplefilter("ignore", UserWarning)

import pandas as pd
df = pd.read_excel("Data_Analyst_Practice_Sales_100_Rows.xlsx",skiprows=2)


# Normalize column names (strip spaces, lowercase)
df.columns = df.columns.str.strip().str.lower()

# ===============================
# 1. Display First 5 Rows
# ===============================
print("First 5 Rows")
print(df.head())

# ===============================
# 2. Display Last 5 Rows
# ===============================
print("\nLast 5 Rows")
print(df.tail())

# ===============================
# 3. Dataset Shape
# ===============================
print("\nDataset Shape")
print(df.shape)
print(f"\nTotal Rows : {df.shape[0]}")
print(f"Total Columns : {df.shape[1]}")

# ===============================
# 4. Column Names
# ===============================
print("\nColumn Names")
print(df.columns.tolist())

# ===============================
# 5. Dataset Information
# ===============================
print("\nDataset Information")
print(df.info())

# ===============================
# 6. Data Types
# ===============================
print("\nData Types")
print(df.dtypes)

# ===============================
# 7. Statistical Summary
# ===============================
print("\nStatistical Summary")
print(df.describe())

# ===============================
# 8. Missing Values
# ===============================
print("\nMissing Values")
print(df.isnull().sum())

# ===============================
# 9. Duplicate Rows
# ===============================
print("\nDuplicate Rows")
print(df.duplicated().sum())

# ===============================
# 10. Unique Values in Each Column
# ===============================
print("\nUnique Values Count")
print(df.nunique())

# ===============================
# 11–16. Unique Values (Safe Access)
# ===============================
for col in ["city", "state", "category", "product", "payment_mode", "salesperson"]:
    if col in df.columns:
        print(f"\nUnique {col.title()}s")
        print(df[col].unique())
    else:
        print(f"\n⚠️ Column '{col}' not found in dataset")

# ===============================
# 17. Check Numerical Columns
# ===============================
numerical_columns = ["quantity", "unit_price", "discount", "sales", "cost", "profit"]
existing_num_cols = [col for col in numerical_columns if col in df.columns]

print("\nNumerical Columns Summary")
if existing_num_cols:
    print(df[existing_num_cols].describe())
else:
    print("⚠️ No numerical columns found in dataset")


# ===============================
# 18. Check Categorical Columns
# ===============================
categorical_columns = ["city", "state", "category", "product", "payment_mode", "salesperson"]
existing_cat_cols = [col for col in categorical_columns if col in df.columns]

print("\nCategorical Columns Summary")
if existing_cat_cols:
    print(df[existing_cat_cols].describe())
else:
    print("⚠️ No categorical columns found in dataset")

# ===============================
# 19. Target Variable
# ===============================
if "profit" in df.columns:
    print("\nTarget Variable")
    print(df["profit"].head())
else:
    print("\n⚠️ Target variable 'Profit' not found")

# ===============================
# 20. Final Report
# ===============================
print("\n========== DATA UNDERSTANDING REPORT ==========")
print("Rows               :", df.shape[0])
print("Columns            :", df.shape[1])
print("Missing Values     :", df.isnull().sum().sum())
print("Duplicate Rows     :", df.duplicated().sum())
print("Target Variable    :", "Profit" if "profit" in df.columns else "⚠️ Not Found")
print("==============================================")
