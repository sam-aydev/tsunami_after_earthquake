import streamlit as st
import joblib
import numpy as np

st.title("🌊 Earthquake → Tsunami Prediction App")

model = joblib.load("best_tsunami_model.pkl")

magnitude = st.number_input("Magnitude", 0.0, 10.0, 5.0)
cdi = st.number_input("CDI", 0, 10, 3)
mmi = st.number_input("MMI", 0, 10, 3)
sig = st.number_input("Significance", 0, 1000, 500)
nst = st.number_input("NST", 0, 100, 10)
dmin = st.number_input("DMin", 0.0, 10.0, 0.2)
gap = st.number_input("Gap", 0.0, 180.0, 90.0)
depth = st.number_input("Depth", 0.0, 1000.0, 10.0)
latitude = st.number_input("Latitude", -90.0, 90.0, 10.0)
longitude = st.number_input("Longitude", -180.0, 180.0, 100.0)
year = st.number_input("Year", 1900, 2100, 2025)
month = st.number_input("Month", 1, 12, 5)

if st.button("Predict Tsunami"):
    features = np.array([[magnitude, cdi, mmi, sig, nst, dmin, gap, depth, latitude, longitude, year, month]])
    prediction = model.predict(features)[0]
    
    if prediction == 1:
        st.error("🌊 Tsunami likely!")
    else:
        st.success("✅ No tsunami expected.")
