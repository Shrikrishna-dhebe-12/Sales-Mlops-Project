# ===============================
# STEP 7 : MODEL EVALUATION
# ===============================

import pandas as pd
import joblib
import matplotlib.pyplot as plt
import warnings
warnings.simplefilter("ignore", UserWarning)

from sklearn.metrics import mean_absolute_error, mean_squared_error, r2_score
from sklearn.model_selection import train_test_split

# ===============================
# Load Best Model
# ===============================
model = joblib.load("sales_prediction_model.pkl")

# ===============================
# Load Processed Dataset (matches training features)
# ===============================
df = pd.read_excel("Processed_Sales_Data.xlsx")
df.columns = df.columns.str.strip().str.lower().str.replace(" ", "_")

# ===============================
# Features & Target
# ===============================
if "profit" in df.columns:
    X = df.drop("profit", axis=1)
    y = df["profit"]

    # Train/Test Split (same as training)
    X_train, X_test, y_train, y_test = train_test_split(
        X, y, test_size=0.20, random_state=42
    )

    # ===============================
    # Predict on Test Data
    # ===============================
    y_pred = model.predict(X_test)

    # ===============================
    # Evaluation Metrics
    # ===============================
    mae = mean_absolute_error(y_test, y_pred)
    mse = mean_squared_error(y_test, y_pred)
    rmse = mse ** 0.5
    r2 = r2_score(y_test, y_pred)

    print("="*50)
    print("MODEL EVALUATION")
    print("="*50)
    print(f"MAE        : {mae:.2f}")
    print(f"MSE        : {mse:.2f}")
    print(f"RMSE       : {rmse:.2f}")
    print(f"R2 Score   : {r2:.4f}")

    # ===============================
    # Actual vs Predicted
    # ===============================
    results = pd.DataFrame({
        "Actual Profit": y_test.values,
        "Predicted Profit": y_pred
    })

    print("\nFirst 10 Predictions")
    print(results.head(10))

    # ===============================
    # Scatter Plot
    # ===============================
    plt.figure(figsize=(8,5))
    plt.scatter(y_test, y_pred)
    plt.xlabel("Actual Profit")
    plt.ylabel("Predicted Profit")
    plt.title("Actual vs Predicted Profit")
    plt.grid(True)
    plt.tight_layout()
    plt.show()

    # ===============================
    # Prediction Error
    # ===============================
    results["Error"] = results["Actual Profit"] - results["Predicted Profit"]

    print("\nPrediction Error Summary")
    print(results["Error"].describe())

    # ===============================
    # Save Prediction Results
    # ===============================
    results.to_excel("Prediction_Results.xlsx", index=False)
    print("\n✅ Prediction results saved successfully.")

else:
    print("\n⚠️ Target variable 'Profit' not found in dataset")
