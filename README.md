# 📱 Phone Usage Addiction Level Predictor

A machine learning web app that predicts a user's **smartphone addiction level** based on their daily phone usage patterns. Built with **Streamlit** for the frontend and **Logistic Regression** for the prediction model.

---

## 🔍 Overview

This project classifies users into different levels of phone addiction (Low, Moderate, High) using behavioral data such as screen time, sleep hours, and app usage. It was created to apply data science and machine learning skills and demonstrate a complete workflow from data preprocessing to deployment.

---

## 🎯 Features

- 📊 Input daily phone usage data manually
- 🤖 Predicts addiction level using a trained Logistic Regression model
- 💡 User-friendly result (instead of class numbers):
  - `Low Addiction`
  - `Moderate Addiction`
  - `High Addiction`
- ✅ Clean and modern Streamlit UI for a professional experience

---

## 🧠 Model Info

- **Model:** Logistic Regression (`multinomial`)
- **Preprocessing:**
  - StandardScaler for feature scaling
  - SMOTE for handling class imbalance
- **Evaluation:**
  - Accuracy on Test Set: **~100%**
  - Cross-validation Accuracy: **~99.8%**


---

## 🚀 How to Run Locally

### 1. Clone the repository


git clone https://github.com/Nafay-Aftab/phone-addiction-prediction.git
cd phone-addiction-prediction

### 2. Create and activate a virtual environment
python -m venv venv
## Activate on Windows
venv\Scripts\activate
## Or activate on macOS/Linux
source venv/bin/activate

#### 3. Install required packages
pip install -r requirements.txt

#### 4. Run the Streamlit app
streamlit run app.py


