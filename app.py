import streamlit as st
import pandas as pd
import numpy as np
import pickle
from sklearn.preprocessing import StandardScaler
st.title("The MEdical Diagnostic Web App")

# Step 1: Load the model
model=open('rfc.pickle', 'rb')
rfc_pickled=pickle.load(model)
model.close()


# Step2: Get the front end user input
pregs=st.slider('Pregnancies',0, 20, step=1)
glucose=st.slider('Glucose',40, 200, 40)
bp=st.slider('BloodPressure',20, 140, 20)
skin=st.slider('SkinThickness', 5,100,5)
insulin=st.slider('Insulin',10, 900, 10)
bmi=st.slider('BMI',15, 70, 15)
dpf=st.slider('DiabetesPedigreeFunction', 0.5, 3.5, 0.5)
age=st.slider('Age', 21, 90, 21)

# Step 3 : convert the inpout data to inout data of the model
data={'Pregnancies':pregs,
    'Glucose':glucose,
    'BloodPressure':bp, 
    'SkinThickness':skin, 
    'Insulin':insulin,
    'BMI':bmi, 
    'DiabetesPedigreeFunction':dpf,
    'Age':age}

# Step4 : Convrt front end user input to model input
input_data=pd.DataFrame([data])
predictions=rfc_pickled.predict(input_data)[0]
if st.button("Predict"):
    if predictions==0:
        st.success('Disease Free')
    if predictions==1:
        st.error("Has Disease")
        
