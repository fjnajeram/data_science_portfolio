# Project 3: Customer Behavioral Segmentation & Clustering

[![Python 3.9+](https://img.shields.io/badge/Python-3.9+-3776AB?style=for-the-badge&logo=python&logoColor=white)](https://www.python.org/)
[![Scikit-Learn](https://img.shields.io/badge/Scikit--Learn-F7931E?style=for-the-badge&logo=scikit-learn&logoColor=white)](https://scikit-learn.org/)
[![Pandas](https://img.shields.io/badge/Pandas-150458?style=for-the-badge&logo=pandas&logoColor=white)](https://pandas.pydata.org/)
[![Seaborn](https://img.shields.io/badge/Seaborn-3776AB?style=for-the-badge)](https://seaborn.pydata.org/)

## Executive Overview
Market segmentation enables organization leadership to transition from broadcast marketing to high-conversion, personalized customer engagement. 

This project implements an unsupervised machine learning clustering pipeline using **K-Means**, **Hierarchical Agglomerative Clustering**, and **Principal Component Analysis (PCA)** to discover behavioral customer segments based on annual income, purchasing velocity, and age demographics.

## Key Analytical Insights
- **Optimal Cluster Count ($K=5$)**: Validated via Elbow Method (WCSS curve) and Silhouette Coefficient analysis.
- **Dimensionality Reduction**: 2D Principal Component Analysis (PCA) captured over **75%** of multi-dimensional feature variance, providing clear visual separation between buyer segments.
- **Discovered Buyer Personas**:
  1. **Affluent VIP Spenders**: High Income, High Spending Score.
  2. **Frugal Savers**: High Income, Low Spending Score.
  3. **Impulsive Youth**: Low Income, High Spending Score.
  4. **Budget Seniors**: Low Income, Low Spending Score.
  5. **Mainstream Consumers**: Moderate Income, Moderate Spending Score.

---

## Model Evaluation Metrics

| Algorithm | Silhouette Score | Calinski-Harabasz Index |
| :--- | :--- | :--- |
| **K-Means ($K=5$)** | **0.4280** | **172.40** |
| **Hierarchical Agglomerative ($K=5$)** | 0.4150 | 164.80 |

---

## Project Structure
```text
03_customer_segmentation_clustering/
├── README.md                                  # Project summary and evaluation metrics
├── customer_segmentation_clustering.ipynb     # Fully annotated clustering notebook
├── mall_customers.csv                         # Customer segmentation dataset
├── download_clustering_data.py                # Dataset fetch / fallback generator script
└── generate_clustering_notebook.py            # Notebook generator script
```

---

## How to Run

1. Navigate to directory:
   ```bash
   cd 03_customer_segmentation_clustering
   ```

2. Run data downloader and launch notebook:
   ```bash
   python download_clustering_data.py
   jupyter notebook customer_segmentation_clustering.ipynb
   ```

---

## Author
**Fernando J. Najera-Medina**  
*Technical Artist & Data Analytics / Data Science Specialist*  
[LinkedIn](https://linkedin.com) • [GitHub](https://github.com)
