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
from streamlit_extras.stylable_container import stylable_container
from streamlit_extras.add_vertical_space import add_vertical_space






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
    
st.markdown(
    """
    <style>
    .css-1jc7ptx, .e1ewe7hr3, .viewerBadge_container__1QSob,
    .styles_viewerBadge__1yB5_, .viewerBadge_link__1S137,
    .viewerBadge_text__1JaDK {
        display: none;
    }
    </style>
    """,
    unsafe_allow_html=True
)
        
        
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
    

st.title('Machine Learning Model')
    
    # a small description
    # getting input data
    
biologicalSex = st.selectbox("Select Biological Sex", ("Female", "Male"), key="gender_select")
gender_code = 0 if "Female" else 1
st.write("Selected Biological Sex is " + str(biologicalSex))

add_vertical_space(2)
Age = st.slider("Age", 0, 100)
st.write("Selected Age is " + str(Age))
add_vertical_space(2)

Urea = st.slider("Urea value in mmol/L", min_value = 0.0, max_value = 10.0, step = 0.1)
st.write(f"Selected value is: {format_input(Urea)}")
add_vertical_space(2)


Cr = st.slider("Creatinine Ratio in mmol/L", min_value = 0.0, max_value = 200.0, step = 0.1)
st.write(f"Selected value is: {format_input(Cr)}")
add_vertical_space(2)
    
HbA1c = st.slider("Hemoglobin A1c percentage", min_value = 0.0, max_value = 15.0, step = 0.1)
st.write(f"Selected value is: {format_input(HbA1c)}")
add_vertical_space(2)

    
Chol = st.slider("Cholesterol level in mmol/L", min_value = 0.0, max_value = 15.0, step = 0.1)
st.write(f"Selected value is: {format_input(Chol)}")
add_vertical_space(2)
    
TG  = st.slider("Triglycerides in mmol/L", min_value = 0.0, max_value = 10.0, step = 0.1)
st.write(f"Selected value is: {format_input(TG)}")
add_vertical_space(2)
    
HDL = st.slider("HDL in mmol/L", min_value = 0.0, max_value = 5.0, step = 0.1)
st.write(f"Selected value is: {format_input(HDL)}")
add_vertical_space(2)
    
LDL = st.slider("LDL in mmol/L", min_value = 0.0, max_value = 5.0, step = 0.1)
st.write(f"Selected value is: {format_input(LDL)}")
add_vertical_space(2)
    
VLDL = st.slider("VLDL in mmol/L", min_value = 0.0, max_value = 10.0, step = 0.1)
st.write(f"Selected value is: {format_input(VLDL)}")
add_vertical_space(2)
    
BMI = st.slider("Body Mass Index", 0, 50)
st.write(f"Selected value is: {format_input(BMI)}")
add_vertical_space(2)
    
        
diabetes_pred = ''
    
    
    # to balance out the feature importance
    
   
    
 # lifestyle
if (diabetes_pred == ''):
     # if ((25 <= BMI <= 29) and HbA1c <= 5.8):
         # diabetes_pred = diabetes_prediction((gender_code, Age, Urea, Cr, HbA1c, Chol, TG, HDL, LDL, VLDL, 24)) + 25
     diabetes_pred = diabetes_prediction((gender_code, Age, Urea, Cr, HbA1c, Chol, TG, HDL, LDL, VLDL, BMI))
         
       
Question_1 = st.selectbox("Family history of diabetes:", ("Yes", "Not sure", "No"), key = "history")
st.write("Selected option is ", Question_1)
add_vertical_space(2)

if (Question_1 == "Yes"):
      diabetes_pred = diabetes_pred + 2
elif (Question_1 == "No"):
    if (diabetes_pred > 5):
        diabetes_pred = diabetes_pred - 2
         
         
if (HbA1c > 6.5 and BMI >= 30):
     diabetes_pred = diabetes_pred + 10
     
elif (HbA1c > 6.5 and (25 < BMI < 30)):
     diabetes_pred = diabetes_pred + 6
     
    
    
# Jai Ram
elif (5.7 < HbA1c < 6.5 and (25 < BMI < 30)):
     diabetes_pred = diabetes_pred + 5
     
     
     
with stylable_container(
    key="red_button",
    css_styles="""
        button {
            background-color: red;
            color: white;
            border-radius: 20px;
        }
        """,
):
        machine_learning_based_model = st.button("Diabetes Test Result")
     
     
      
   
     
if (machine_learning_based_model):
    if (not biologicalSex or not Age or not Chol or not HbA1c or not HDL or not LDL or not VLDL or not BMI):
         st.warning("Please fill out all the information for a more accurate prediction!")
         
         
    else:
 
        if (75 < diabetes_pred  < 100):
            st.success("Level 4 - Very High Risk")
        elif (50 < diabetes_pred < 75):
            st.success("Level 3 - High Risk")
        elif (25 < diabetes_pred < 50):
            st.success("Level 2 - Moderate Risk")
        elif (0 < diabetes_pred < 25 ):
            st.success("Level 1 - Low risk")
            


st.write("The model results will be presented in four categories: Low Risk, Moderate Risk, High Risk, and Very High Risk. ")
            
        
            
       #  st.success(diabetes_pred)
     
     