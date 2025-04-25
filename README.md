# 📉 Customer Churn Prediction App

A simple and interactive web application that predicts whether a telecom customer is likely to churn, based on their service usage patterns and personal profile.

Built with **Streamlit**, powered by a trained **Logistic Regression model**, and deployed with **Streamlit Cloud**.

---

## 🚀 Live Demo

👉 [Click here to try the app](https://customer-churn-pred-app.streamlit.app)  

---

## 🔍 Features

- 📊 Predicts customer churn based on:
  - Tenure, monthly charges, total services
  - Internet & phone services
  - Contract type, payment method, and more
- ✅ Clean, user-friendly interface
- ⚙️ All preprocessing (label encoding, one-hot, scaling) handled automatically
- 🧠 Model trained on the [Telco Customer Churn dataset](https://www.kaggle.com/blastchar/telco-customer-churn)

---

## 🛠 Tech Stack

- Python
- Streamlit
- Scikit-learn
- XGBoost
- Pandas, NumPy
- Joblib (for model persistence)

---

## 📁 Project Structure
```plaintext
├── app.py                 # Streamlit UI
├── predict.py             # Preprocessing + prediction logic
├── logistic_model.pkl     # Saved Logistic Regression model
├── scaler.pkl             # Saved MinMaxScaler
├── requirements.txt       # Dependencies for deployment
└── .gitignore
```

---

## 🧠 Model Info

- Type: Logistic Regression
- Preprocessing: Label Encoding, One-Hot Encoding, Scaling
- Accuracy: ~80%
- Balanced with: `class_weight='balanced'`

---

## 📦 Setup Instructions (for local dev)

```bash
git clone https://github.com/amandesai59/Customer-Churn-Prediction.git
cd Customer-Churn-Prediction
pip install -r requirements.txt
streamlit run app.py
```

## ✨ Screenshot
![image](https://github.com/user-attachments/assets/d40a7133-2a58-4dac-b4ed-d34e9865b2e6)

## 🙌 Credits
Inspired by projects from the Kaggle community.
