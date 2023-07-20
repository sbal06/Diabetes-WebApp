# -*- coding: utf-8 -*-
"""
Created on Mon Jul 17 13:08:54 2023

@author: shrey
"""

import numpy as np
import pickle
import streamlit as st
import os


# creating a function for prediction
current_directory = os.path.dirname(os.path.realpath(r"C:\Users\shrey\Downloads\DeployingMachineLearningModel\trained_model.sav"))
model_path = os.path.join(current_directory, "trained_model.sav")
load_model = pickle.load(open(model_path, 'rb'))


current_directory2 = os.path.dirname(os.path.realpath(r"C:\Users\shrey\Downloads\DeployingMachineLearningModel\best_estimator.pkl"))
model_path2 = os.path.join(current_directory, "best_estimator.pkl")
load_model2 = pickle.load(open(model_path2, 'rb'))

def diabetes_prediction(user_input):
    user_input = list(user_input)
    user_input = [user_input]
    user_input_np = np.asarray(user_input)
    
    prediction = load_model2.predict(user_input_np)
    
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
    
    
# if __name__ == 'explore_webapp_page':
    #explore_webapp_page()
        

