<div align="center">

# 🏦 Loan Approval Prediction System

### 🚀 Machine Learning Project using Logistic Regression & Streamlit

<p align="center">
<img src="https://img.shields.io/badge/Python-3.11.9-blue?style=for-the-badge&logo=python">
<img src="https://img.shields.io/badge/Scikit--Learn-ML-orange?style=for-the-badge&logo=scikitlearn">
<img src="https://img.shields.io/badge/Streamlit-WebApp-red?style=for-the-badge&logo=streamlit">
<img src="https://img.shields.io/badge/Status-Completed-success?style=for-the-badge">
<img src="https://img.shields.io/badge/License-MIT-green?style=for-the-badge">
</p>

---

### 💡 Predict whether a loan application will be **Approved ✅** or **Rejected ❌** using Machine Learning.

</div>

---

# 📖 Table of Contents

- 🎯 Project Overview
- ✨ Features
- 📊 Dataset
- ⚙️ Machine Learning Workflow
- 🧠 Model Used
- 🛠 Technologies
- 📂 Project Structure
- 🚀 Installation
- 💻 Running the Project
- 📸 Application Preview
- 📈 Model Performance
- 🧪 Sample Test Case
- 🔮 Future Improvements
- 👨‍💻 Author

---

# 🎯 Project Overview

The **Loan Approval Prediction System** is a Machine Learning web application that predicts whether a customer's loan application is likely to be approved.

The application takes multiple applicant details as input and instantly predicts the loan status using a trained **Logistic Regression** model.

---

# ✨ Features

✅ Interactive Streamlit UI

✅ Real-time Loan Prediction

✅ Prediction Confidence Score

✅ Clean and Responsive Interface

✅ Machine Learning Classification

✅ Easy to Use

---

# 📊 Dataset Information

The dataset contains **614 loan records** with **11 input features**.

| Feature | Description |
|----------|-------------|
| Gender | Male / Female |
| Married | Yes / No |
| Dependents | Number of Dependents |
| Education | Graduate / Not Graduate |
| Self Employed | Yes / No |
| Applicant Income | Monthly Income |
| Coapplicant Income | Monthly Co-Income |
| Loan Amount | Requested Loan Amount |
| Loan Amount Term | Loan Duration (Months) |
| Credit History | Good / Bad |
| Property Area | Rural / Semiurban / Urban |

🎯 Target Variable

```
Loan_Status
```

- **1 → Approved**
- **0 → Rejected**

---

# ⚙️ Machine Learning Workflow

```text
📂 Dataset
      │
      ▼
🧹 Data Cleaning
      │
      ▼
🏷 Label Encoding
      │
      ▼
📊 Exploratory Data Analysis
      │
      ▼
✂ Train Test Split
      │
      ▼
🤖 Logistic Regression
      │
      ▼
📈 Model Evaluation
      │
      ▼
💾 Save Model (.pkl)
      │
      ▼
🌐 Streamlit Deployment
```

---

# 🧹 Data Preprocessing

✔ Missing Value Handling

✔ Duplicate Removal

✔ Label Encoding

✔ Feature Selection

✔ Train-Test Split

---

# 🤖 Model Used

| Algorithm | Purpose |
|------------|----------|
| Logistic Regression | Classification |

```python
from sklearn.linear_model import LogisticRegression

model = LogisticRegression(max_iter=1000)

model.fit(x_train,y_train)
```

---

# 📈 Model Performance

| Metric | Score |
|----------|---------|
| Accuracy | **78.86%** |

---

# 🛠 Technologies Used

| Technology | Purpose |
|------------|----------|
| 🐍 Python | Programming |
| 📊 Pandas | Data Processing |
| 🔢 NumPy | Numerical Operations |
| 📉 Matplotlib | Visualization |
| 🤖 Scikit-Learn | Machine Learning |
| 💾 Joblib | Model Saving |
| 🌐 Streamlit | Web Application |

---

# 📂 Project Structure

```
Loan-Approval-Predictor
│
├── app.py
├── loan_model.pkl
├── train.csv
├── requirements.txt
├── README.md
│
└── notebooks/
      └── Loan_Approval.ipynb
```

---

# 🚀 Installation

### Clone Repository

```bash
git clone https://github.com/yourusername/Loan-Approval-Predictor.git
```

### Go to Project Folder

```bash
cd Loan-Approval-Predictor
```

### Install Dependencies

```bash
pip install -r requirements.txt
```

### Run Streamlit

```bash
streamlit run app.py
```

---

# 📸 Application Features

### 🏦 Applicant Details

✔ Gender

✔ Marital Status

✔ Dependents

✔ Education

✔ Self Employment

✔ Applicant Income

✔ Coapplicant Income

✔ Loan Amount

✔ Loan Amount Term

✔ Credit History

✔ Property Area

---

# 🎉 Output

The application predicts

```
✅ Loan Approved
```

or

```
❌ Loan Rejected
```

along with

```
Prediction Confidence
```

---

# 🧪 Sample Test Case

| Input | Value |
|--------|-------|
| Gender | Male |
| Married | Yes |
| Dependents | 0 |
| Education | Graduate |
| Self Employed | No |
| Applicant Income | 6000 |
| Coapplicant Income | 2250 |
| Loan Amount | 265 |
| Loan Term | 360 |
| Credit History | Good |
| Property Area | Semiurban |

### Prediction

```
✅ Loan Approved

Confidence : 79.76%
```

---

# 📊 Workflow Diagram

```text
          User Input
               │
               ▼
      Streamlit Interface
               │
               ▼
     Data Preprocessing
               │
               ▼
   Logistic Regression Model
               │
               ▼
 Loan Approved / Rejected
               │
               ▼
     Prediction Confidence
```

---

# 🔮 Future Enhancements

- 🌲 Random Forest Classifier
- 🚀 XGBoost Classifier
- ☁ Deploy on Streamlit Cloud
- 📊 Dashboard Analytics
- 📱 Mobile Responsive UI
- 📄 Download Prediction Report

---

# ⭐ Project Highlights

🏆 Machine Learning Classification Project

🏆 Interactive Web Application

🏆 Real-Time Predictions

🏆 Beginner Friendly

🏆 Clean UI

🏆 End-to-End ML Pipeline

---

# 👨‍💻 Author

## Abdullah Ahmed Khan

**Computer Science Engineering**

Machine Learning • Data Science • Python • Streamlit

---

<div align="center">

### ⭐ If you like this project, don't forget to Star ⭐ the repository!

Made with ❤️ using Python, Scikit-Learn & Streamlit

</div>
