mport pandas as pd  # For loading, manipulating and analyzing structured data 
import numpy as np # USed for numerical computation and array operations 
import matplotlib.pyplot as plt #Creating Basic charts and visualizations
import seaborn as sns #Creating more advance and visual statistical plots 
from sklearn.ensemble import RandomForestClassifier #For model building 
from sklearn.model_selection import train_test_split # To split the data into training and testing set 
from sklearn.metrics import accuracy_score, classification_report, confusion_matrix #To evaluate the model
import warnings # to suppress unnessary warning messages so the output stays clean
warnings.filterwarnings("ignore")

def load_data():
    """
    Loads and merges all five Brazilian E-Commerce datasets
    into one master dataframe.
    Returns the merged dataframe.
    """
    customers = pd.read_csv("../data/olist_customers_dataset.csv")
    orders = pd.read_csv("../data/olist_orders_dataset.csv")
    order_reviews = pd.read_csv("../data/olist_order_reviews_dataset.csv")
    order_items = pd.read_csv("../data/olist_order_items_dataset.csv")
    order_payments = pd.read_csv("../data/olist_order_payments_dataset.csv")

    # Merge all datasets into one master dataframe
    df = orders.merge(order_reviews, on="order_id", how="left")
    df = df.merge(order_items, on="order_id", how="left")
    df = df.merge(order_payments, on="order_id", how="left")
    df = df.merge(customers, on="customer_id", how="left")

    return df