# 🚗 Car Price Prediction API

This project builds a **Machine Learning API** that predicts the price of a car based on its specifications.
The model is trained using **XGBoost** and deployed using **FastAPI**.

---

## 📌 Project Overview

The goal of this project is to create an **end-to-end machine learning system** that:

* Cleans and preprocesses car dataset features
* Encodes categorical variables using `OneHotEncoder`
* Trains a regression model using **XGBoost**
* Saves the model as a **pipeline**
* Deploys the model through a **FastAPI REST API**

Users can send car information and receive the **predicted car price**.

---

## 📊 Dataset

The dataset contains **19,000+ car listings** with features such as:

* Manufacturer
* Category
* Leather interior
* Fuel type
* Engine volume
* Gear box type
* Drive wheels
* Mileage
* Cylinders
* Doors
* Wheel
* Color
* Airbags
* Levy
* Production year

### Feature Engineering

A new feature was created:

```
Car_Age = Current Year - Production Year
```

---

## ⚙️ Machine Learning Pipeline

The model is trained using a **Scikit-Learn pipeline**:

```
ColumnTransformer
   ├── OneHotEncoder (categorical features)
   └── Numerical features
            ↓
        XGBoost Regressor
```

This ensures that **the same preprocessing is applied during training and prediction**.

---

## 📈 Model Performance

| Metric                    | Score    |
| ------------------------- | -------- |
| R² Score                  | **0.77** |
| Mean Absolute Error (MAE) | **4206** |

The model predicts car prices with an **average error of approximately $4206**.

---

## 🚀 API Endpoint

### POST `/predict`

Predicts the price of a car.

### Example Request

```json
{
  "Manufacturer": "HYUNDAI",
  "Category": "Sedan",
  "Leather interior": "Yes",
  "Fuel type": "Petrol",
  "Engine volume": 2.4,
  "Gear box type": "Automatic",
  "Drive wheels": "Front",
  "Mileage": 216118,
  "Cylinders": 4,
  "Doors": 4,
  "Wheel": "Left wheel",
  "Color": "Grey",
  "Airbags": 12,
  "Levy": 751,
  "Car_Age": 11
}
```

### Example Response

```json
{
  "Predicted Price": 50613
}
```

---

## 🛠 Technologies Used

* Python
* Pandas
* NumPy
* Scikit-learn
* XGBoost
* FastAPI
* Uvicorn
* Joblib

---

## 📂 Project Structure

```
car-price-prediction
│
├── app.py
├── car_price_pipeline.pkl
├── requirements.txt
├── README.md
│
├── data/
│   └── car_price_prediction.csv
│
└── notebook/
    └── train_model.ipynb
```

---

## ▶️ Running the API Locally

Install dependencies:

```
pip install -r requirements.txt
```

Run the FastAPI server:

```
uvicorn app:app --reload
```

Open API documentation:

```
http://127.0.0.1:8000/docs
```

---

## 🔮 Future Improvements

* Hyperparameter tuning
* Feature importance visualization
* Model monitoring
* Frontend interface for predictions

---

## 👨‍💻 Author

**Ashish Jadhav**

Aspiring Machine Learning Engineer building practical ML systems and APIs.
