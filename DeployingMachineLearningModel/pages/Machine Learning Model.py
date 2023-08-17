# -*- coding: utf-8 -*-
"""
Created on Sun Aug 13 22:35:19 2023

@author: Zhizhen L., Shreyes B.
"""

import numpy as np
import pandas as pd
import pickle
import streamlit as st
import os
from streamlit_extras.app_logo import add_logo






# Get the current directory of the file (predictive.py)
current_directory = os.path.dirname(os.path.realpath(__file__))
# Construct the relative path to the model file within the app's directory
model_filename = "xgb_model.pkl"
model_path = os.path.join(current_directory, model_filename)


# Get the current directory of the file (predictive.py)
current_directory2 = os.path.dirname(os.path.realpath(__file__))
# Construct the relative path to the model file within the app's directory
model_filename2 = "diaaid2y.png"
model_path2 = os.path.join(current_directory2, model_filename2)

add_logo(model_path2, height = 100)

# Load the model
with open(model_path, 'rb') as f:
    trained_model = pickle.load(f)
        
        
def diabetes_prediction(user_input):
    user_input = list(user_input)
    user_input = [user_input]
    user_input_np = np.asarray(user_input)
    
    predicted_probabilities = trained_model.predict_proba(user_input_np)
    
    diabetes_probability = predicted_probabilities[0, 2]*100
    
    
    
    return diabetes_probability 
def format_input(Number):
    formatted_value = "{:.1f}".format(Number)
    
    return formatted_value
    


    # st.markdown()
    

st.title('Diabetes Prediction Interactive Web App')
    
    # a small description
st.write("""### Input your health information to predict the chance of diabetes""")
st.write("""### It is important to note that not all information can be filled without medical tests. Read the About section for a disclaimer about the model.""")
    
    # getting input data
    
Gender = st.selectbox("Select Sex", ("Female", "Male"), key="gender_select")
gender_code = 0 if "Female" else 1
st.write("Selected Gender is " + str(Gender))
    
    
Age = st.slider("Age", 0, 100)
st.write("Selected Age is " + str(Age))
    

Urea = st.slider("Urea value in mmol/L", min_value = 0.0, max_value = 10.0, step = 0.1)
st.write(f"Selected value is: {format_input(Urea)}")
    
Cr = st.slider("Creatinine Ratio in mmol/L", min_value = 0.0, max_value = 200.0, step = 0.1)
st.write(f"Selected value is: {format_input(Cr)}")
    
HbA1c = st.slider("Hemoglobin A1c percentage", min_value = 0.0, max_value = 15.0, step = 0.1)
st.write(f"Selected value is: {format_input(HbA1c)}")
    
Chol = st.slider("Cholesterol level in mmol/L", min_value = 0.0, max_value = 15.0, step = 0.1)
st.write(f"Selected value is: {format_input(Chol)}")
    
TG  = st.slider("Triglycerides in mmol/L", min_value = 0.0, max_value = 10.0, step = 0.1)
st.write(f"Selected value is: {format_input(TG)}")
    
HDL = st.slider("HDL in mmol/L", min_value = 0.0, max_value = 5.0, step = 0.1)
st.write(f"Selected value is: {format_input(HDL)}")
    
LDL = st.slider("LDL in mmol/L", min_value = 0.0, max_value = 5.0, step = 0.1)
st.write(f"Selected value is: {format_input(LDL)}")
    
VLDL = st.slider("VLDL in mmol/L", min_value = 0.0, max_value = 10.0, step = 0.1)
st.write(f"Selected value is: {format_input(VLDL)}")
    
BMI = st.slider("Body Mass Index", 0, 50)
st.write(f"Selected value is: {format_input(BMI)}")
    
    
        
diabetes_pred = ''
    
    
    # to balance out the feature importance
    
   
    
 # lifestyle
if (diabetes_pred == ''):
     # if ((25 <= BMI <= 29) and HbA1c <= 5.8):
         # diabetes_pred = diabetes_prediction((gender_code, Age, Urea, Cr, HbA1c, Chol, TG, HDL, LDL, VLDL, 24)) + 25
     diabetes_pred = diabetes_prediction((gender_code, Age, Urea, Cr, HbA1c, Chol, TG, HDL, LDL, VLDL, BMI))
         
       
Question_1 = st.selectbox("Family history of diabetes", ("Yes", "Not sure", "No"), key = "history")
st.write("Selected option is ", Question_1)
 
if (Question_1 == "Yes"):
      diabetes_pred = diabetes_pred + 2
elif (Question_1 == "No"):
    if (diabetes_pred > 5):
        diabetes_pred = diabetes_pred - 2
         
         
if (HbA1c > 6.5 and BMI >= 30):
     diabetes_pred = diabetes_pred + 10
     
elif (HbA1c > 6.5 and (25 < BMI < 30)):
     diabetes_pred = diabetes_pred + 5
     
     

     
     
if (st.button('Diabetes Test Result')):
    if (not Gender or not Age or not Chol or not HbA1c or not HDL or not LDL or not VLDL or not BMI):
         st.warning("Please fill out all information")
         
         
    else:
 
        if (75 < diabetes_pred  < 100):
            st.success("Level 4 - Very High Risk")
        elif (50 < diabetes_pred < 75):
            st.success("Level 3 - High Risk")
        elif (25 < diabetes_pred < 50):
            st.success("Level 2 - Moderate Risk")
        elif (0 < diabetes_pred < 25 ):
            st.success("Level 1 - Low risk")
            
       #  st.success(diabetes_pred)
     
     