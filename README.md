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

<img width="1892" height="983" alt="Screenshot (1)" src="https://github.com/user-attachments/assets/8a7c8d64-4819-4991-ad9e-060cc211e288" />

Insights

The developed integrated framework provides several important insights into crop yield prediction under uncertain climatic conditions. The use of LightGBM showed that nonlinear machine learning models are highly effective in capturing complex relationships between climatic variables and agricultural output. Compared with traditional regression approaches, the model demonstrated stronger predictive capability because it was able to learn interactions among variables such as temperature, rainfall, fertilizer usage, and soil health without requiring strict linear assumptions. The quantile-based modeling approach provided deeper insight than single-value prediction because it generated lower, median, and upper yield estimates, allowing uncertainty to be explicitly represented. This made it possible to understand not only the expected crop yield but also the likely variation around that prediction under different climatic scenarios.

The uncertainty interval produced by the quantile models showed that prediction confidence changes across observations, indicating that some agricultural situations are inherently more uncertain than others. Wider intervals generally reflected greater climatic instability or feature combinations associated with less predictable outcomes. The application of Generalized Extreme Value distribution revealed that extreme crop losses can be estimated separately from average prediction behavior. By modeling lower-tail residuals, the framework identified rare but severe yield-loss scenarios, which are highly relevant in climate-sensitive agriculture where extreme weather events may create sudden production shocks. This tail-risk analysis added an important risk perspective that is not normally captured in standard machine learning forecasting systems.

Feature importance analysis showed that only a limited number of variables dominate crop yield prediction, indicating that some environmental factors contribute more strongly than others. This supports the idea that targeted agricultural interventions may produce greater benefits when focused on the most influential variables. The SHAP explanation further clarified how individual features increase or decrease yield predictions for specific cases, making the model interpretable rather than purely predictive. The causal evaluation of adaptation strategies through the doubly robust framework indicated that adaptation measures can produce measurable yield improvements, although the impact varies depending on feature combinations and treatment conditions.

The live dashboard added practical insight by converting the analytical framework into an interactive system. Through slider-based input control, users can simulate different climate and agricultural scenarios and immediately observe changes in predicted yield, uncertainty range, and model explanation. This demonstrated that the framework is not limited to offline analysis but can function as a practical decision-support environment.

Conclusions

This study successfully developed an integrated crop yield prediction framework that combines machine learning, uncertainty quantification, extreme risk analysis, causal inference, and interactive deployment into a unified agricultural analytics system. The use of LightGBM provided accurate prediction of crop yield under varying climatic conditions by effectively modeling nonlinear relationships between environmental and agricultural variables. Quantile regression extended the predictive capability by estimating uncertainty ranges, allowing prediction intervals rather than single deterministic values. This significantly improves practical usefulness because agricultural decisions often require understanding of possible variation rather than relying only on one expected value.

The integration of extreme value analysis enabled identification of severe yield-loss risks that may arise under rare climate conditions. This tail-risk component strengthened the framework by introducing probabilistic understanding of extreme agricultural loss scenarios. The causal modeling component further improved the study by evaluating the potential impact of adaptation strategies, providing evidence that intervention-based agricultural planning can influence yield outcomes.

The deployment of the full framework in an interactive live dashboard demonstrated the practical applicability of the proposed model. Users can upload datasets, modify climate-related variables, and visualize all major analytical outputs including prediction, uncertainty, extreme risk, feature importance, and explainability in a single interface. This makes the framework suitable not only for academic analysis but also for practical agricultural decision support.

Overall, the proposed system shows that combining predictive modeling, uncertainty estimation, explainability, and interactive visualization can create a more complete agricultural forecasting tool. The framework offers strong potential for future extension into real-time climate-linked agricultural advisory systems, regional crop monitoring platforms, and farmer-support technologies.
