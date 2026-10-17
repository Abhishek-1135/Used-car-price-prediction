from pathlib import Path
import joblib
import pandas as pd
import streamlit as st

ROOT = Path(__file__).resolve().parent
st.set_page_config(page_title="Used Car Price Prediction", page_icon="🚗", layout="centered")

@st.cache_resource
def get_pipeline():
    return joblib.load(ROOT / "models" / "car_price_pipeline.pkl")

st.title("🚗 Used Car Price Prediction")
st.caption("Demo model trained on synthetic sample data; prices are illustrative, not market valuations.")
with st.form("car_form"):
    brand = st.selectbox("Brand", ["Maruti", "Hyundai", "Honda", "Tata", "Toyota", "Mahindra", "Kia", "Ford"])
    vehicle_age = st.number_input("Vehicle age (years)", 0, 40, 5)
    km_driven = st.number_input("Kilometres driven", 0, 1000000, 40000, step=1000)
    seller_type = st.selectbox("Seller type", ["Individual", "Dealer", "Trustmark Dealer"])
    fuel_type = st.selectbox("Fuel type", ["Petrol", "Diesel", "CNG", "LPG", "Electric"])
    transmission_type = st.selectbox("Transmission type", ["Manual", "Automatic"])
    mileage = st.number_input("Mileage (km/l)", 0.0, 60.0, 18.0, step=0.1)
    engine = st.number_input("Engine (CC)", 0, 10000, 1200, step=100)
    max_power = st.number_input("Maximum power (bhp)", 0.0, 1000.0, 80.0)
    seats = st.number_input("Seats", 1, 20, 5)
    submit = st.form_submit_button("Predict Selling Price", use_container_width=True)

if submit:
    input_data = pd.DataFrame({
        "brand": [brand],
        "vehicle_age": [vehicle_age],
        "km_driven": [km_driven],
        "seller_type": [seller_type],
        "fuel_type": [fuel_type],
        "transmission_type": [transmission_type],
        "mileage": [mileage],
        "engine": [engine],
        "max_power": [max_power],
        "seats": [seats],
    })
    try:
        prediction = get_pipeline().predict(input_data)
        st.success(f"Predicted Selling Price: ₹{max(0, float(prediction[0])):,.2f}")
    except Exception as e:
        st.error(f"Prediction failed: {e}")
