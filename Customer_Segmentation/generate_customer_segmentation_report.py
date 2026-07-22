# ===============================================
# Project 1: Customer Segmentation Dashboard
# Author: Fernando Najera
# Purpose: K-means clustering customer data with visualization
# ===============================================

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
from sklearn.cluster import KMeans
from sklearn.preprocessing import StandardScaler
from sklearn.decomposition import PCA
import warnings
import yaml
import os

warnings.filterwarnings('ignore')


class CustomerSegmentation:
    """Customer Segmentation and Clustering Analysis"""

    def __init__(self, data_path='data/customers.csv'):
        self.data_path = data_path
        self.data = None
        self.scaler = StandardScaler()
        self.pca = PCA()
        self.model = None
        self.labels = None

    def load_data(self):
        """Load and clean customer data"""
        try:
            self.data = pd.read_csv(self.data_path)
            print(f"✓ Loaded {len(self.data)} customer records")
            print(f"✓ Columns: {list(self.data.columns)}")
            return self.data
        except FileNotFoundError:
            print(f"✗ File not found: {self.data_path}")
            return None

    def clean_data(self):
        """Data preprocessing"""
        if self.data is None:
            self.load_data()
            return self.data

        # Handle missing values
        self.data = self.data.dropna(subset=['SpendScore', 'EngagementScore', 'Age'])

        # Remove duplicates
        self.data = self.data.drop_duplicates()

        # Print cleaned data info
        print(f"✓ Cleaned data shape: {self.data.shape}")
        print(f"✓ Missing values before cleaning:\n{self.data.isnull().sum()}")
        return self.data

    def feature_engineering(self):
        """Create additional features"""
        if self.data is None:
            self.load_data()

        # Create engagement ratio
        self.data['EngagementRatio'] = self.data['EngagementScore'] / (self.data['SpendScore'] + 1)

        # Create value score
        self.data['ValueScore'] = (self.data['SpendScore'] + self.data['EngagementScore']) / 2

        # Age groups
        def get_age_group(age):
            if age < 30:
                return 'Young'
            elif age < 50:
                return 'Middle'
            else:
                return 'Senior'

        self.data['AgeGroup'] = self.data['Age'].apply(get_age_group)

        print("✓ Feature engineering complete")
        return self.data

    def scale_features(self):
        """Scale features for clustering"""
        if self.data is None:
            self.load_data()

        feature_cols = ['SpendScore', 'EngagementScore', 'Age']
        self.data_scaled = self.data[feature_cols].copy()
        self.data_scaled = self.scaler.fit_transform(self.data_scaled)

        print("✓ Features scaled")
        return self.data_scaled

    def find_optimal_clusters(self):
        """Find optimal number of clusters using silhouette score"""
        if self.data is None:
            self.load_data()

        X = self.scale_features()

        silhouette_scores = []
        inertias = []

        for n_clusters in range(2, 11):
            model = KMeans(n_clusters=n_clusters, random_state=42, n_init=10)
            labels = model.fit_predict(X)


        inertia = model.inertia_

        # Calculate silhouette score
        from sklearn.metrics import silhouette_score

        silhouette_scores.append(silhouette_score(X, labels))
        inertias.append(inertia)

        optimal_n_clusters = range(2, 11)
        n_clusters_with_highest_score = np.argmax(silhouette_scores) + 2

        print(f"✓ Optimal number of clusters: {n_clusters_with_highest_score}")
        print(f"✓ Highest silhouette score: {max(silhouette_scores):.3f}")

        return n_clusters_with_highest_score


    def fit_model(self, n_clusters=5):
        """Fit K-Means clustering model"""
        if self.data is None:
            self.load_data()

        X = self.scale_features()
        self.model = KMeans(n_clusters=n_clusters, random_state=42, n_init=10)
        self.labels = self.model.fit_predict(X)

        print(f"✓ Model trained with {n_clusters} clusters")
        print(f"✓ Cluster sizes: {self.cluster_sizes()}")

        return self.model


    def cluster_sizes(self):
        """Get cluster sizes"""
        if self.labels is None:
            return {}

        sizes = {}
        for i in range(self.model.n_clusters):
            cluster_indices = np.where(self.labels == i)[0]
            sizes[f'Cluster_{i}'] = len(cluster_indices)

        return sizes


    def visualize_clusters_2d(self):
        """2D visualization using PCA"""
        if self.data is None or self.labels is None:
            print("✗ Load data and fit model first")
            return

        # Apply PCA
        X = self.scale_features()
        X_pca = self.pca.fit_transform(X)

        # Get cluster labels from full model
        if self.model is not None:
            self.labels = self.model.predict(X_pca)

        # Plot
        plt.figure(figsize=(12, 8))
        scatter = plt.scatter(X_pca[:, 0], X_pca[:, 1],
                              c=self.labels, alpha=0.6, cmap='viridis', s=100)
        plt.colorbar(scatter, label='Cluster')

        # Add cluster centers
        centers = self.model.cluster_centers_
        plt.scatter(self.pca.transform(centers)[:, 0],
                    self.pca.transform(centers)[:, 1],
                    c='red', marker='X', s=200, alpha=0.8)

        plt.title('Customer Segmentation - 2D PCA Visualization')
        plt.xlabel('Principal Component 1')
        plt.ylabel('Principal Component 2')
        plt.tight_layout()
        plt.savefig('output/cluster_2d_viz.png', dpi=150)
        plt.close()

        print("✓ 2D visualization saved as cluster_2d_viz.png")


    def create_full_dashboard(self, output_dir='output'):
        """Create comprehensive visualization dashboard"""
        os.makedirs(output_dir, exist_ok=True)

        # Plot 1: Original distribution
        plt.figure(figsize=(14, 6))

        plt.subplot(1, 2, 1)
        plt.scatter(self.data['SpendScore'], self.data['EngagementScore'],
                    c=self.labels, alpha=0.5, cmap='viridis')
        plt.title('Customer Segments by Spend & Engagement')
        plt.xlabel('Spend Score')
        plt.ylabel('Engagement Score')

        plt.subplot(1, 2, 2)
        self.data['Cluster'] = self.labels
        plt.bar(self.data['Cluster'].unique(),
                self.data.groupby('Cluster').size(),
                alpha=0.7, color='steelblue')
        plt.title('Cluster Distribution')
        plt.xlabel('Cluster')
        plt.ylabel('Count')

        plt.tight_layout()
        plt.savefig(f'{output_dir}/cluster_dashboard.png', dpi=150)
        plt.close()

        # Plot 2: Cluster characteristics
        plt.figure(figsize=(14, 8))

        for i in range(len(self.data.columns) - 2):
            if i < 3:  # Plot top 3 features
                plt.subplot(2, 2, i + 1)
                sns.boxplot(x=self.labels, y=self.data.columns[i + 2], data=self.data)
                plt.title(f'{self.data.columns[i + 2]} by Cluster')
                plt.xlabel('Cluster')
                plt.ylabel(self.data.columns[i + 2])

        plt.tight_layout()
        plt.savefig(f'{output_dir}/cluster_characteristics.png', dpi=150)
        plt.close()

        print(f"✓ Dashboard saved to {output_dir}/")


    def generate_report(self, output_file='output/customer_segmentation_report.html'):
        """Generate markdown/HTML report"""

        report = f"""# Customer Segmentation Report
    
        ## Executive Summary
    
        - **Total Customers Analyzed:** {len(self.data)}
        - **Number of Clusters:** {self.model.n_clusters if self.model else 'N/A'}
        - **Analysis Date:** {pd.Timestamp('now').strftime('%Y-%m-%d')}
    
        ## Cluster Details
    
        """


        if self.model and self.labels.any():
            for i in range(self.model.n_clusters):
                cluster_mask = self.labels == i
                cluster_data = self.data[cluster_mask]

                report += f"""
        ### Cluster {i}
        - **Size:** {cluster_data.shape[0]} customers ({cluster_data.shape[0] / len(self.data) * 100:.1f}%)
        - **Avg. Spend Score:** {cluster_data['SpendScore'].mean():.2f}
        - **Avg. Engagement Score:** {cluster_data['EngagementScore'].mean():.2f}
        - **Avg. Age:** {cluster_data['Age'].mean():.1f}
        - **Gender Distribution:** {cluster_data['Gender'].value_counts()}
        - **Location Distribution:** {cluster_data['Location'].value_counts()}
        
    
        """

        report += """
        ## Recommendations
    
        1. **High-Value Cluster**: Target with premium offerings
        2. **Low-Engagement Cluster**: Re-engage campaigns
        3. **High-Engagement, Low-Spend**: Upsell opportunities
    
        """

        with open(output_file, 'w') as f:
            f.write(report)

        print(f"✓ Report generated: {output_file}")
        return report


# ===============================================
# Main Execution
# ===============================================

if __name__ == "__main__":

    try:
        # Initialize and run analysis
        cs = CustomerSegmentation(data_path='data/sample_customers.csv')

        print("=" * 60)
        print("CUSTOMER SEGMENTATION ANALYSIS")
        print("=" * 60)

        # Load data
        cs.load_data()

        # Clean data
        cs.clean_data()

        # Feature engineering
        cs.feature_engineering()

        # Find optimal clusters
        n_clusters = cs.find_optimal_clusters()

        # Fit model
        cs.fit_model(n_clusters=n_clusters)

        # Visualize
        cs.visualize_clusters_2d()
        cs.create_full_dashboard()

        # Generate report
        cs.generate_report()

        print("=" * 60)
        print("✓ ANALYSIS COMPLETE!")
        print("=" * 60)

    except Exception as e:
        print(f"✗ Error: {str(e)}")
        import traceback

        traceback.print_exc()


