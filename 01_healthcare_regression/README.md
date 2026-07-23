# Project 1: Healthcare Medical Cost & Risk Prediction (Regression)

[![Python 3.9+](https://img.shields.io/badge/Python-3.9+-3776AB?style=for-the-badge&logo=python&logoColor=white)](https://www.python.org/)
[![Scikit-Learn](https://img.shields.io/badge/Scikit--Learn-F7931E?style=for-the-badge&logo=scikit-learn&logoColor=white)](https://scikit-learn.org/)
[![Pandas](https://img.shields.io/badge/Pandas-150458?style=for-the-badge&logo=pandas&logoColor=white)](https://pandas.pydata.org/)
[![Matplotlib](https://img.shields.io/badge/Matplotlib-11557c?style=for-the-badge)](https://matplotlib.org/)

## Executive Overview
In healthcare economics and health insurance actuarial underwriting, predicting individual annual medical expenditures accurately is essential for risk-adjusted pricing, policy reserve management, and targeted clinical intervention programs.

This repository presents an end-to-end regression analysis evaluating both linear and non-linear machine learning models (OLS Linear Regression, Regularized Ridge/Lasso, Random Forest, and Gradient Boosting Regressors) on US insurance claim demographics.

## Key Insights & Clinical Findings
- **Compound Super-Linear Risk**: Smoking alone elevates baseline expected medical claims by ~\$14,000/year. However, the compound interaction of **Smoking + Obesity (BMI $\ge$ 30)** creates a super-linear risk surge, elevating expected annual claims to **\$35,000 - \$45,000**.
- **Model Performance**: Linear Regression model achieved an **$R^2$ of ~0.8764** on unseen test data.
- **Targeted Wellness ROI**: Actuarial underwriting teams can achieve maximum cost reduction by sponsoring targeted smoking cessation and metabolic health programs specifically for the high-risk "Smoker + BMI $\ge 30$" subgroup.

---

## Model Benchmark Results

| Model                 | Test RMSE ($) | Test MAE ($) | Test $R^2$ | 5-Fold CV $R^2$ |
|:----------------------|:--------------| :--- |:-----------|:----------------|
| **Linear Regression** | **$4,380.43** | **$2430.27** | **0.8764** | **0.8561**      |
| **Lasso Regression**  | $4,380.96     | $2431.86 | 0.8764     | 0.8561                |
| **Gradient Boosting** | $4,402.36     | $2491.66 | 0.8752           | 0.8458        |
| **Ridge Regression**  | $4,411.80     | $2561.28| 0.8746     | 0.8531         |
| **Random Forest**     | $4,669.31     | $2586.58 | 0.8596     | 0.8257         |



---

## Project Structure
```text
01_healthcare_regression/
├── README.md                           # Executive summary and benchmark results
├── medical_cost_regression.ipynb       # Complete annotated Jupyter notebook
├── insurance.csv                       # Medical cost dataset
└── requirements.txt                    # Project Python dependencies
```


---

## Author
**Fernando J. Najera-Medina**  
*Technical Artist & Data Analytics / Data Science Specialist*  
[LinkedIn](https://linkedin.com) • [GitHub](https://github.com)
