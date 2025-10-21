# 🌊 Tsunami Prediction App  

This is a **machine learning web app** built with **Streamlit** that predicts whether a **tsunami is likely** after an earthquake, based on parameters such as magnitude, depth, and coordinates.

---

## 🚀 Features  
✅ Predict tsunami likelihood from earthquake data  
✅ Interactive UI built with Streamlit  
✅ Model trained and optimized using multiple ML algorithms  
✅ Simple to deploy on Streamlit Cloud or Hugging Face  

---

## 📊 Dataset Info  
- **Total Records:** 782  
- **Target Variable:** `tsunami` (1 = tsunami, 0 = no tsunami)  
- **Input Features:**  
  - Magnitude  
  - CDI  
  - MMI  
  - Significance  
  - NST  
  - DMin  
  - Gap  
  - Depth  
  - Latitude  
  - Longitude  
  - Year  
  - Month  

---

## 🧠 Model Details  
- Algorithms Tested: Logistic Regression, Random Forest, SVM, Gradient Boosting  
- **Best Model Selected Automatically** using hyperparameter tuning  
- Final model saved as `best_tsunami_model.pkl`



## 🌋 Example Test Data  

You can use the following **example earthquake events** to test your app:  

Perfect ✅ — including example test data in your `README.md` makes it easier for others (and you) to verify the app instantly.

Below are **three realistic test cases** you can use to check your tsunami prediction model.
These are based on common earthquake patterns that may or may not trigger tsunamis.

---

## 🌋 **Example Test Inputs (for README.md)**

| Test Case                             | Magnitude | CDI | MMI | Significance | NST | DMin | Gap | Depth | Latitude | Longitude | Year | Month | Expected Output           |
| ------------------------------------- | --------- | --- | --- | ------------ | --- | ---- | --- | ----- | -------- | --------- | ---- | ----- | ------------------------- |
| **1. Strong, shallow offshore quake** | 7.8       | 8   | 7   | 900          | 25  | 0.1  | 50  | 20.0  | 37.5     | 142.0     | 2023 | 3     | 🌊 **Tsunami likely**     |
| **2. Deep inland quake**              | 6.0       | 4   | 4   | 400          | 15  | 2.5  | 120 | 300.0 | 35.0     | 100.0     | 2024 | 6     | ✅ **No tsunami expected** |

---

### 🧠 How to Use These Test Cases in `app.py`

You can paste these values directly into your **Streamlit interface** fields.

Example:

```
Magnitude: 7.8  
CDI: 8  
MMI: 7  
Significance: 900  
NST: 25  
DMin: 0.1  
Gap: 50  
Depth: 20  
Latitude: 37.5  
Longitude: 142.0  
Year: 2023  
Month: 3  
```

👉 Simply enter these values in your Streamlit app fields and click **“Predict Tsunami”** to see the results.



## 📊 Output

🌊 Tsunami likely! – when the model predicts 1

✅ No tsunami expected. – when the model predicts 0

### ☁️ Deployment Options

Streamlit Cloud

Hugging Face Spaces

Render

👨‍💻 Author

Adetunji Samuel

💡 Data Engineer | Machine Learning | Physiotherapy Student

🌐 GitHub: sam-aydev

