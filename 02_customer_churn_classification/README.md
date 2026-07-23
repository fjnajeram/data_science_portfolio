# Project 2: Customer Churn & Retention Machine Learning Classifier

[![Python 3.9+](https://img.shields.io/badge/Python-3.9+-3776AB?style=for-the-badge&logo=python&logoColor=white)](https://www.python.org/)
[![Scikit-Learn](https://img.shields.io/badge/Scikit--Learn-F7931E?style=for-the-badge&logo=scikit-learn&logoColor=white)](https://scikit-learn.org/)
[![Pandas](https://img.shields.io/badge/Pandas-150458?style=for-the-badge&logo=pandas&logoColor=white)](https://pandas.pydata.org/)
[![Seaborn](https://img.shields.io/badge/Seaborn-3776AB?style=for-the-badge)](https://seaborn.pydata.org/)

## Executive Overview
Customer retention is a critical profitability driver in subscription, telecommunications, and SaaS business models. Retaining existing users is vastly more cost-effective than acquiring new ones.

This project delivers a machine learning classification pipeline designed to identify high-risk churn customers in advance. We evaluate Logistic Regression, Random Forest, and Gradient Boosting models, optimizing the classification decision boundary to maximize **Recall** and **ROC-AUC** while minimizing the total cost of churn.

## Key Strategic Takeaways
- **Contract & Tenure Dominance**: Short tenure (< 12 months) combined with Month-to-Month contracts represent over **60%** of total churn volume.
- **Decision Threshold Optimization**: Adjusting the classification threshold from 0.50 down to **0.35** boosts **Churn Sensitivity (Recall) to >78%**, catching significantly more at-risk users before subscription cancellation.
- **Top Risk Predictors**: Total Charges, Tenure, Fiber Optic internet service, and Month-to-Month contracts are the top 4 churn predictors identified via Gradient Boosting feature importances.

---

## Model Benchmark Results

| Model | Accuracy | Precision | Recall (Sensitivity) | F1-Score | ROC-AUC |
| :--- | :--- | :--- | :--- | :--- | :--- |
| **Gradient Boosting** | **0.8062** | **0.6620** | **0.5481** | **0.5997** | **0.8465** |
| **Random Forest (Weighted)** | 0.7715 | 0.5510 | 0.7513 | 0.6358 | 0.8390 |
| **Logistic Regression (Weighted)**| 0.7480 | 0.5180 | 0.7968 | 0.6280 | 0.8350 |

> *Note: Shifting the Gradient Boosting classification threshold to 0.35 increases Recall to 0.7850 with an F1-Score of 0.6420.*

---

## Project Structure
```text
02_customer_churn_classification/
├── README.md                              # Project summary and benchmark results
├── customer_churn_classification.ipynb    # Fully annotated classification notebook
├── telecom_churn.csv                      # Telco customer churn dataset
├── download_churn_data.py                 # Dataset fetch / fallback generator script
└── generate_churn_notebook.py             # Notebook generator script
```

---

## How to Run

1. Navigate to directory:
   ```bash
   cd 02_customer_churn_classification
   ```

2. Run data downloader and launch notebook:
   ```bash
   python download_churn_data.py
   jupyter notebook customer_churn_classification.ipynb
   ```

---

## Author
**Fernando J. Najera-Medina**  
*Technical Artist & Data Analytics / Data Science Specialist*  
[LinkedIn](https://linkedin.com) • [GitHub](https://github.com)
