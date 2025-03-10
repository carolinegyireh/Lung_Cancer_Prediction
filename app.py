import streamlit as st
import joblib
import numpy as np

# ✅ Ensure this is the very first Streamlit command
st.set_page_config(page_title="MultiDiPredXpert", layout="centered", initial_sidebar_state="expanded")

# Now proceed with the rest of your imports and code...
st.markdown("""
    <style>
        body {
            background-color: #f9f9f9;
            font-family: 'Arial', sans-serif;
        }
        .title {
            color: #FF69B4;  /* Cancer Awareness Color */
            text-align: center;
            font-size: 3rem;
            margin-bottom: 20px;
        }
        .stButton>button {
            background-color: #FF4B4B;
            color: white;
            font-size: 16px;
            font-weight: bold;
            border-radius: 8px;
            padding: 10px 20px;
            margin-top: 20px;
        }
        .stButton>button:hover {
            background-color: #FF1A1A;
        }
    </style>
""", unsafe_allow_html=True)

# Load saved model
rf_model = joblib.load("models/xgboost_model.pkl")

# Function to make predictions
def predict_disease(features):
    features = np.array(features).reshape(1, -1)
    prediction = rf_model.predict(features)[0]
    return "🛑 Disease Detected ✅" if prediction == 1 else "✅ No Disease ❌"

# UI Components
st.markdown('<h1 class="title">🩺 Lung Cancer Predictor</h1>', unsafe_allow_html=True)
st.write("### Enter patient details to predict disease presence.")

# Create a container to hold the form and predictions
with st.container():
    # Form Layout
    col1, col2 = st.columns(2)

    with col1:
        age = st.number_input("📌 Age", min_value=0, max_value=120, value=30)
        gender = st.selectbox("📌 Gender", ["Male", "Female"], help="Select the gender of the patient.")
        smoker = st.selectbox("📌 Smoker", ["Yes", "No"], help="Have you ever smoked cigarettes regularly?")
        years_of_smoking = st.number_input("📌 Years of Smoking", min_value=0, value=5)
        cigarettes_per_day = st.number_input("📌 Cigarettes per Day", min_value=0, value=10)
        passive_smoker = st.selectbox("📌 Passive Smoker", ["Yes", "No"], help="Are you exposed to second-hand smoke?")
        family_history = st.selectbox("📌 Family History", ["Yes", "No"], help="Does anyone in your family have a history of lung cancer?")

    with col2:
        adenocarcinoma_type = st.selectbox("📌 Adenocarcinoma Type", ["Yes", "No"], help="Do you have adenocarcinoma?")
        air_pollution_exposure_low = st.selectbox("📌 Low Air Pollution Exposure", ["Yes", "No"], help="Have you been exposed to low levels of air pollution?")
        air_pollution_exposure_medium = st.selectbox("📌 Medium Air Pollution Exposure", ["Yes", "No"], help="Have you been exposed to medium levels of air pollution?")
        occupational_exposure = st.selectbox("📌 Occupational Exposure", ["Yes", "No"], help="Do you work in an environment with harmful substances?")
        indoor_pollution = st.selectbox("📌 Indoor Pollution", ["Yes", "No"], help="Are you exposed to indoor pollution?")
        healthcare_access_poor = st.selectbox("📌 Poor Healthcare Access", ["Yes", "No"], help="Do you have limited access to healthcare?")
        early_detection = st.selectbox("📌 Early Detection", ["Yes", "No"], help="Have you undergone early detection screenings?")

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

    # Predict button with style
    if st.button("🔍 Predict Now"):
        result = predict_disease(input_features)
        st.success(result)

# Disclaimer
st.markdown("⚕️ **Disclaimer:** This tool is for educational purposes only. Consult a doctor for medical advice.")
