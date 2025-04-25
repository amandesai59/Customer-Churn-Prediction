import streamlit as st
import joblib
import numpy as np
from predict import predict_churn

st.set_page_config(page_title="Churn Predictor", layout="centered")
st.title("📉 Customer Churn Prediction")

# --- UI Inputs ---
gender = st.selectbox("Gender", ["Female", "Male"])
senior = st.selectbox("Senior Citizen", [0, 1])
partner = st.selectbox("Partner", ["No", "Yes"])
dependents = st.selectbox("Dependents", ["No", "Yes"])
tenure = st.slider("Tenure (in months)", 0, 72, 12)
phone = st.selectbox("Phone Service", ["No", "Yes"])
multiple = st.selectbox("Multiple Lines", ["No", "Yes"])
online_sec = st.selectbox("Online Security", ["No", "Yes"])
online_backup = st.selectbox("Online Backup", ["No", "Yes"])
device_protection = st.selectbox("Device Protection", ["No", "Yes"])
tech_support = st.selectbox("Tech Support", ["No", "Yes"])
stream_tv = st.selectbox("Streaming TV", ["No", "Yes"])
stream_movies = st.selectbox("Streaming Movies", ["No", "Yes"])
paperless = st.selectbox("Paperless Billing", ["No", "Yes"])
payment_method = st.selectbox("Payment Method", [
    "Bank transfer (automatic)", 
    "Credit card (automatic)", 
    "Electronic check", 
    "Mailed check"
])
monthly_charges = st.number_input("Monthly Charges", value=70.0)
total_charges = st.number_input("Total Charges", value=1200.0)
internet_service = st.selectbox("Internet Service", ["DSL", "Fiber optic", "No"])
contract = st.selectbox("Contract Type", ["Month-to-month", "One year", "Two year"])

# --- Submit Button ---
if st.button("Predict"):
    input_data = {
        'gender': gender,
        'SeniorCitizen': senior,
        'Partner': partner,
        'Dependents': dependents,
        'tenure': tenure,
        'PhoneService': phone,
        'MultipleLines': multiple,
        'OnlineSecurity': online_sec,
        'OnlineBackup': online_backup,
        'DeviceProtection': device_protection,
        'TechSupport': tech_support,
        'StreamingTV': stream_tv,
        'StreamingMovies': stream_movies,
        'PaperlessBilling': paperless,
        'PaymentMethod': payment_method,
        'MonthlyCharges': monthly_charges,
        'TotalCharges': total_charges,
        'InternetService': internet_service,
        'Contract': contract
    }

    result = predict_churn(input_data)
    st.success(f"Prediction: **{result}**")