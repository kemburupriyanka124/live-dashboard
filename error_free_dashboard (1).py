import streamlit as st
import pandas as pd
import numpy as np

from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestRegressor
from sklearn.metrics import mean_squared_error, r2_score

st.set_page_config(page_title="Crop Yield Dashboard", layout="wide")
st.title("🌾 Error-Free Crop Yield Dashboard")

uploaded_file = st.file_uploader("Upload CSV file", type=["csv"])

if uploaded_file is not None:
    data = pd.read_csv(uploaded_file)
    st.subheader("Dataset Preview")
    st.dataframe(data.head())

    target = "Crop_Yield_MT_per_HA"

    if target not in data.columns:
        st.error(f"Target column '{target}' not found.")
        st.stop()

    # Fill missing values
    for col in data.columns:
        if data[col].dtype == "object":
            data[col] = data[col].fillna(data[col].mode()[0])
        else:
            data[col] = data[col].fillna(data[col].median())

    # Encode categorical columns
    cat_cols = data.select_dtypes(include="object").columns.tolist()
    if target in cat_cols:
        cat_cols.remove(target)

    data = pd.get_dummies(data, columns=cat_cols, drop_first=True)

    X = data.drop(columns=[target])
    y = data[target]

    X_train, X_test, y_train, y_test = train_test_split(
        X, y, test_size=0.2, random_state=42
    )

    model = RandomForestRegressor(n_estimators=50, random_state=42)
    model.fit(X_train, y_train)

    pred = model.predict(X_test)

    rmse = np.sqrt(mean_squared_error(y_test, pred))
    r2 = r2_score(y_test, pred)

    c1, c2 = st.columns(2)
    c1.metric("RMSE", f"{rmse:.3f}")
    c2.metric("R²", f"{r2:.3f}")

    # Prediction input
    st.sidebar.header("Prediction Input")
    user_input = {}

    for col in X.columns:
        user_input[col] = st.sidebar.number_input(
            col,
            value=float(X[col].median())
        )

    user_df = pd.DataFrame([user_input])

    if st.button("Predict Yield"):
        result = model.predict(user_df)[0]
        st.success(f"Predicted Crop Yield: {result:.2f} MT/ha")

    # Built-in charts (no matplotlib)
    st.subheader("Actual vs Predicted (Sample)")
    chart_df = pd.DataFrame({
        "Actual": y_test.reset_index(drop=True).head(20),
        "Predicted": pd.Series(pred).head(20)
    })
    st.line_chart(chart_df)

    st.subheader("Feature Importance")
    importance = pd.DataFrame({
        "Feature": X.columns,
        "Importance": model.feature_importances_
    }).sort_values("Importance", ascending=False).head(10)

    st.bar_chart(importance.set_index("Feature"))

else:
    st.info("Please upload a CSV file to continue.")
