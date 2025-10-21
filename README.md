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


## 🧮 Example Input
Feature	Example
Magnitude	7.1
Depth	20.0
Latitude	37.5
Longitude	142.0
Month	3
Year	2024


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

