**Sales Prediction MLOps Pipeline**

An end-to-end Machine Learning Operations (MLOps) project that demonstrates the complete lifecycle of a machine learning model, from data preprocessing and feature engineering to model deployment and experiment tracking.
The primary objective of this project is to simulate how machine learning models are developed, evaluated, deployed, and managed in a real production environment using industry-standard tools.

**Project Objectives**

• Build a complete machine learning pipeline from raw data to deployment.
• Compare multiple regression algorithms and select the best-performing model.
• Deploy the trained model as a REST API using Flask.
• Containerize the application using Docker.
• Track experiments, parameters, and evaluation metrics using MLflow.
• Automate development workflow with GitHub.
• Deploy the application to the cloud.

**Project Workflow**

Raw Sales Dataset

↓

Data Understanding

↓

Data Cleaning

↓

Exploratory Data Analysis (EDA)

↓

Feature Engineering

↓

Data Preprocessing
- Label Encoding
- Feature Scaling

↓

Train-Test Split

↓

Model Training
- Linear Regression
- Decision Tree Regressor
- Random Forest Regressor

↓

Model Evaluation
- R² Score
- MAE
- MSE

↓

Best Model Selection

↓

Model Serialization

↓

Flask REST API

↓

Docker Containerization

↓

GitHub Version Control

↓

Railway Cloud Deployment

↓

MLflow Experiment Tracking

**Project Structure**
```
MLOPS/
│
├── Data Understanding.py
├── Data Cleaning.py
├── Clean(EDA).py
├── Feature engg.py
├── Model train.py
├── Model evaluation.py
├── app.py
├── Dockerfile
├── requirements.txt
├── sales_prediction_model.pkl
├── model.pkl
├── scaler.pkl
├── encoders.pkl
├── Processed_Sales_Data.xlsx
├── Clean_Sales_Data.xlsx
├── Prediction_Results.xlsx
├── .github/
│   └── workflows/
│       └── ci.yml
└── README.md
```

**Machine Learning Models**
• Linear Regression
• Decision Tree Regressor
• Random Forest Regressor

**Evaluation Metrics**
• R² Score
• Mean Absolute Error (MAE)
• Mean Squared Error (MSE)

**Technology Stack**

**Programming Language**
• Python

**Libraries**
• Pandas
• NumPy
• Scikit-learn
• Flask
• Joblib
• MLflow
• OpenPyXL

**DevOps & MLOps**
• Docker
• Git
• GitHub
• GitHub Actions
• Railway
• MLflow

**API Endpoint**
Home Endpoint
```
GET /
```
**Returns**
```
Sales Prediction API Running Successfully
```
**Prediction Endpoint**
```
POST /predict
```
**Input Format**
```json
{
  "city": "...",
  "state": "...",
  "category": "...",
  "product": "...",
  "payment_mode": "...",
  "salesperson": "...",
  "quantity": 0,
  "unit_price": 0,
  "discount": 0,
  "sales": 0,
  "cost": 0
}
```
**Response**
```json
{
    "Predicted Profit": 25925.05
}
```

**MLflow**

The project uses MLflow to:
• Track machine learning experiments
• Compare multiple models
• Store parameters
• Record evaluation metrics
• Monitor model performance

**Key Features**
• End-to-End Machine Learning Pipeline
• Data Cleaning and Feature Engineering
• Multiple Model Comparison
• Automated Model Selection
• REST API using Flask
• Dockerized Application
• Cloud Deployment
• MLflow Experiment Tracking
• GitHub Version Control
• CI Workflow Integration

**Learning Outcomes**
Through this project, the following concepts were implemented and understood:
• Data preprocessing
• Feature engineering
• Machine learning model training
• Model evaluation
• Model serialization
• REST API development
• Docker containerization
• Cloud deployment
• Version control using Git
• CI workflow
• Experiment tracking using MLflow
• Production-ready project structure

**Future Improvements**
• Model Registry
• Automated Retraining
• Data Validation
• Monitoring Dashboard
• Unit Testing
• Kubernetes Deployment
• AWS Deployment
• CI/CD Pipeline Enhancement

**POW (proof of work)**

**Application deployment**
<img width="1885" height="858" alt="Screenshot 2026-08-04 184045" src="https://github.com/user-attachments/assets/ca9d10b3-8f47-4282-ae35-ed8602885167" />
**Mlflow**
<img width="1892" height="901" alt="Screenshot 2026-08-04 184108" src="https://github.com/user-attachments/assets/70121899-a00a-4298-8d53-1da3342cf290" />
**Docker containers / images**
<img width="1917" height="1021" alt="image" src="https://github.com/user-attachments/assets/cc889245-adc4-4794-8fe0-04d0ff930186" />



**Author
Shrikrushna Dhebe**

**Skills**
Python | Automation | Data Analysis | Machine Learning | MLOps | Data Science | GEN AI | Deep learning | Machine learning |

**License**
This project is developed for educational, portfolio, and learning purposes.
