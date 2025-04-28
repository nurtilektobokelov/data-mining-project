# Data Mining Project: Student Data Clustering

This repository contains the code and results for the **Data Mining** project, where we perform data preprocessing and clustering analysis on a student dataset. The main objective is to apply various data preprocessing techniques and then use **K-Means clustering** to segment students based on their academic performance and behavior.

## Table of Contents

1. [Project Description](#project-description)
2. [Data Preprocessing Techniques](#data-preprocessing-techniques)
3. [Model Selection](#model-selection)
4. [Results](#results)
5. [Installation and Setup](#installation-and-setup)
6. [Usage](#usage)
7. [Future Improvements](#future-improvements)
8. [License](#license)

## Project Description

This project involves preprocessing a dataset of student behaviors and academic performance. The dataset includes features such as playing habits, parental education, and student grades. We applied various preprocessing steps, such as data cleaning, normalization, PCA, and discretization. After preprocessing, we used **K-Means clustering** to segment the students into different groups based on these features.

## Data Preprocessing Techniques

- **Data Cleaning**: Removed duplicate entries and handled missing values.
- **Data Transformation**: Applied **Min-Max Scaling** to normalize the numerical features.
- **Data Reduction**: Used **Principal Component Analysis (PCA)** to reduce dimensionality to two components for visualization.
- **Data Discretization**: The continuous "Grade" feature was categorized into **Low**, **Medium**, and **High**.

## Model Selection

We applied **K-Means clustering** to segment the students into three groups:
- **Cluster 1**: High-performing students
- **Cluster 2**: Medium-performing students
- **Cluster 3**: Low-performing students

**Why K-Means?**
- It's an unsupervised learning algorithm that helps discover patterns in data without labeled outcomes.
- It's efficient and works well for segmenting data based on similarities.

## Results

- **Clustering Outcome**: We discovered three distinct clusters, each representing different types of students based on their behavior and academic performance.
- **PCA Visualization**: The two principal components were used to plot the data, helping visualize the distribution of the clusters.

## Installation and Setup

To run the project, you need to have **Python** and several libraries installed. Follow these steps:

1. Clone the repository:
    ```bash
    git clone https://github.com/your-username/data-mining-project.git
    ```
2. Navigate to the project directory:
    ```bash
    cd data-mining-project
    ```
3. Install the required libraries:
    ```bash
    pip install -r requirements.txt
    ```

## Usage

After setting up the environment, you can run the main script (`main.py`) to execute the data preprocessing and clustering steps.

1. Run the script:
    ```bash
    python main.py
    ```

2. The results will be saved as a CSV file with clustering information.

## Future Improvements

- **Additional Data**: Collect more features (e.g., extracurricular activities, time spent studying) to improve clustering accuracy.
- **Clustering Algorithms**: Experiment with other clustering algorithms like DBSCAN or Hierarchical Clustering for better segmentation.
- **Model Evaluation**: Use metrics like **Silhouette Score** to evaluate clustering quality.

