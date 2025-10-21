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

---

## ⚙️ Installation  

### 1️⃣ Clone Repository  
```bash



## 🌋 Example Test Data  

You can use the following **example earthquake events** to test your app:  

| Scenario | Magnitude | CDI | MMI | Significance | NST | DMin | Gap | Depth | Latitude | Longitude | Year | Month | Expected Result |
|-----------|------------|-----|-----|---------------|------|-------|------|---------|-----------|------------|------|--------|----------------|
| 🟢 Small local quake | 4.5 | 2 | 2 | 100 | 15 | 0.5 | 90 | 30 | 36.5 | 140.8 | 2024 | 2 | ✅ No tsunami expected |
| 🟡 Moderate quake near coast | 6.3 | 4 | 4 | 400 | 25 | 0.1 | 70 | 15 | 38.2 | 142.5 | 2023 | 11 | ⚠️ Borderline — could cause small tsunami |
| 🔴 Severe deep ocean quake | 8.2 | 7 | 7 | 900 | 60 | 0.05 | 45 | 10 | -8.5 | 107.5 | 2025 | 5 | 🌊 Tsunami likely! |

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

