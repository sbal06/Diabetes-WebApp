# -*- coding: utf-8 -*-
"""
Created on Thu Jul 20 13:55:51 2023

@author: shrey
"""


import numpy as np
import streamlit as st
import pickle
import os

# Get the current directory of the file (predictive.py)
current_directory = os.path.dirname(os.path.realpath(__file__))

# Construct the relative path to the model file within the app's directory
model_filename = "trained_model.sav"
model_path = os.path.join(current_directory, model_filename)

model2_filename = 'best_estimator.pkl'
model2_path = os.path.join(current_directory, model2_filename)

# Load the model
with open(model_path, 'rb') as f:
    trained_model = pickle.load(f)
    
with open(model2_path, 'rb') as f:
    best_estimator = pickle.load(f)
    



def main():
    select_page = st.sidebar.selectbox("Predict or About", ("Predict", "About"), key = "option1")

    
    if (select_page == 'Predict'):
        explore_webapp_page()
        
    elif (select_page == 'About'):
        about()
        
        
def diabetes_prediction(user_input):
    user_input = list(user_input)
    user_input = [user_input]
    user_input_np = np.asarray(user_input)
    
    prediction = best_estimator.predict(user_input_np)
    
    if (prediction[0] == 0):
        return "Person is not diabetic. Recommendation plans: "
    
    elif (prediction[0] == 1):
        return "Person has a high-liklihood of being diabetic. Predict-Diabetic."
    
    return "Person is diabetic"

def format_input(Number):
    formatted_value = "{:.1f}".format(Number)
    
    return formatted_value
    

def explore_webapp_page():
    # st.markdown()
    

    st.title('Diabetes Prediction Interactive Web App')
    
    # a small description
    st.write("""### You can input values or toggle the sliders to desired values.""")
    st.write("""### It is important to note that not all information can be filled without medical tests. Read the About section for a disclaimer about the model.""")
    
    # getting input data
    
    Gender = st.selectbox("Select Gender", ("Female", "Male"), key="gender_select")
    gender_code = 0 if "Female" else 1
    st.write("Selected Gender is " + str(Gender))
    
    Age = st.slider("Select Age", 0, 100)
    st.write("Selected Age is " + str(Age))
    
    Urea = st.slider("Urea Value in mmol/L", min_value = 0.0, max_value = 10.0, step = 0.1)
    st.write(f"Selected value is: {format_input(Urea)}")
    
    Creatinine_Ratio = st.slider("Creatinine Ratio in mmol/L", 0, 900)
    st.write(f"Selected value is: {format_input(Creatinine_Ratio)}")
    
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
 
        
    if (st.button('Diabetes Test Result')):
        if not Gender or not Age or not Chol or not HbA1c or not HDL or not LDL or not VLDL or not BMI:
            st.warning("Please fill out all information")
        
        else:
            diabetes_pred = diabetes_prediction((gender_code, Age, Urea, Creatinine_Ratio, HbA1c, Chol, TG, HDL, LDL, VLDL, BMI))

            
        
    st.success(diabetes_pred)
     

def about():
    st.title("About Page")
    st.subheader("About the Mendeley Dataset")
    
        
# change this
if __name__ == '__main__':
    main()