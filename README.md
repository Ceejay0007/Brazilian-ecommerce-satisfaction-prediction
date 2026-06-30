# Brazilian E-Commerce Customer Satisfaction Prediction

## Business Question
What factors most influence customer satisfaction in e-commerce,
and can we predict whether a customer will leave a positive or
negative review based on their order experience?

## Dataset
- **Source:** Brazilian E-Commerce Public Dataset by Olist — Kaggle
- **Size:** 119,000+ orders across 5 relational tables
- **Tables Used:** orders, order_reviews, order_items, order_payments, customers

## Project Structure
notebooks/
 01_data_loading_and_overview.ipynb
 02_exploratory_data_analysis.ipynb
 03_data_cleaning_and_feature_engineering.ipynb
 04_model_building_and_evaluation.ipynb
 05_confusion_matrix.ipynb
 06_feature_importance_and_recommendations.ipynb

## How To Run This Project
Run the notebooks in order starting from 01 through 06.

## Data
Download the dataset from Kaggle:
https://www.kaggle.com/datasets/olistbr/brazilian-ecommerce
Place all CSV files inside the /data folder before running.

## Results
- Model: Random Forest Classifier
- Accuracy: 80%
- Key Finding: Late delivery and long delivery times are the
  strongest predictors of customer dissatisfaction

## Tools Used
Python, pandas, scikit-learn, matplotlib, seaborn

## Author
Conrad Toke
github.com/Ceejay0007