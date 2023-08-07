# -*- coding: utf-8 -*-
"""
Created on Thu Jul 20 13:55:51 2023

@author: shrey
"""


import numpy as np
import streamlit as st
import pickle
import os
import xgboost
import matplotlib.pyplot as plt

# Get the current directory of the file (predictive.py)
current_directory = os.path.dirname(os.path.realpath(__file__))

# Construct the relative path to the model file within the app's directory
model_filename = "xgb_model.pkl"
model_path = os.path.join(current_directory, model_filename)



# Load the model
with open(model_path, 'rb') as f:
    trained_model = pickle.load(f)
    

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
    
    predicted_probabilities = trained_model.predict_proba(user_input_np)
    
    diabetes_probability = predicted_probabilities[0, 2]*100
    
    return diabetes_probability

def format_input(Number):
    formatted_value = "{:.1f}".format(Number)
    
    return formatted_value
    

def explore_webapp_page():
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
        
    
            
   
        
        
    if (st.button('Diabetes Test Result')):
        if not Gender or not Age or not Chol or not HbA1c or not HDL or not LDL or not VLDL or not BMI:
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
                
           # st.success(diabetes_pred)

def about():
    st.title("About Page")
    st.subheader("About the Model")
    st.write("Hi")
   # show_feature_importance_plot(best_estimator)
    

#def show_feature_importance_plot(model):
    #classifier_list = ['GENDER', 'AGE', 'UREA', 'Cr', 'Hb1AC', 'Chol', 'TG', 'HDL', 'LDL', 'VLDL', 'BMI', 'CLASS']

   # importances = rf_best.feature_importances_

    #indices = np.argsort(importances)
    
   # fig, ax = plt.subplots(figsize = (8,6))
   ### ax.barh(range(len(indices)), importances[indices], color = 'b', align = 'center')
   # ax.set_yticks(range(len(indices)), [classifier_list[i] for i in indices])
   ## ax.set_xlabel("Relative Importances")
    #st.pyplot(fig)
        
# change this
if __name__ == '__main__':
    main()