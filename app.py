import streamlit as st
import joblib
import numpy as np

# Load saved models
rf_model = joblib.load("models/xgboost_model.pkl")

# Function to make predictions
def predict_disease(features):
    features = np.array(features).reshape(1, -1)
    prediction = rf_model.predict(features)[0]
    return prediction

# Streamlit UI configuration
st.set_page_config(page_title="MultiDiPredXpert", layout="centered")

# Title and introductory text
st.title("🩺 Lung Cancer Predictor")
st.write("### Enter patient details to predict disease presence.")
st.write("---")

# Create two columns for a better layout
col1, col2 = st.columns(2)

with col1:
    age = st.number_input("📌 **Age**", min_value=0, max_value=120, value=30)
    gender = st.selectbox("📌 **Gender**", ["Male", "Female"])
    smoker = st.selectbox("📌 **Smoker**", ["Yes", "No"])
    years_of_smoking = st.number_input("📌 **Years of Smoking**", min_value=0, value=5)

with col2:
    passive_smoker = st.selectbox("📌 **Passive Smoker**", ["Yes", "No"])
    family_history = st.selectbox("📌 **Family History**", ["Yes", "No"])
    adenocarcinoma_type = st.selectbox("📌 **Adenocarcinoma Type**", ["Yes", "No"])
    air_pollution_exposure_low = st.selectbox("📌 **Low Air Pollution Exposure**", ["Yes", "No"])

# Convert categorical features to numerical values for the model
gender = 1 if gender == "Male" else 0
smoker = 1 if smoker == "Yes" else 0
passive_smoker = 1 if passive_smoker == "Yes" else 0
family_history = 1 if family_history == "Yes" else 0
adenocarcinoma_type = 1 if adenocarcinoma_type == "Yes" else 0
air_pollution_exposure_low = 1 if air_pollution_exposure_low == "Yes" else 0

# Collect input features
input_features = [
    age, gender, smoker, years_of_smoking, passive_smoker, family_history,
    adenocarcinoma_type, air_pollution_exposure_low
]

# Predict button with style
if st.button("🔍 Predict Now"):
    result = predict_disease(input_features)
    if result == 1:
        st.markdown('<h2 style="color: red;">🛑 Disease Detected ✅</h2>', unsafe_allow_html=True)
    else:
        st.markdown('<h2 style="color: green;">✅ No Disease ❌</h2>', unsafe_allow_html=True)

# Disclaimer
st.write("---")
st.markdown("⚕️ **Disclaimer:** This tool is for educational purposes only. Please consult a doctor for medical advice.")
