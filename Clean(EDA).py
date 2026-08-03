# ===============================
# STEP 4 : EXPLORATORY DATA ANALYSIS (EDA)
# ===============================

import pandas as pd
import matplotlib.pyplot as plt
import warnings
warnings.simplefilter("ignore", UserWarning)

# Load Clean Dataset
df = pd.read_excel("Clean_Sales_Data.xlsx")

# Normalize column names
df.columns = df.columns.str.strip().str.lower().str.replace(" ", "_")

# ===============================
# 1. Total Sales
# ===============================
if "sales" in df.columns:
    print("Total Sales :", df["sales"].sum())
else:
    print("⚠️ 'sales' column not found")

# ===============================
# 2. Total Profit
# ===============================
if "profit" in df.columns:
    print("Total Profit :", df["profit"].sum())
else:
    print("⚠️ 'profit' column not found")

# ===============================
# 3–5. Sales Stats
# ===============================
if "sales" in df.columns:
    print("Average Sales :", df["sales"].mean())
    print("Highest Sale :", df["sales"].max())
    print("Lowest Sale :", df["sales"].min())

# ===============================
# 6. Sales by City
# ===============================
if "city" in df.columns and "sales" in df.columns:
    city_sales = df.groupby("city")["sales"].sum().sort_values(ascending=False)
    plt.figure(figsize=(8,5))
    city_sales.plot(kind="bar")
    plt.title("Sales by City")
    plt.xlabel("City")
    plt.ylabel("Sales")
    plt.tight_layout()
    plt.show()

# ===============================
# 7. Profit by Product
# ===============================
if "product" in df.columns and "profit" in df.columns:
    product_profit = df.groupby("product")["profit"].sum().sort_values(ascending=False)
    plt.figure(figsize=(8,5))
    product_profit.plot(kind="bar")
    plt.title("Profit by Product")
    plt.xlabel("Product")
    plt.ylabel("Profit")
    plt.tight_layout()
    plt.show()

# ===============================
# 8. Sales by Category
# ===============================
if "category" in df.columns and "sales" in df.columns:
    category_sales = df.groupby("category")["sales"].sum()
    plt.figure(figsize=(6,6))
    category_sales.plot(kind="pie", autopct="%1.1f%%")
    plt.title("Sales by Category")
    plt.ylabel("")
    plt.show()

# ===============================
# 9. Payment Mode Distribution
# ===============================
if "payment_mode" in df.columns:
    payment = df["payment_mode"].value_counts()
    plt.figure(figsize=(6,6))
    payment.plot(kind="pie", autopct="%1.1f%%")
    plt.title("Payment Mode Distribution")
    plt.ylabel("")
    plt.show()

# ===============================
# 10. Salesperson Performance
# ===============================
if "salesperson" in df.columns and "profit" in df.columns:
    salesperson_profit = df.groupby("salesperson")["profit"].sum().sort_values(ascending=False)
    plt.figure(figsize=(8,5))
    salesperson_profit.plot(kind="bar")
    plt.title("Profit by Salesperson")
    plt.xlabel("Salesperson")
    plt.ylabel("Profit")
    plt.tight_layout()
    plt.show()

# ===============================
# 11. Monthly Sales Trend
# ===============================
if "date" in df.columns and "sales" in df.columns:
    df["month"] = df["date"].dt.to_period("M").astype(str)
    monthly_sales = df.groupby("month")["sales"].sum()
    plt.figure(figsize=(8,5))
    monthly_sales.plot(kind="line", marker="o")
    plt.title("Monthly Sales Trend")
    plt.xlabel("Month")
    plt.ylabel("Sales")
    plt.grid(True)
    plt.tight_layout()
    plt.show()

# ===============================
# 12. Correlation
# ===============================
num_cols = [col for col in ["quantity","unit_price","discount","sales","cost","profit"] if col in df.columns]
if num_cols:
    print("\nCorrelation Matrix")
    print(df[num_cols].corr())

# ===============================
# 13. Business Insights
# ===============================
print("\n========== BUSINESS INSIGHTS ==========")
if "city" in df.columns and "sales" in df.columns:
    print("Top City :", city_sales.idxmax())
if "product" in df.columns and "profit" in df.columns:
    print("Top Product :", product_profit.idxmax())
if "category" in df.columns and "sales" in df.columns:
    print("Best Category :", category_sales.idxmax())
if "payment_mode" in df.columns:
    print("Most Used Payment Mode :", payment.idxmax())
if "salesperson" in df.columns and "profit" in df.columns:
    print("Best Salesperson :", salesperson_profit.idxmax())
print("======================================")
