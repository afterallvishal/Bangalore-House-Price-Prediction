import streamlit as st
import pickle
import pandas as pd





#load model

model=pickle.load(open("RidgeModel.pkl",'rb'))

#load locations
locations = pickle.load(open('locations.pkl', 'rb'))

st.title("Bangalore House Price Prediction")

st.write("Enter the Details to Predict the Estimated Price")

#user input

location=st.text_input('Enter Location').strip()

total_sqft= st.number_input('Total Square Feet',min_value=450,max_value=10000)
st.info("For better predictions, enter Total Square Feet value within the range of 450 to 10000.")

bath=st.number_input('Number of Bathrooms',min_value=1)

bhk=st.number_input('Number of BHK', min_value=1)

#prediction

if st.button('Predict Price'):

    input_data=pd.DataFrame({
        'location':[location],
        'total_sqft':[total_sqft],
        'bath':[bath],
        'bhk':[bhk]
    })

    if location not in locations:
         st.warning("Location not found. Please enter a valid Bangalore location.")
    try:

        prediction=model.predict(input_data)
        Price=prediction[0]

        # Negative prediction handling
        if Price < 0:
            st.warning("Please enter a realistic house size and location.")
        elif Price >= 100:
            price_crores = Price / 100
            st.success(f'Estimated Price : ₹{price_crores:.2f} Crores')
        else:
            st.success(f'Estimated House Price : ₹{Price:.2f} Lakhs')

    except ValueError:
        st.error("Invalid Location ! Please enter a Valid Location")
