import streamlit as st
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestRegressor
from sklearn.preprocessing import LabelEncoder
from sklearn.metrics import mean_absolute_error, r2_score

# Page Title
st.title("Climate Change Impact on Agriculture Dashboard")

# Load Dataset
data = pd.read_csv("climate_change_impact_on_agriculture_2024.csv")

# Fill Missing Values Correctly
for col in data.columns:
    if data[col].dtype == 'object' or str(data[col].dtype) == 'string':
        data[col] = data[col].fillna(data[col].mode()[0])
    else:
        data[col] = data[col].fillna(data[col].median())

# Encode Categorical Columns
label_encoders = {}
for col in data.select_dtypes(include=['object']).columns:
    le = LabelEncoder()
    data[col] = le.fit_transform(data[col])
    label_encoders[col] = le

# Display Dataset
st.subheader("Dataset Preview")
st.dataframe(data.head())

# Select Target Column
target = st.selectbox("Select Target Variable", data.columns)

# Prepare Data
X = data.drop(columns=[target])
y = data[target]

# Train-Test Split
X_train, X_test, y_train, y_test = train_test_split(
    X, y, test_size=0.2, random_state=42
)

# Model Training
model = RandomForestRegressor()
model.fit(X_train, y_train)

# Prediction
y_pred = model.predict(X_test)

# Metrics
mae = mean_absolute_error(y_test, y_pred)
r2 = r2_score(y_test, y_pred)

st.subheader("Model Performance")
st.write("MAE:", mae)
st.write("R² Score:", r2)

# Prediction Plot
st.subheader("Actual vs Predicted")
fig, ax = plt.subplots()
ax.scatter(y_test, y_pred)
ax.set_xlabel("Actual")
ax.set_ylabel("Predicted")
st.pyplot(fig)

# Feature Importance
st.subheader("Feature Importance")
importance = model.feature_importances_
features = X.columns

fig2, ax2 = plt.subplots()
ax2.barh(features, importance)
st.pyplot(fig2)

# User Input Prediction
st.subheader("Custom Prediction")
input_data = {}

for col in X.columns:
    input_data[col] = st.number_input(f"Enter {col}", value=float(X[col].mean()))

input_df = pd.DataFrame([input_data])
prediction = model.predict(input_df)

st.write("Predicted Value:", prediction[0])