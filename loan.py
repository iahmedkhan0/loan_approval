import streamlit as st
import numpy as np
import joblib

# -------------------------------
# Page Configuration
# -------------------------------
st.set_page_config(
    page_title="🏦 Loan Approval Predictor",
    page_icon="💳",
    layout="wide",
    initial_sidebar_state="expanded"
)

# -------------------------------
# Load Model
# -------------------------------
loan_model = joblib.load("loan_model.pkl")

# -------------------------------
# Premium CSS
# -------------------------------
st.markdown("""
<style>

@import url('https://fonts.googleapis.com/css2?family=Poppins:wght@300;400;500;600;700;800&display=swap');

html, body, [class*="css"]{
    font-family:'Poppins',sans-serif;
}

/* Background */
.stApp{
background:
linear-gradient(135deg,#0F2027,#203A43,#2C5364);
background-size:400% 400%;
animation:bgMove 15s ease infinite;
}

@keyframes bgMove{
0%{background-position:0% 50%;}
50%{background-position:100% 50%;}
100%{background-position:0% 50%;}
}

/* Hide Streamlit branding */
#MainMenu{visibility:hidden;}
footer{visibility:hidden;}
header{visibility:hidden;}

/* Hero */
.hero{
padding:35px;
border-radius:28px;
background:rgba(255,255,255,0.08);
backdrop-filter:blur(15px);
border:1px solid rgba(255,255,255,.2);
box-shadow:0 8px 32px rgba(0,0,0,.35);
margin-bottom:25px;
}

.hero h1{
font-size:48px;
color:white;
font-weight:800;
margin-bottom:5px;
}

.hero p{
font-size:18px;
color:#E5E7EB;
}

/* Cards */

.metric-card{
background:rgba(255,255,255,.09);
border-radius:22px;
padding:25px;
text-align:center;
backdrop-filter:blur(15px);
border:1px solid rgba(255,255,255,.2);
transition:.4s;
margin-bottom:15px;
}

.metric-card:hover{
transform:translateY(-6px);
box-shadow:0 15px 40px rgba(0,255,255,.2);
}

.metric-value{
font-size:34px;
font-weight:700;
color:#00FFD1;
}

.metric-title{
font-size:16px;
color:white;
margin-top:8px;
}

/* Input Containers */

.block-container{
padding-top:2rem;
padding-bottom:2rem;
}

/* Sidebar */

section[data-testid="stSidebar"]{
background:linear-gradient(180deg,#1A1A2E,#16213E);
}

section[data-testid="stSidebar"] h1,
section[data-testid="stSidebar"] h2,
section[data-testid="stSidebar"] h3,
section[data-testid="stSidebar"] p{
color:white;
}

/* Buttons */

.stButton>button{
width:100%;
padding:18px;
font-size:20px;
font-weight:700;
border-radius:18px;
border:none;
background:linear-gradient(90deg,#00F5A0,#00D9F5);
color:#111;
transition:.4s;
}

.stButton>button:hover{
transform:scale(1.03);
box-shadow:0 0 25px cyan;
}

/* Inputs */

.stSelectbox div[data-baseweb="select"],
.stNumberInput input{

border-radius:15px !important;

}

hr{
border:1px solid rgba(255,255,255,.2);
}

</style>
""", unsafe_allow_html=True)

# -------------------------------
# Sidebar
# -------------------------------
with st.sidebar:

    st.image("https://cdn-icons-png.flaticon.com/512/3135/3135706.png", width=120)

    st.markdown("## 💳 Loan Predictor")

    st.write("""
Predict whether a loan application
will be approved using Machine Learning.

---

### 📌 Model
Logistic Regression

### 🧠 Features
- Real-time Prediction
- Confidence Score
- Interactive Dashboard
- Streamlit UI

---

Made with ❤️ in Python
""")

# -------------------------------
# Hero Banner
# -------------------------------
st.markdown("""
<div class="hero">

<h1>🏦 Loan Approval Prediction</h1>

<p>
Smart Financial Decisions powered by Machine Learning.
Instantly analyze applicant information and estimate
loan approval probability with an elegant dashboard.
</p>

</div>
""", unsafe_allow_html=True)

# -------------------------------
# Dashboard Cards
# -------------------------------
c1,c2,c3,c4=st.columns(4)

with c1:
    st.markdown("""
<div class="metric-card">
<div class="metric-value">614</div>
<div class="metric-title">Applications</div>
</div>
""",unsafe_allow_html=True)

with c2:
    st.markdown("""
<div class="metric-card">
<div class="metric-value">11</div>
<div class="metric-title">Features</div>
</div>
""",unsafe_allow_html=True)

with c3:
    st.markdown("""
<div class="metric-card">
<div class="metric-value">78.86%</div>
<div class="metric-title">Accuracy</div>
</div>
""",unsafe_allow_html=True)

with c4:
    st.markdown("""
<div class="metric-card">
<div class="metric-value">⚡</div>
<div class="metric-title">Instant Prediction</div>
</div>
""",unsafe_allow_html=True)

st.markdown("<br>",unsafe_allow_html=True)
# ==========================================================
# APPLICANT DETAILS
# ==========================================================

st.markdown("""
<h2 style='color:white;text-align:center;margin-bottom:20px;'>
👤 Applicant Information
</h2>
""", unsafe_allow_html=True)

left, right = st.columns(2, gap="large")

with left:

    st.markdown("### 🧑 Personal Details")

    gender = st.selectbox(
        "👨 Gender",
        ["Male", "Female"]
    )

    married = st.selectbox(
        "💍 Marital Status",
        ["Yes", "No"]
    )

    dependents = st.selectbox(
        "👨‍👩‍👧 Dependents",
        ["0", "1", "2", "3+"]
    )

    education = st.selectbox(
        "🎓 Education",
        ["Graduate", "Not Graduate"]
    )

    self_employed = st.selectbox(
        "💼 Self Employed",
        ["No", "Yes"]
    )


with right:

    st.markdown("### 💰 Financial Details")

    applicant_income = st.number_input(
        "💵 Applicant Income",
        min_value=0,
        value=5000,
        step=500
    )

    coapplicant_income = st.number_input(
        "👨‍👩‍👧 Coapplicant Income",
        min_value=0,
        value=0,
        step=500
    )

    loan_amount = st.number_input(
        "🏦 Loan Amount",
        min_value=0,
        value=150,
        step=10
    )

    loan_term = st.selectbox(
        "📅 Loan Term (Months)",
        [12,36,60,84,120,180,240,300,360]
    )

    credit_history = st.selectbox(
        "📈 Credit History",
        ["Good","Bad"]
    )

    property_area = st.selectbox(
        "🏠 Property Area",
        ["Rural","Semiurban","Urban"]
    )

st.markdown("<br>", unsafe_allow_html=True)

# ==========================================================
# SUMMARY DASHBOARD
# ==========================================================

st.markdown("""
<h2 style='color:white;text-align:center;'>
📊 Quick Overview
</h2>
""", unsafe_allow_html=True)

a,b,c = st.columns(3)

with a:
    st.metric(
        label="💰 Income",
        value=f"${applicant_income:,.0f}"
    )

with b:
    st.metric(
        label="🏦 Loan",
        value=f"${loan_amount:,.0f}"
    )

with c:

    if applicant_income>0:
        ratio=(loan_amount/applicant_income)*100
    else:
        ratio=0

    st.metric(
        label="📈 Loan / Income",
        value=f"{ratio:.1f}%"
    )

st.markdown("<br>", unsafe_allow_html=True)

st.markdown("""
<div style="
background:rgba(255,255,255,.08);
padding:18px;
border-radius:18px;
border:1px solid rgba(255,255,255,.2);
">

<h3 style="color:#00FFD1;">
💡 Smart Banking Tip
</h3>

<p style="color:white;font-size:17px;">
Applicants with a <b>Good Credit History</b>,
stable income, and a moderate loan amount generally
have a higher probability of loan approval.
</p>

</div>
""", unsafe_allow_html=True)

st.markdown("<br>", unsafe_allow_html=True)

predict = st.button(
    "🚀 Predict Loan Approval"
)
# ==========================================================
# PREDICTION
# ==========================================================

if predict:

    # -----------------------------
    # Encode Inputs
    # -----------------------------
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

    confidence = max(probability[0]) * 100

    st.markdown("<br>", unsafe_allow_html=True)

    st.markdown("---")

    st.markdown(
        "<h2 style='text-align:center;color:white;'>📋 Prediction Report</h2>",
        unsafe_allow_html=True,
    )

    col1, col2 = st.columns([2, 1])

    # ====================================================
    # RESULT
    # ====================================================

    with col1:

        if prediction[0] == 1:

            st.balloons()

            st.markdown(
                """
                <div style="
                background:linear-gradient(135deg,#00C853,#69F0AE);
                padding:30px;
                border-radius:25px;
                text-align:center;
                box-shadow:0px 0px 35px rgba(0,255,120,.45);
                ">
                <h1 style="color:white;">✅ LOAN APPROVED</h1>
                <h3 style="color:white;">
                Congratulations! Your application has a high probability of approval.
                </h3>
                </div>
                """,
                unsafe_allow_html=True,
            )

        else:

            st.markdown(
                """
                <div style="
                background:linear-gradient(135deg,#D50000,#FF5252);
                padding:30px;
                border-radius:25px;
                text-align:center;
                box-shadow:0px 0px 35px rgba(255,0,0,.35);
                ">
                <h1 style="color:white;">❌ LOAN REJECTED</h1>
                <h3 style="color:white;">
                The current application has a lower probability of approval.
                </h3>
                </div>
                """,
                unsafe_allow_html=True,
            )

        st.markdown("<br>", unsafe_allow_html=True)

        st.progress(confidence / 100)

        st.success(f"Prediction Confidence : {confidence:.2f}%")

    # ====================================================
    # SIDE PANEL
    # ====================================================

    with col2:

        st.metric(
            "💰 Applicant Income",
            f"${applicant_income:,.0f}",
        )

        st.metric(
            "🏦 Loan Amount",
            f"${loan_amount:,.0f}",
        )

        st.metric(
            "📅 Loan Term",
            f"{loan_term} Months",
        )

        st.metric(
            "📈 Confidence",
            f"{confidence:.1f}%",
        )

    st.markdown("<br>", unsafe_allow_html=True)

    # ====================================================
    # APPLICATION SUMMARY
    # ====================================================

    with st.expander("📄 View Submitted Application"):

        st.write("### Personal Details")

        st.write(f"**Gender:** {'Male' if gender==1 else 'Female'}")
        st.write(f"**Married:** {'Yes' if married==1 else 'No'}")
        st.write(f"**Dependents:** {dependents}")
        st.write(f"**Education:** {'Graduate' if education==0 else 'Not Graduate'}")
        st.write(f"**Self Employed:** {'Yes' if self_employed==1 else 'No'}")

        st.divider()

        st.write("### Financial Details")

        st.write(f"Applicant Income : ${applicant_income:,.0f}")
        st.write(f"Coapplicant Income : ${coapplicant_income:,.0f}")
        st.write(f"Loan Amount : ${loan_amount:,.0f}")
        st.write(f"Loan Term : {loan_term} Months")

        st.write(
            f"Credit History : {'Good' if credit_history==1 else 'Bad'}"
        )

    st.markdown("<br>", unsafe_allow_html=True)

    # ====================================================
    # SMART TIPS
    # ====================================================

    st.markdown(
        "<h3 style='color:white;'>💡 Tips to Improve Loan Approval</h3>",
        unsafe_allow_html=True,
    )

    tips = []

    if credit_history == 0:
        tips.append("✔ Improve your credit history.")

    if applicant_income < 4000:
        tips.append("✔ Higher income generally improves eligibility.")

    if loan_amount > applicant_income:
        tips.append("✔ Consider applying for a smaller loan amount.")

    if self_employed == 1:
        tips.append("✔ Maintain stable income documentation.")

    if len(tips) == 0:
        tips.append("🎉 Your application already satisfies the major eligibility factors!")

    for tip in tips:
        st.info(tip)

    st.markdown("<br>", unsafe_allow_html=True)

    st.markdown("---")

    st.markdown(
        """
        <div style='text-align:center;color:lightgray;'>

        <h3>🏦 Loan Approval Prediction System</h3>

        Built with ❤️ using

        <b>Python • Streamlit • Scikit-learn • Logistic Regression</b>

        </div>
        """,
        unsafe_allow_html=True,
    )