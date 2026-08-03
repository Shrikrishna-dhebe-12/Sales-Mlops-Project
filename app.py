# ===============================
# STEP 9 + STEP 10 : TRAINING + PRODUCTION FLASK API
# ===============================

from flask import Flask, request, jsonify
import pandas as pd
import joblib
import warnings
warnings.simplefilter("ignore", UserWarning)

from sklearn.preprocessing import LabelEncoder, StandardScaler
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestRegressor

# ===============================
# TRAINING PHASE
# ===============================

# Load Dataset
df = pd.read_excel("Clean_Sales_Data.xlsx")
df.columns = df.columns.str.strip().str.lower().str.replace(" ", "_")

# Remove unwanted columns safely
drop_cols = ["order_id", "customer_name", "date"]
df = df.drop(columns=[col for col in drop_cols if col in df.columns], errors="ignore")

# Label Encoding
encoders = {}
categorical_columns = ["city", "state", "category", "product", "payment_mode", "salesperson"]

for col in categorical_columns:
    if col in df.columns:
        encoder = LabelEncoder()
        df[col] = encoder.fit_transform(df[col].astype(str))
        encoders[col] = encoder
    else:
        print(f"⚠️ Column '{col}' not found, skipping encoding")

print("\nCategorical Encoding Completed")

# Feature Scaling
scaler = StandardScaler()
numerical_columns = ["quantity", "unit_price", "discount", "sales", "cost"]
existing_num_cols = [col for col in numerical_columns if col in df.columns]

if existing_num_cols:
    df[existing_num_cols] = scaler.fit_transform(df[existing_num_cols])
    print("\nFeature Scaling Completed")
else:
    print("\n⚠️ No numerical columns found for scaling")

# Features & Target
if "profit" in df.columns:
    X = df.drop("profit", axis=1)
    y = df["profit"]

    # Train Model
    X_train, X_test, y_train, y_test = train_test_split(
        X, y, test_size=0.20, random_state=42
    )

    model = RandomForestRegressor(random_state=42)
    model.fit(X_train, y_train)

    # Save Everything
    joblib.dump(model, "model.pkl")
    joblib.dump(encoders, "encoders.pkl")
    joblib.dump(scaler, "scaler.pkl")

    print("\n✅ Production files saved successfully.")
    print("Saved: model.pkl, encoders.pkl, scaler.pkl")

else:
    print("\n⚠️ Target variable 'Profit' not found in dataset")

# ===============================
# FLASK API
# ===============================

# Load saved files
model = joblib.load("model.pkl")
encoders = joblib.load("encoders.pkl")
scaler = joblib.load("scaler.pkl")

app = Flask(__name__)

@app.route("/", methods=["GET"])
def home():
    return jsonify({
        "message": "✅ Sales Prediction API Running Successfully"
    })

@app.route("/predict", methods=["POST"])
def predict():
    try:
        data = request.get_json()

        # Normalize keys
        input_df = pd.DataFrame([data])
        input_df.columns = input_df.columns.str.strip().str.lower().str.replace(" ", "_")

        # Required fields check
        required_columns = categorical_columns + numerical_columns
        for col in required_columns:
            if col not in input_df.columns:
                return jsonify({"error": f"{col} is missing."}), 400

        # Encode categorical columns
        for col in categorical_columns:
            key = col.lower()
            val = str(input_df[col].iloc[0])
            le = encoders[key]
            if val in le.classes_:
                input_df[col] = le.transform([val])
            else:
                print(f"⚠️ Unseen category '{val}' in column '{col}', mapping to default")
                if "Unknown" in le.classes_:
                    input_df[col] = le.transform(["Unknown"])
                else:
                    input_df[col] = le.transform([le.classes_[0]])

        # Scale numerical columns
        input_df[numerical_columns] = scaler.transform(input_df[numerical_columns])

        # Prediction
        prediction = model.predict(input_df)

        return jsonify({
            "Predicted Profit": round(float(prediction[0]), 2)
        })

    except Exception as e:
        return jsonify({"error": str(e)}), 500

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000, debug=True)
