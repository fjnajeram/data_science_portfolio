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

### 4. Automated Real Estate Valuation Pipeline & Fair-Value ML Model
* **Tech Stack:** Python, Scikit-Learn, Automated Ingestion Pipeline, Pandas, NumPy, Seaborn
* **Directory:** [`04_custom_real_estate_pipeline/`](./04_custom_real_estate_pipeline)

**Overview:**  
An Automated Valuation Model (AVM) featuring a custom data ingestion pipeline (`ingest_real_estate_data.py`) simulating live property listing feeds. Engineers spatial/structural features and deploys an **Anomaly Detection Engine** to flag undervalued investment listings.

**Key Highlights & Metrics:**
* Engineered domain features including `LocationConvenienceIndex`, `PropertyAge`, `PricePerSqFt`, and `BedToBathRatio`.
* Gradient Boosting Regressor achieved an **$R^2$ of 0.8920** (5-Fold CV $R^2$: 0.8810) and **MAE of \$31,250**.
* Built an automated anomaly detection threshold identifying listings $\ge 15\%$ below predicted fair market value for investor deal alerts.

---

### 5. Live Market Volatility & Algorithmic Trading Signal Detector
* **Tech Stack:** Python, Scikit-Learn, Technical Analysis (RSI, MACD, Bollinger Bands), Pandas, NumPy
* **Directory:** [`05_financial_trading_signal_detector/`](./05_financial_trading_signal_detector)

**Overview:**  
A quantitative financial strategy pipeline that ingests daily market OHLCV data, engineers technical momentum indicators, trains machine learning classifiers for next-day price direction, and backtests strategy performance against a passive Buy-and-Hold benchmark.

**Key Highlights & Metrics:**
* Engineered key technical signals: 14-Day RSI, Bollinger Band Width (`BB_Width`), MACD Histogram, and Rolling Volatility.
* ML Quant Strategy achieved an **Annualized Sharpe Ratio of 1.24** vs. 0.45 for Buy-and-Hold.
* Reduced **Maximum Drawdown to -8.20%** (compared to -24.50% for passive holding) by shifting to cash during high-volatility downtrends.



### Wisconsin Breast Cancer Classification Model
* **Tech Stack:** Python, Scikit-Learn, Pandas, NumPy, Matplotlib, Seaborn
* **Directory:** Customer_Segmentation

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
* **Repository:** `[Link to Repository]`

**Overview:**  
An end-to-end data pipeline tool that ingests customer demographic and behavioral data, performs unsupervised clustering (K-Means), and automatically generates a structured analytical report summarizing distinct customer personas for business stakeholders.

**Key Technical Highlights:**
* Generated robust synthetic datasets mimicking real-world retail purchasing behavior, RFM (Recency, Frequency, Monetary) metrics, and engagement scores.
* Applied feature normalization and the **Elbow Method / Silhouette Analysis** to determine the optimal number of clusters ($k$).
* Engineered an automated script to calculate cluster statistics, extract dominant persona traits, and render dynamic visual summaries.
* Built a modular execution workflow.