# =============================
# Crop Resilience Predictor
# Dataset: Agricultural Crop Yield in Indian States (1997–2020)
# Offline-only, self-contained
# Author: Tanishka Pal
# =============================

# 1. Import Libraries
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import LabelEncoder, StandardScaler, PolynomialFeatures
from sklearn.preprocessing import OneHotEncoder
from sklearn.compose import ColumnTransformer
from sklearn.linear_model import LinearRegression
from sklearn.tree import DecisionTreeClassifier
from sklearn.metrics import mean_squared_error, r2_score, accuracy_score, confusion_matrix, classification_report

# =============================
# 2. Load Dataset
# =============================
df = pd.read_csv(r"C:\Users\tanis\FOSS-Recruitment-2025\projects\Pal_Tanishka\src\crop_yield.csv")  # CSV included in repo
print("Dataset Preview:")
print(df.head())
print("\nDataset Info:")
print(df.info())

# =============================
# 3. Data Preprocessing
# =============================
# Drop missing values for simplicity
df = df.dropna()

# Define categorical and numeric columns
categorical_features = ['Crop', 'Season', 'State']
numeric_features = ['Annual_Rainfall', 'Temperature', 'Fertilizer']

# Features (X) and target (y)
X = df.iloc[:, :-1].values
y = df.iloc[:, -1].values

# Define categorical and numeric columns
categorical_features = ['Crop', 'Season', 'State']
numeric_features = ['Crop_Year', 'Area', 'Production', 'Annual_Rainfall', 'Fertilizer', 'Pesticide']

# Apply OneHotEncoder on categorical features
ct = ColumnTransformer(
    transformers=[
        ('encoder', OneHotEncoder(), categorical_features)
    ],
    remainder='passthrough'   # keeps numeric features as they are
)
