#save the model
import streamlit as st
import joblib
import numpy as np
#Load the model
model = joblib.load("age_charges_model.pkl")

#streamlit app
st.title("Prediction of Charges by age")

#Building the input column
age = st.number_input("Enter Age", min_value = 18, max_value = 100, step = 1)
if st.button("Predict Charges"):
    exog = np.array([[1, age]])
    prediction = model.predict(exog)[0]
    st.success(f"Predicted Charges: ${prediction:.2f}")