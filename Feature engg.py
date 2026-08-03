# ===============================
# STEP 5 : FEATURE ENGINEERING
# ===============================

import pandas as pd
from sklearn.preprocessing import LabelEncoder, StandardScaler
from sklearn.model_selection import train_test_split
import warnings
warnings.simplefilter("ignore", UserWarning)

# ===============================
# Load Dataset
# ===============================
df = pd.read_excel("Clean_Sales_Data.xlsx")

# Normalize column names
df.columns = df.columns.str.strip().str.lower().str.replace(" ", "_")

# ===============================
# Remove Unnecessary Columns
# ===============================
drop_cols = ["order_id", "customer_name", "date"]
df = df.drop(columns=[col for col in drop_cols if col in df.columns], errors="ignore")

print("Columns after removing unnecessary columns:")
print(df.columns.tolist())

# ===============================
# Encode Categorical Columns
# ===============================
categorical_columns = ["city", "state", "category", "product", "payment_mode", "salesperson"]

encoder = LabelEncoder()

for col in categorical_columns:
    if col in df.columns:
        df[col] = encoder.fit_transform(df[col].astype(str))
    else:
        print(f"⚠️ Column '{col}' not found, skipping encoding")

print("\nCategorical Encoding Completed")

# ===============================
# Feature Scaling
# ===============================
scaler = StandardScaler()

numerical_columns = ["quantity", "unit_price", "discount", "sales", "cost"]
existing_num_cols = [col for col in numerical_columns if col in df.columns]

if existing_num_cols:
    df[existing_num_cols] = scaler.fit_transform(df[existing_num_cols])
    print("\nFeature Scaling Completed")
else:
    print("\n⚠️ No numerical columns found for scaling")

# ===============================
# Define Features & Target
# ===============================
if "profit" in df.columns:
    X = df.drop("profit", axis=1)
    y = df["profit"]

    print("\nFeature Shape :", X.shape)
    print("Target Shape :", y.shape)

    # ===============================
    # Train Test Split
    # ===============================
    X_train, X_test, y_train, y_test = train_test_split(
        X, y, test_size=0.20, random_state=42
    )

    print("\nTraining Data :", X_train.shape)
    print("Testing Data :", X_test.shape)

    # ===============================
    # Save Processed Dataset
    # ===============================
    processed_data = pd.concat([X, y], axis=1)
    processed_data.to_excel("Processed_Sales_Data.xlsx", index=False)
    print("\n✅ Processed dataset saved successfully.")
else:
    print("\n⚠️ Target variable 'Profit' not found in dataset")
