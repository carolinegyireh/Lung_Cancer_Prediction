import streamlit as st
import joblib
import numpy as np

# Streamlit UI configuration - Make sure this is the first Streamlit command
st.set_page_config(page_title="MultiDiPredXpert", layout="centered")

# Load saved models
rf_model = joblib.load("models/xgboost_model.pkl")

# Function to make predictions
def predict_disease(features):
    features = np.array(features).reshape(1, -1)
    prediction = rf_model.predict(features)[0]
    return "🛑 Disease Detected ✅" if prediction == 1 else "✅ No Disease ❌"

# Apply custom CSS for better design
st.markdown("""
    <style>
    .title {
        color: #4CAF50;
        font-size: 50px;
        font-weight: bold;
        text-align: center;
    }
    .subtitle {
        font-size: 20px;
        color: #555;
        text-align: center;
        margin-bottom: 20px;
    }
    .container {
        background-color: #f8f8f8;
        padding: 20px;
        border-radius: 10px;
        box-shadow: 0 4px 8px rgba(0, 0, 0, 0.1);
    }
    .input-section {
        margin-bottom: 20px;
    }
    .btn {
        background-color: #4CAF50;
        color: white;
        border: none;
        padding: 15px 32px;
        font-size: 16px;
        cursor: pointer;
        border-radius: 5px;
    }
    .btn:hover {
        background-color: #45a049;
    }
    </style>
""", unsafe_allow_html=True)

# Streamlit UI components
st.markdown('<div class="title">🩺 Lung Cancer Predictor</div>', unsafe_allow_html=True)
st.markdown('<div class="subtitle">Enter patient details to predict disease presence.</div>', unsafe_allow_html=True)

# Create columns for better layout
col1, col2 = st.columns(2)

with col1:
    age = st.number_input("📌 Age", min_value=0, max_value=120, value=30, step=1)
    gender = st.selectbox("📌 Gender", ["Male", "Female"])
    smoker = st.selectbox("📌 Smoker", ["Yes", "No"])
    years_of_smoking = st.number_input("📌 Years of Smoking", min_value=0, value=5, step=1)
    cigarettes_per_day = st.number_input("📌 Cigarettes per Day", min_value=0, value=10, step=1)
    passive_smoker = st.selectbox("📌 Passive Smoker", ["Yes", "No"])
    family_history = st.selectbox("📌 Family History", ["Yes", "No"])

with col2:
    adenocarcinoma_type = st.selectbox("📌 Adenocarcinoma Type", ["Yes", "No"])
    air_pollution_exposure_low = st.selectbox("📌 Low Air Pollution Exposure", ["Yes", "No"])
    air_pollution_exposure_medium = st.selectbox("📌 Medium Air Pollution Exposure", ["Yes", "No"])
    occupational_exposure = st.selectbox("📌 Occupational Exposure", ["Yes", "No"])
    indoor_pollution = st.selectbox("📌 Indoor Pollution", ["Yes", "No"])
    healthcare_access_poor = st.selectbox("📌 Poor Healthcare Access", ["Yes", "No"])
    early_detection = st.selectbox("📌 Early Detection", ["Yes", "No"])

# Convert categorical features to numerical values for the model
gender = 1 if gender == "Male" else 0
smoker = 1 if smoker == "Yes" else 0
passive_smoker = 1 if passive_smoker == "Yes" else 0
family_history = 1 if family_history == "Yes" else 0
adenocarcinoma_type = 1 if adenocarcinoma_type == "Yes" else 0
air_pollution_exposure_low = 1 if air_pollution_exposure_low == "Yes" else 0
air_pollution_exposure_medium = 1 if air_pollution_exposure_medium == "Yes" else 0
occupational_exposure = 1 if occupational_exposure == "Yes" else 0
indoor_pollution = 1 if indoor_pollution == "Yes" else 0
healthcare_access_poor = 1 if healthcare_access_poor == "Yes" else 0
early_detection = 1 if early_detection == "Yes" else 0

# Collect input features
input_features = [
    age, gender, smoker, years_of_smoking, cigarettes_per_day, passive_smoker,
    family_history, adenocarcinoma_type, air_pollution_exposure_low,
    air_pollution_exposure_medium, occupational_exposure, indoor_pollution,
    healthcare_access_poor, early_detection
]

# Add a button with custom style
if st.button("🔍 Predict Now", key="predict", help="Click to predict the disease presence.", use_container_width=True):
    result = predict_disease(input_features)
    st.success(result)

# Disclaimer section with a customized font
st.markdown("""
    <div style="text-align: center; font-size: 16px; color: #777;">
    ⚕️ **Disclaimer:** This tool is for educational purposes only. Consult a doctor for medical advice.
    </div>
""", unsafe_allow_html=True)
