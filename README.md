# delivery-time-prediction
# 🚚 Delivery Time Prediction System

## 📌 Overview
This project predicts delivery time based on factors like distance, traffic, and order details.  
It is an end-to-end Machine Learning system with API deployment and frontend UI.

---

## 🚀 Features
- 📊 Exploratory Data Analysis (EDA)
- 🧠 Feature Engineering (traffic, time-based patterns)
- 🤖 Random Forest Regression Model
- 🌐 FastAPI backend for real-time prediction
- 🎨 Interactive frontend UI

---

## 🛠️ Tech Stack
- Python (Pandas, NumPy, Scikit-learn)
- FastAPI
- HTML, CSS, JavaScript

---

## 📊 Model Performance
- MAE: ~8.48 minutes
- RMSE: ~10.14 minutes

---

## ▶️ How to Run

### 1. Install dependencies
```bash
pip install fastapi uvicorn pandas numpy scikit-learn joblib
Run backend
cd api
uvicorn main:app --reload
