import streamlit as st
import pickle
import numpy as np

# Load model
with open("model.pkl", "rb") as file:
    model = pickle.load(file)

st.title("Car Price Prediction 🚗💰")

st.write("Enter the details of the car below to get the predicted price:")

# 🔹 Replace these with your actual model features
year = st.number_input("Year of Manufacture", min_value=1990, max_value=2025, step=1)
present_price = st.number_input("Present Price (in lakhs)", min_value=0.0, step=0.1)
kms_driven = st.number_input("Kilometers Driven", min_value=0, step=500)
owner = st.number_input("Number of Previous Owners", min_value=0, max_value=3, step=1)

fuel_type = st.selectbox("Fuel Type", ["Petrol", "Diesel", "CNG"])
seller_type = st.selectbox("Seller Type", ["Dealer", "Individual"])
transmission = st.selectbox("Transmission", ["Manual", "Automatic"])

# 🔹 Encoding categorical values (adjust if your model used different encoding)
fuel_map = {"Petrol": 0, "Diesel": 1, "CNG": 2}
seller_map = {"Dealer": 0, "Individual": 1}
trans_map = {"Manual": 0, "Automatic": 1}

features = np.array([[
    year,
    present_price,
    kms_driven,
    owner,
    fuel_map[fuel_type],
    seller_map[seller_type],
    trans_map[transmission]
]])

# Predict button
if st.button("Predict Price"):
    prediction = model.predict(features)
    st.success(f"Predicted Selling Price: ₹ {prediction[0]:.2f} lakhs")
