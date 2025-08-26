
'''Crop Yield Prediction using Multiple Linear Regression

This project predicts crop yield based on various factors such as crop type, 
year, season, state, area, production, rainfall, fertilizer, and pesticide usage.
- Dataset: Agricultural Crop Yield in Indian States (1997–2020)
- Offline-only
- Author: Tanishka Pal


I researched about projects big techs are funding right now and this project is a simplified version of real-world crop yield prediction systems. 
Companies like Google (AI for Social Good), Microsoft (AI for Earth), etc are actively funding large-scale projects in this space.
'''

# =======================
# 1. Import Libraries
# =======================
import pandas as pd
import numpy as np
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import LabelEncoder, StandardScaler, PolynomialFeatures
from sklearn.preprocessing import OneHotEncoder
from sklearn.compose import ColumnTransformer
from sklearn.linear_model import LinearRegression
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

# ==========================================
# 4. Define categorical and numeric columns
# ==========================================
categorical_features = ['Crop', 'Season', 'State']
numeric_features = ['Annual_Rainfall', 'Temperature', 'Fertilizer']

# =============================
# 5. Features (X) and target (y)
# =============================
X = df.iloc[:, :-1]
y = df.iloc[:, -1].values

# ========================================
# 6. Define categorical and numeric columns
# ========================================
categorical_features = ['Crop', 'Season', 'State']
numeric_features = ['Crop_Year', 'Area', 'Production', 'Annual_Rainfall', 'Fertilizer', 'Pesticide']

# =============================================
# 7. Apply OneHotEncoder on categorical features
# =============================================
ct = ColumnTransformer(
    transformers=[
        ('encoder', OneHotEncoder(handle_unknown='ignore'), categorical_features)
    ],
    remainder='passthrough'   # keeps numeric features as they are
)

# Transform data
X = ct.fit_transform(X)

# ===================
# 8. Train-test split
# ===================
X_train, X_test, y_train, y_test= train_test_split(X, y, test_size= 0.2, random_state=1)

# =============================
# 9. Regression Models
# =============================
def train_linear_regression(X_train, y_train, X_test, y_test):
    """
    Train and evaluate a simple Multiple Linear Regression model.
    I recently learned about 5 ways for efficient feature selection, most used one is Backward elimination, it drops features based on statistical significance (p-values)
    I know the working of it but didn't apply it as of now because the code would get too complex.
    I can add it as future improvement to make the model more effective as it removes less relevant features.
    """
    lr = LinearRegression()
    lr.fit(X_train, y_train)
    y_pred = lr.predict(X_test)
    print("\n--- Linear Regression Results ---")
    print("R2 Score:", r2_score(y_test, y_pred))
    print("RMSE:", np.sqrt(mean_squared_error(y_test, y_pred)))
    return lr

# =============================
# 10. Polynomial Regression Model
# =============================
def train_polynomial_regression(X_train, y_train, X_test, y_test, degree=2):
    """
    Train and evaluate Polynomial Regression model.
    """
    poly = PolynomialFeatures(degree=degree)
    X_train_poly = poly.fit_transform(X_train)
    X_test_poly = poly.transform(X_test)

    lr_poly = LinearRegression()
    lr_poly.fit(X_train_poly, y_train)
    y_pred_poly = lr_poly.predict(X_test_poly)

    print(f"\n--- Polynomial Regression (degree={degree}) Results ---")
    print("R2 Score:", r2_score(y_test, y_pred_poly))
    print("RMSE:", np.sqrt(mean_squared_error(y_test, y_pred_poly)))
    return lr_poly, poly

# ===============
# Train models
# ===============
linear_model = train_linear_regression(X_train, y_train, X_test, y_test)
poly_model, poly_transformer = train_polynomial_regression(X_train, y_train, X_test, y_test, degree=2)

# Example prediction

def example_prediction():
    # Example data (replace with realistic values from your dataset)
    sample = pd.DataFrame([{
        "Crop": "Wheat",
        "Crop_Year": 2020,
        "Season": "Rabi",
        "State": "Uttar Pradesh",
        "Area": 1500,
        "Production": 3000,
        "Annual_Rainfall": 800,
        "Fertilizer": 120,
        "Pesticide": 30
    }])

    # Transform input using same preprocessor
    sample_processed = ct.transform(sample)

    # Predict yield
    prediction = linear_model.predict(sample_processed)
    print("Predicted Yield:", prediction[0])

# just call directly
example_prediction()
