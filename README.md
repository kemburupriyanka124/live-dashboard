# live-dashboard
The dashboard consolidates all analytical components into a single visual interface, making the system accessible and interpretable for researchers, policymakers, and agricultural stakeholders. Overall, the proposed framework demonstrates how machine learning, statistical risk modeling, causal analysis.
his project presents an interactive live dashboard for crop yield prediction under climate uncertainty using machine learning, uncertainty quantification, extreme risk analysis, and explainable AI. The dashboard is built using Streamlit and integrates a hybrid predictive framework based on LightGBM to estimate crop yield from climatic and agricultural variables such as temperature, rainfall, fertilizer usage, and soil health indicators.

The system uses quantile-based prediction models to generate lower (10th percentile), median (50th percentile), and upper (90th percentile) yield estimates, allowing uncertainty-aware forecasting instead of single-point prediction. Extreme yield-loss events are analyzed using Generalized Extreme Value distribution to estimate tail risk under severe climate conditions. The dashboard also includes feature importance visualization and SHAP explanations to interpret how different variables influence yield predictions.

An interactive sidebar enables users to adjust numerical input variables in real time and instantly observe changes in predicted yield and uncertainty intervals. All major project visualizations — actual vs predicted yield, uncertainty bands, extreme risk curves, feature importance plots, and SHAP explanations — are displayed consecutively in a single dashboard interface.

This project is designed as a practical decision-support tool for agricultural analytics, climate risk assessment, and crop yield forecasting.

Main Features
Crop yield prediction using LightGBM
Quantile regression for uncertainty estimation
Extreme Value Theory for tail-risk analysis
Interactive sliders for real-time scenario testing
Feature importance analysis
SHAP-based model explainability
Single-frame integrated visualization dashboard
Technology Stack
Python
Streamlit
LightGBM
SHAP
Scikit-learn
Matplotlib
Seaborn
Use Case

The dashboard can support:

climate-aware agricultural forecasting
yield uncertainty analysis
adaptation planning
research demonstration
