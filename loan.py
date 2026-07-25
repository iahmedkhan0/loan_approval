import streamlit as st
import numpy as np
import joblib

# Load Model
loan_model = joblib.load("loan_model.pkl")

# Page Configuration
st.set_page_config(
    page_title="Loan Approval Predictor",
    page_icon="🏦",
    layout="centered"
)

st.title("🏦 Loan Approval Predictor")
st.write("Enter Applicant Details")
st.divider()

# Gender
gender = st.selectbox(
    "Gender",
    ["Male", "Female"]
)

# Married
married = st.selectbox(
    "Marital Status",
    ["Yes", "No"]
)

# Dependents
dependents = st.selectbox(
    "Dependents",
    ["0", "1", "2", "3+"]
)

# Education
education = st.selectbox(
    "Education",
    ["Graduate", "Not Graduate"]
)

# Self Employed
self_employed = st.selectbox(
    "Self Employed",
    ["No", "Yes"]
)

st.divider()

# Income Details
applicant_income = st.number_input(
    "Applicant Income",
    min_value=0
)

coapplicant_income = st.number_input(
    "Coapplicant Income",
    min_value=0
)

loan_amount = st.number_input(
    "Loan Amount",
    min_value=0
)

loan_term = st.selectbox(
    "Loan Amount Term (Months)",
    [12, 36, 60, 84, 120, 180, 240, 300, 360]
)

credit_history = st.selectbox(
    "Credit History",
    ["Good", "Bad"]
)

property_area = st.selectbox(
    "Property Area",
    ["Rural", "Semiurban", "Urban"]
)

st.divider()

if st.button("Predict Loan Status"):

    # Encode Inputs
    gender = 1 if gender == "Male" else 0
    married = 1 if married == "Yes" else 0

    dep_map = {
        "0": 0,
        "1": 1,
        "2": 2,
        "3+": 3
    }
    dependents = dep_map[dependents]

    education = 0 if education == "Graduate" else 1
    self_employed = 1 if self_employed == "Yes" else 0
    credit_history = 1 if credit_history == "Good" else 0

    property_map = {
        "Rural": 0,
        "Semiurban": 1,
        "Urban": 2
    }
    property_area = property_map[property_area]

    test = np.array([[
        gender,
        married,
        dependents,
        education,
        self_employed,
        applicant_income,
        coapplicant_income,
        loan_amount,
        loan_term,
        credit_history,
        property_area
    ]])

    prediction = loan_model.predict(test)
    probability = loan_model.predict_proba(test)

    st.divider()

    if prediction[0] == 1:
        st.success("✅ Loan Approved")
        st.info(f"Approval Confidence: **{probability[0][1]*100:.2f}%**")
    else:
        st.error("❌ Loan Rejected")
        st.warning(f"Rejection Confidence: **{probability[0][0]*100:.2f}%**")