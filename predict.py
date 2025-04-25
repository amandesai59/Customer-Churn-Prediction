#!/usr/bin/env python
# coding: utf-8

# In[16]:


import joblib
import numpy as np
import pandas as pd


# In[17]:


model = joblib.load('logistic_model.pkl')
scaler = joblib.load('scaler.pkl')


# In[22]:


def preprocess_input(user_input):
    # Binary label encoding map
    label_map = {'no': 0, 'yes': 1, 'female': 0, 'male': 1}
    payment_map = {
    'bank transfer (automatic)': 0,
    'credit card (automatic)': 1,
    'electronic check': 2,
    'mailed check': 3
    }

    # One-hot encode InternetService
    internet_cats = ['Fiber optic', 'No']
    internet_encoded = [1 if user_input['InternetService'] == cat else 0 for cat in internet_cats]

    # One-hot encode Contract
    contract_cats = ['One year', 'Two year']
    contract_encoded = [1 if user_input['Contract'] == cat else 0 for cat in contract_cats]

    # Build feature vector
    feature_row = [
        label_map[user_input['gender'].strip().lower()],
        int(user_input['SeniorCitizen']),
        label_map[user_input['Partner'].strip().lower()],
        label_map[user_input['Dependents'].strip().lower()],
        int(user_input['tenure']),
        label_map[user_input['PhoneService'].strip().lower()],
        label_map[user_input['MultipleLines'].strip().lower()],
        label_map[user_input['OnlineSecurity'].strip().lower()],
        label_map[user_input['OnlineBackup'].strip().lower()],
        label_map[user_input['DeviceProtection'].strip().lower()],
        label_map[user_input['TechSupport'].strip().lower()],
        label_map[user_input['StreamingTV'].strip().lower()],
        label_map[user_input['StreamingMovies'].strip().lower()],
        label_map[user_input['PaperlessBilling'].strip().lower()],
        payment_map[user_input['PaymentMethod'].strip().lower()],
        float(user_input['MonthlyCharges']),
        float(user_input['TotalCharges']),
        *internet_encoded,
        *contract_encoded
    ]

    input_array = np.array([feature_row])
    input_df = pd.DataFrame(input_array, columns=scaler.feature_names_in_)
    input_scaled = scaler.transform(input_df)
    return input_scaled


# In[23]:


def predict_churn(user_input):
    processed = preprocess_input(user_input)
    prediction = model.predict(processed)[0]
    return "Churn" if prediction == 1 else "No Churn"


# In[33]:


sample_input = {
    'gender': 'Female',
    'SeniorCitizen': 0,
    'Partner': 'Yes',
    'Dependents': 'Yes',
    'tenure': 60,
    'PhoneService': 'Yes',
    'MultipleLines': 'Yes',
    'OnlineSecurity': 'Yes',
    'OnlineBackup': 'Yes',
    'DeviceProtection': 'Yes',
    'TechSupport': 'Yes',
    'StreamingTV': 'Yes',
    'StreamingMovies': 'Yes',
    'PaperlessBilling': 'No',
    'PaymentMethod': 'Bank transfer (automatic)',  # label encoded = 0
    'MonthlyCharges': 55.2,
    'TotalCharges': 3300.0,
    'InternetService': 'DSL',
    'Contract': 'Two year'
}
predict_churn(sample_input)


# In[ ]:




