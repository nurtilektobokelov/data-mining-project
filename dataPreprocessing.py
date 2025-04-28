import pandas as pd
from sklearn.decomposition import PCA
from sklearn.preprocessing import MinMaxScaler
from sklearn.cluster import KMeans
import matplotlib.pyplot as plt

# Step 1: Data Cleaning (Handle Missing Values and Duplicates)
# Load the dataset
file_path = '/Users/nurti/Desktop/python/Data Mining HW/gameandgrade.csv'
data = pd.read_csv(file_path)

# Remove duplicates
data_cleaned = data.drop_duplicates()

# Step 2: Data Integration
# (Skipping data integration as no additional datasets are provided)

# Step 3: Data Reduction (Using PCA)
# Selecting numerical columns for PCA
numerical_cols = data_cleaned.select_dtypes(include=['float64', 'int64']).columns

# Perform PCA
pca = PCA(n_components=2)  # Reducing to 2 components for visualization
pca_result = pca.fit_transform(data_cleaned[numerical_cols])

# Add PCA result to the dataframe
data_cleaned['PCA1'] = pca_result[:, 0]
data_cleaned['PCA2'] = pca_result[:, 1]

# Step 4: Data Transformation (Normalization)
# Normalize the numerical columns
scaler = MinMaxScaler()
data_normalized = data_cleaned.copy()
data_normalized[numerical_cols] = scaler.fit_transform(data_cleaned[numerical_cols])

# Step 5: Data Discretization (Grade Discretization into Categories)
# Convert 'Grade' column to numeric and discretize into Low, Medium, High categories
bins = [0, 60, 80, 100]
labels = ['Low', 'Medium', 'High']
data_normalized['Grade'] = pd.to_numeric(data_normalized['Grade'], errors='coerce')
data_normalized['Grade Category'] = pd.cut(data_normalized['Grade'], bins=bins, labels=labels)

# Step 6: Clustering (K-Means)
# We will use K-Means Clustering to segment the dataset into 3 clusters
kmeans = KMeans(n_clusters=3, random_state=42)
data_normalized['Cluster'] = kmeans.fit_predict(data_normalized[numerical_cols])

# Step 7: Visualize the Clusters
plt.scatter(data_normalized['PCA1'], data_normalized['PCA2'], c=data_normalized['Cluster'], cmap='viridis')
plt.title('K-Means Clustering')
plt.xlabel('PCA1')
plt.ylabel('PCA2')
plt.colorbar(label='Cluster')
plt.show()

# The final processed data with PCA, Normalization, Discretization, and Clustering
processed_data = data_normalized[['Sex', 'School Code', 'Playing Years', 'Playing Often', 'Playing Hours', 
                                 'Playing Games', 'Parent Revenue', 'Father Education', 'Mother Education', 
                                 'Grade', 'PCA1', 'PCA2', 'Grade Category', 'Cluster']]

# Optionally, save the final processed data to a new CSV
processed_data.to_csv('processed_game_and_grade_with_clusters.csv', index=False)

# Display the processed data
print(processed_data.head())
