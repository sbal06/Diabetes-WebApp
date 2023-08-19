# -*- coding: utf-8 -*-
"""
Created on Sun Aug 13 22:34:33 2023

@author: Zhizhen L., Shreyes B.
"""

import numpy as np
import pandas as pd
import pickle
import streamlit as st
from streamlit_extras.app_logo import add_logo
import os
from streamlit_extras.no_default_selectbox import selectbox





# Get the current directory of the file (predictive.py)
current_directory2 = os.path.dirname(os.path.realpath(__file__))
# Construct the relative path to the model file within the app's directory
model_filename2 = "diaaid2y.png"
model_path2 = os.path.join(current_directory2, model_filename2)

add_logo(model_path2, height = 100)

st.title("Research-Based Model")

def calculateBMI(weight, height):
    return round(((weight / (height**2)) * 703), 1)



weights = {
    'type_1' : 2,
    'type_2' : 2,
    'gestational': 2,
    'add': 2,
    'double': 4,
    'triple': 6,
    'smoke_alcohol_stress_hp': 0.5,
    'sleep_age_12': 0.5,
    'sleep_age_18': 0.5,

    }

type1 = 0
type2 = 0
gestational = 0


question1 = selectbox("What is your biological sex?", ("Male", "Female"), key = "gender")

if (question1 == "Male"):
    gestational = 0
    
elif (question1 == "Female"):
    subq1 = selectbox("Are you pregnant?", ("Yes", "No", "Unsure"), key = "pregnant")
    if (subq1 == "Yes"):
        subq2 = selectbox("Did you have gestational diabetes in your last pregnancy?", ("Yes", "No", "Unsure"), key = "gestational")
        if (subq2 == "Yes"):
            gestational = gestational + weights['gestational'] # because user said yes
            
        subq3 = selectbox("Is your baby larger than 4000 gm (about 9 pounds)?", ("Yes", "No", "Unsure"), key = "subq3")
        if (subq3 == "Yes"):
            gestational = gestational + weights['add']
            
    elif (subq1 == "No" or subq1 == "Unsure"):
        gestational = 0
        

question2 = st.number_input("What is your age?", min_value = 0, max_value = 120, step = 1)   
     
        
if ((4 <= question2 <= 7) or (10 <= question2 <= 14) ):
    type1 = type1 + weights['double']
    
elif (question2 == 8 or question2 == 9):
    type1 = type1 + weights['add']
    
elif (35 <= question2 <= 45):
    type2 = type2 + weights['add']
    if (question1 == "Female" and (subq1 == "Yes")):
        gestational = gestational + weights['add']
    
    
elif (question2 >= 45):
    type2 = type2 + weights['double']
    if (question1 == "Female" and (subq1 == "Yes")):
        gestational = gestational + weights['double']



question3Weight = st.number_input("Enter your weight in pounds:", min_value = 1, max_value = 400, step = 1 )
question3Height = st.number_input("Enter your height in inches:", min_value = 1, max_value = 200, step = 1)



bmi = calculateBMI(question3Weight, question3Height)

bmi_threshold1 = 25.0
bmi_threshold2 = 30.0

if (bmi_threshold1 <= bmi < bmi_threshold2):
    type1 = type1 + weights['add']
    type2 = type2 + weights['add']
    if (question1 == "Female" and (subq1 == "Yes")):
        gestational = gestational + weights['add'] # I don't know about keep on adding to gestational
        
elif (bmi >= bmi_threshold2):
    type1 = type1 + weights['add']
    type2 = type2 + weights['double']
    if (question1 == "Female" and (subq1 == "Yes")):
        gestational = gestational + weights['double']
        
question4 = st.selectbox("How often do you exercise per week?", ("--", "0-2 days", "3-5 days", "6-7 days"), key = "exercise")

if (question4 == "0-2 days"):
    type1 = type1 + weights['double']
    type2 = type2 + weights['double']
    if (question1 == "Female" and (subq1 == "Yes")):
        gestational = gestational + weights["double"]
        
question5 = selectbox("Do you have a family history of diabetes?", ("Yes", "No", "Unsure"), key = "family")

if (question5 == "Yes"):
    type1 = type1 + weights['add']
    type2 = type2 + weights['triple'] # type2 diabetes has a stronger link to family history
    if (question1 == "Female" and (subq1 == "Yes")):
        gestational = gestational + weights['gestational']
elif (question5 == "Unsure"):
    type1 = type1 + weights['add']
    type2 = type2 + weights['add']
    if (question1 == "Female" and (subq1 == "Yes")):
        gestational = gestational + weights['gestational']
        
        

question6 = selectbox("Do you have a balanced diet?", ("Yes", "Unsure", "No"), key = "balanceddiet")
if (question6 == "No"):
    type1 = type1 + weights['double']
    type2 = type2 + weights['double'] 
    if (question1 == "Female" and (subq1 == "Yes")):
        gestational = gestational + weights['double']
    st.write("Definitely check out our personalized meal plans!")
    


question7 = selectbox("Do you identify as white?", ("Yes", "No"), key = "race")

if (question7 == "Yes"):
    type1 = type1 + weights['add']
    
else:
    if (question1 == "Female" and (subq1 == "Yes")):
        gestational = gestational + weights['double']
    type2 = type2 + weights['add']
    
question8 = selectbox("Do you smoke?", ("Yes", "No"), key = "smoke")
if (question8 == "Yes"):
    type1 = type1 + weights['smoke_alcohol_stress_hp']
    type2 = type2 + weights['smoke_alcohol_stress_hp']
    if (question1 == "Female" and (subq1 == "Yes")):
        gestational = gestational + weights['gestational']
        
        
question9 = selectbox("Do you ingest alcohol?", ("Yes", "No"), key = "alcohol")
if (question9 == "Yes"):
    type1 = type1 + weights['smoke_alcohol_stress_hp']
    type2 = type2 + weights['smoke_alcohol_stress_hp']
    if (question1 == "Female" and (subq1 == "Yes")):
        gestational = gestational + weights['gestational']
        
question9y = selectbox("Have you been stressed lately?", ("Yes", "No"), key = "stress")
if (question9y == "Yes"):
    type1 = type1 + weights['smoke_alcohol_stress_hp']
    type2 = type2 + weights['smoke_alcohol_stress_hp']
    if (question1 == "Female" and (subq1 == "Yes")):
        gestational = gestational + weights['gestational']

    
question10 = selectbox("Do you have high blood pressure?", ("Yes", "No", "Unsure"))
if (question10 == "Yes"):
    type1 = type1 + weights['smoke_alcohol_stress_hp']
    type2 = type2 + weights['smoke_alcohol_stress_hp']
    if (question1 == "Female" and (subq1 == "Yes")):
        gestational = gestational + weights['gestational']
    



question11 = st.number_input("How many hours of sleep do you get?", min_value = 0.0, max_value = 24.0, step = 0.25)
if (question2 <= 12 and question11 < 10):
    type1 = type1 + weights['sleep_age_12']
    type2 = type2 + weights['sleep_age_12']
    if (question1 == "Female" and (subq1 == "Yes")):
        gestational = gestational + weights['sleep_age_12']
        
elif ((12 < question2 < 18) and question11 < 8 ):
    type1 = type1 + weights['sleep_age_12']
    type2 = type2 + weights['sleep_age_12']
    if (question1 == "Female" and (subq1 == "Yes")):
        gestational = gestational + weights['sleep_age_12']

elif (question2 >= 18 and question11 <= 7 ):
    type1 = type1 + weights['sleep_age_12']
    type2 = type2 + weights['sleep_age_12']
    if (question1 == "Female" and (subq1 == "Yes")):
        gestational = gestational + weights['sleep_age_12']
    
    

    
risk_levels = {   # will modify later if we have to.
    'low risk': 5,
    'medium risk': 10,
    'high risk': 15,
    'very high risk': 20,
    }

key_list = list(risk_levels.keys())
values_list = list(risk_levels.values())

diabetesString = ["Type1", "Type2", "Gestational"]
diabetesValue = [type1, type2, gestational]

if (st.button("Diabetes test result")):
    if (not question1 or not question2 or not question3Weight or not question3Height or not question4 or not question5 or not question6 or not question7 or not question8 or not question9 or not question9y or not question10 or not question11):
        st.warning("Please fill out all the information for an accurate prediction!")
    
    else:
        for string, value in zip(diabetesString, diabetesValue): # possible way to iterate two iterables parallelly  
            if (value <= values_list[0] or values_list[0] < value < values_list[1] ):
                st.success(string + " diabetes risk: " + key_list[0])
                
            elif (values_list[1] <= value < values_list[2]):
                st.success(string + " diabetes risk: " + key_list[1])
                
            elif (values_list[2] <= value < values_list[3]):
                st.success(string + " diabetes risk: " + key_list[2])
                
            else:
                st.success(string + " diabetes risk: " + key_list[3] )
    
            
          
    
        
    
         
        
   
        
        
        
          


