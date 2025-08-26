# Project Title: Crop Yield Prediction Using Machine Learning

## Student Details

**Name:** Tanishka Pal
**PRN:** 24070126186
**Year:** SY
**Branch:** AIML

---

## Problem Statement

Predicting agricultural crop yields is a challenge for farmers and policymakers due to multiple factors such as soil, rainfall, pesticides, and fertilizers. Manual estimation is often inaccurate and time-consuming.
This project applies **Machine Learning models** to predict crop yield more accurately and efficiently, helping in better planning and decision-making.

---

## Features

* Accepts agricultural data with categorical (state, crop type) and numerical (rainfall, pesticides, yield, etc.) values.
* Automatically handles preprocessing with **One-Hot Encoding**.
* Implements **two regression models**:

  * Linear Regression
  * Random Forest Regression
* Evaluates performance using **R² score** and **RMSE (Root Mean Squared Error)**.
* Provides **sample predictions** for new input data.
* Code is modular, commented, and easy to extend.

---

## Tech Stack

* **Python**
* **Libraries:** pandas, numpy, scikit-learn
* **Models:** Linear Regression, Random Forest Regression

---

## How to Run

1. Clone/download the project folder.
2. Open it in **VS Code**.
3. Install dependencies (if not already installed)
4. Run the script:

   ```bash
   python main.py
   ```
5. The terminal will display **model performance metrics** and an **example prediction**.

---

## Project Structure

Pal_Tanishka/
├── README.md                 
├── src/                      
│   ├── main.py               
│   └── crop_yield.csv        

---

## Demo Screenshot / Output

**Sample Terminal Output:**

PS C:\Users\tanis\FOSS-Recruitment-2025\projects\Pal_Tanishka> & C:/Users/tanis/AppData/Local/Programs/Python/Python313/python.exe c:/Users/tanis/FOSS-Recruitment-2025/projects/Pal_Tanishka/src/main.py
Dataset Preview:
           Crop  Crop_Year       Season  State     Area  Production  Annual_Rainfall  Fertilizer  Pesticide        Yield
0      Arecanut       1997  Whole Year   Assam  73814.0       56708           2051.4  7024878.38   22882.34     0.796087
1     Arhar/Tur       1997  Kharif       Assam   6637.0        4685           2051.4   631643.29    2057.47     0.710435
2   Castor seed       1997  Kharif       Assam    796.0          22           2051.4    75755.32     246.76     0.238333
3      Coconut        1997  Whole Year   Assam  19656.0   126905000           2051.4  1870661.52    6093.36  5238.051739
4  Cotton(lint)       1997  Kharif       Assam   1739.0         794           2051.4   165500.63     539.09     0.420909

Dataset Info:
<class 'pandas.core.frame.DataFrame'>
RangeIndex: 19689 entries, 0 to 19688
Data columns (total 10 columns):
 #   Column           Non-Null Count  Dtype
---  ------           --------------  -----
 0   Crop             19689 non-null  object
 1   Crop_Year        19689 non-null  int64
 2   Season           19689 non-null  object
 3   State            19689 non-null  object
 4   Area             19689 non-null  float64
 5   Production       19689 non-null  int64
 6   Annual_Rainfall  19689 non-null  float64
 7   Fertilizer       19689 non-null  float64
 8   Pesticide        19689 non-null  float64
 9   Yield            19689 non-null  float64
dtypes: float64(5), int64(2), object(3)
memory usage: 1.5+ MB
None

--- Linear Regression Results ---
R2 Score: 0.35518187832221115
RMSE: 858.2438891905881

--- Random Forest Regression Results ---
R2 Score: 0.9511453854178415
RMSE: 236.23535707977857

--- Example Prediction ---
Linear Regression Predicted Yield: 50.006022579434386
Random Forest Predicted Yield: 1.3474522474810553

---

## AI Tools Used

* ChatGPT (for guidance, debugging, and documentation)

---

## Future Improvements

* Use larger and real agricultural datasets for better accuracy.
* Implement feature selection techniques like Backward Elimination to automatically remove less significant features.
* Add more ML models (XGBoost, Neural Networks).
* Build a simple web app/dashboard for farmers to input data and get predictions in real time.

---

## Notes for Reviewers

* Code is fully documented and modular.
* The project runs **offline** (no external API needed).
* Both Linear Regression and Random Forest are implemented for performance comparison.

---

