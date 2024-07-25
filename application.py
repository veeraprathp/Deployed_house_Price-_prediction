import streamlit as st
import pickle
import numpy as np
#from models1 import regressor
#from models1 import scaler
#from altair.vegalite.v4.api import Chart
import pandas as pd
from sklearn.preprocessing import StandardScaler

# Load the pre-trained models
regressor = pickle.load(open("models1/regressor.pkl", 'rb'))
scaler = pickle.load(open("models1/scaler.pickle", 'rb'))

# Set up the Streamlit app
st.title('House Price Prediction App')

# Input fields for user to enter data
MedInc = st.number_input('Median Income', min_value=0.0, format="%.2f")
HouseAge = st.number_input('House Age', min_value=0.0, format="%.2f")
AveRooms = st.number_input('Average Rooms', min_value=0.0, format="%.2f")
AveBedrms = st.number_input('Average Bedrooms', min_value=0.0, format="%.2f")
Population = st.number_input('Population', min_value=0.0, format="%.2f")
AveOccup = st.number_input('Average Occupancy', min_value=0.0, format="%.2f")
Latitude = st.number_input('Latitude', min_value=-90.0, max_value=90.0, format="%.6f")
Longitude = st.number_input('Longitude', min_value=-180.0, max_value=180.0, format="%.6f")

# Button to trigger prediction
if st.button('Predict'):
    # Prepare the input data
    input_data = np.array([[MedInc, HouseAge, AveRooms, AveBedrms ,Population, AveOccup, Latitude, Longitude]])
    
    # Scale the input data
    new_scaled_data = scaler.transform(input_data)
    
    # Make prediction
    result = regressor.predict(new_scaled_data)
    
    # Display the result
    st.write(f'Predicted House Price: ${result[0]:,.2f}')
