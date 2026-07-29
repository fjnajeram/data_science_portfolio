# Fernando J. Najera-Medina | Data Science & Analytics Portfolio

Welcome to my Data Science portfolio! I am a **Principal Technical Artist & Pipeline Specialist** transitioning into **Data Science and Data Analytics**. 

With 20+ years of experience writing Python tools, optimizing asset processing pipelines, and solving spatial/kinematic problems in game development (most recently at **Amazon Games Studio**), I apply a strong engineering mindset to data manipulation, exploratory data analysis, machine learning, and workflow automation.

---

## 🛠️ Core Tech Stack & Tools

* **Languages & Scripting:** Python, SQL, C++, MEL
* **Data Science & Analytics:** Pandas, NumPy, SciPy, SQL / Relational Databases
* **Data Visualization:** Matplotlib, Seaborn, Plotly, Folium
* **Machine Learning & Engineering:** Scikit-Learn, Algorithmic Optimization, Feature Engineering, OOP Architecture
* **Quant & Time-Series:** Technical Indicators (RSI, MACD, Bollinger Bands), Backtesting Frameworks
* **Environment & Tools:** PyCharm, Jupyter Notebooks, Git, Perforce, Claude API / LLM Integrations

---

## 🎓 Education & Specialized Credentials

* **Data Science & ML Certifications:** IBM Data Science Professional Track / Coursera
  * *Machine Learning with Python*
  * *Databases and SQL for Data Science with Python*
  * *Data Analysis & Data Visualization with Python*
  * *Algorithmic Toolbox & Software Engineering Fundamentals*
* **B.A. in Computer Art** — Academy of Art University (San Francisco, CA)
* **B.A. in Marketing** — ITESM (Monterrey, Mexico)

---

## 📫 Connect With Me

* **LinkedIn:** [linkedin.com/in/fernando-najera-medina-7916224](https://www.linkedin.com/in/fernando-najera-medina-7916224)
* **Portfolio & Demo Reels:** [fernajera.com](https://fernajera.com/demo-reels.html)
* **Email:** fjnajeram@gmail.com
* **Location:** Randolph, NJ

---

## 📂 Portfolio Projects

### 1. Healthcare Medical Cost & Risk Prediction (Regression)
* **Tech Stack:** Python, Scikit-Learn, Pandas, NumPy, Matplotlib, Seaborn
* **Directory:** [`01_healthcare_regression/`](./01_healthcare_regression)

**Overview:**  
An end-to-end healthcare economics regression analysis evaluating actuarial medical claims data to predict individual annual healthcare expenditures. The project models linear and non-linear interactions between demographic and lifestyle risk factors to optimize risk-adjusted pricing and wellness interventions.

**Key Highlights & Metrics:**
* Identified a **compound super-linear risk surge**: while smoking alone adds ~\$14,000/yr in claims, **Smoking + Obesity (BMI $\ge$ 30)** elevates claims to **\$35,000–\$45,000/yr**.
* Benchmarked Linear Regression, Lasso, Ridge, Random Forest, and Gradient Boosting Regressors.
* Achieved an **$R^2$ of 0.8764** and **MAE of \$2,430.27** on unseen test data using Linear/Lasso Regression.

---

### 2. Customer Churn & Retention Machine Learning Classifier
* **Tech Stack:** Python, Scikit-Learn, Pandas, NumPy, Seaborn, Matplotlib
* **Directory:** [`02_customer_churn_classification/`](./02_customer_churn_classification)

**Overview:**  
A subscription business classification pipeline that predicts customer churn risk prior to cancellation. Evaluates Logistic Regression, Random Forest, and Gradient Boosting, focusing on threshold tuning to minimize customer acquisition loss.

**Key Highlights & Metrics:**
* Discovered that short tenure (< 12 months) combined with Month-to-Month contracts account for **>60% of total churn volume**.
* Gradient Boosting achieved top overall performance with an **ROC-AUC of 0.8465** and **Accuracy of 80.62%**.
* Optimized classification decision threshold to **0.35**, increasing **Churn Sensitivity (Recall) to 78.50%** to capture at-risk accounts proactively.

---

### 3. Customer Behavioral Segmentation & Clustering
* **Tech Stack:** Python, Scikit-Learn (K-Means, Agglomerative), PCA, Pandas, Seaborn
* **Directory:** [`03_customer_segmentation_clustering/`](./03_customer_segmentation_clustering)

**Overview:**  
An unsupervised machine learning pipeline designed to segment consumer populations based on annual income, purchasing score, and age demographics, establishing actionable business personas for targeted marketing.

**Key Highlights & Metrics:**
* Validated **$K=5$ optimal clusters** using the Elbow Method (WCSS) and Silhouette Analysis (**Silhouette Score: 0.4280**, **Calinski-Harabasz Index: 172.40**).
* Leveraged 2D **Principal Component Analysis (PCA)** to capture over **75% of multi-dimensional feature variance**.
* Mapped 5 distinct customer personas: *Affluent VIP Spenders*, *Frugal Savers*, *Impulsive Youth*, *Budget Seniors*, and *Mainstream Consumers*.

---

### Wisconsin Breast Cancer Classification Model (MCC_DataAnalyticsModeling)
* Final project for course:
   * Data Analytics Applications and Modeling.
   * County College of Morris (Center for Workforce Development)
* **Tech Stack:** Python, Scikit-Learn, Pandas, NumPy, Matplotlib, Seaborn
* **Directory:** MCC_DataAnalyticsModeling/MCC_DataAnalyticsModeling/

**Overview:**  
A machine learning classification project evaluating diagnostic features derived from digitized fine needle aspirate (FNA) images of breast masses. The objective was to build and tune a highly reliable binary classifier to distinguish between malignant and benign tumors.

**Key Technical Highlights:**
* Performed Exploratory Data Analysis (EDA) and feature correlation profiling to identify key predictive parameters (e.g., radius, texture, concavity).
* Handled feature scaling and comparison across multiple algorithms (Logistic Regression, Support Vector Machines, and Random Forest).
* Optimized hyperparameter configurations prioritizing **High Recall for Malignant cases** to minimize false negatives in medical diagnostics.
* Evaluated models using Confusion Matrices, ROC-AUC curves, and Precision-Recall tradeoffs.

---

### Automated Customer Segmentation & Report Generator
* **Tech Stack:** Python, Pandas, Scikit-Learn (K-Means), Matplotlib, Seaborn, Jinja2 / PDF Engine
* **Directory:** Customer_Segmentation

**Overview:**  
An end-to-end data pipeline tool that ingests customer demographic and behavioral data, performs unsupervised clustering (K-Means), and automatically generates a structured analytical report summarizing distinct customer personas for business stakeholders.

**Key Technical Highlights:**
* Generated robust synthetic datasets mimicking real-world retail purchasing behavior, RFM (Recency, Frequency, Monetary) metrics, and engagement scores.
* Applied feature normalization and the **Elbow Method / Silhouette Analysis** to determine the optimal number of clusters ($k$).
* Engineered an automated script to calculate cluster statistics, extract dominant persona traits, and render dynamic visual summaries.
* Built a modular execution workflow.
