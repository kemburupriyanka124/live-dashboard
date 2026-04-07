import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt

# -------------------------------
# Page Configuration
# -------------------------------
st.set_page_config(page_title="Climate Change Agriculture Dashboard", layout="wide")

# -------------------------------
# Title
# -------------------------------
st.title("🌱 Climate Change Impact on Agriculture Dashboard")

# -------------------------------
# Load Dataset
# -------------------------------
data = pd.read_csv("climate_change_impact_on_agriculture_2024.csv")

# -------------------------------
# Handle Missing Values
# -------------------------------
for col in data.columns:
    if data[col].dtype == "object":
        data[col] = data[col].fillna(data[col].mode()[0])
    else:
        data[col] = data[col].fillna(data[col].median())

# -------------------------------
# Dataset Preview
# -------------------------------
st.subheader("📄 Dataset Preview")
st.dataframe(data.head())

# -------------------------------
# Dataset Information
# -------------------------------
st.subheader("📌 Dataset Shape")
st.write("Rows:", data.shape[0])
st.write("Columns:", data.shape[1])

# -------------------------------
# Numeric Columns
# -------------------------------
numeric_cols = data.select_dtypes(include=['number']).columns

if len(numeric_cols) > 0:

    selected_col = st.selectbox("Select Numeric Column", numeric_cols)

    # -------------------------------
    # Statistics
    # -------------------------------
    st.subheader("📈 Statistics")
    st.write(data[selected_col].describe())

    # -------------------------------
    # Histogram
    # -------------------------------
    st.subheader("📊 Histogram")

    fig, ax = plt.subplots()
    ax.hist(data[selected_col], bins=20)
    ax.set_xlabel(selected_col)
    ax.set_ylabel("Frequency")

    st.pyplot(fig)

# -------------------------------
# Correlation Matrix
# -------------------------------
if len(numeric_cols) > 1:
    st.subheader("🔗 Correlation Matrix")
    st.dataframe(data[numeric_cols].corr())

# -------------------------------
# Column-wise Missing Values
# -------------------------------
st.subheader("⚠ Missing Values")
st.write(data.isnull().sum())

# -------------------------------
# Footer
# -------------------------------
st.success("Dashboard loaded successfully ✅")
