# ===============================
# STEP 6 : MODEL TRAINING
# ===============================

import pandas as pd
import joblib
import warnings
warnings.simplefilter("ignore", UserWarning)

from sklearn.model_selection import train_test_split
from sklearn.preprocessing import LabelEncoder, StandardScaler

from sklearn.linear_model import LinearRegression
from sklearn.tree import DecisionTreeRegressor
from sklearn.ensemble import RandomForestRegressor

from sklearn.metrics import r2_score, mean_absolute_error, mean_squared_error

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
# Features & Target
# ===============================
if "profit" in df.columns:
    X = df.drop("profit", axis=1)
    y = df["profit"]

    # ===============================
    # Train Test Split
    # ===============================
    X_train, X_test, y_train, y_test = train_test_split(
        X, y, test_size=0.20, random_state=42
    )

    print("\nTraining Data :", X_train.shape)
    print("Testing Data :", X_test.shape)

    # ===============================
    # Models
    # ===============================
    models = {
        "Linear Regression": LinearRegression(),
        "Decision Tree": DecisionTreeRegressor(random_state=42),
        "Random Forest": RandomForestRegressor(random_state=42)
    }

    best_model = None
    best_score = -1

    print("="*60)

    for name, model in models.items():
        model.fit(X_train, y_train)
        prediction = model.predict(X_test)

        r2 = r2_score(y_test, prediction)
        mae = mean_absolute_error(y_test, prediction)
        mse = mean_squared_error(y_test, prediction)

        print(f"\n{name}")
        print("-"*40)
        print("R2 Score :", round(r2,4))
        print("MAE      :", round(mae,2))
        print("MSE      :", round(mse,2))

        if r2 > best_score:
            best_score = r2
            best_model = model

    print("\n" + "="*60)
    print("Best Model Selected Successfully")
    print("Best R2 Score :", round(best_score,4))

    # ===============================
    # Save Best Model
    # ===============================
    joblib.dump(best_model, "sales_prediction_model.pkl")
    print("\n✅ Model saved as sales_prediction_model.pkl")

else:
    print("\n⚠️ Target variable 'Profit' not found in dataset")
