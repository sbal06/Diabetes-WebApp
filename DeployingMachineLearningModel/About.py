# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""


import numpy as np
import streamlit as st
import pickle
import os
import xgboost
import matplotlib.pyplot as plt
from streamlit_extras.app_logo import add_logo
from PIL import Image
from streamlit_extras.colored_header import colored_header

#from streamlit_extras.no_default_selectbox import selectbox
#from streamlit_extras.switch_page_button import switch_page

# Get the current directory of the file (predictive.py)
current_directory = os.path.dirname(os.path.realpath(__file__))
# Construct the relative path to the model file within the app's directory
model_filename = "diaaid2-removebg-preview.png"
model_path = os.path.join(current_directory, model_filename)


st.set_page_config(layout="wide",
                   page_title = "Multipage App")


st.markdown(
    """
    <style>
    .css-1jc7ptx, .e1ewe7hr3, .viewerBadge_container__1QSob,
     {
        display: none;
    }
    </style>
    """,
    unsafe_allow_html=True
)


def main():
    st.title("About Page")
    add_logo(model_path, height = 100)
    
    st.markdown(
"""
About the two models:
- DiaAid’s Machine Learning Model was trained on the publicly available "Diabetes Dataset" by Ahlam Rashid, available from Mendeley Data (doi: 10.17632/wj9rwkp9c2.1), licensed under a Creative Commons Attribution 4.0 International License (CC BY 4.0). The data is originally from the Iraqi society, which was acquired from the laboratory of Medical City Hospital and the Specialized Center for Endocrinology and Diabetes-Al-Kindi Hospital. The Mendeley Dataset contained 1000 data entries and 14 column values: ID, gender, age, urea value, creatinine ratio(Cr), hemoglobin A1C, cholesterol, triglycerides, HDL, LDL, VLDL, BMI, and an output class (diabetes, predict-diabetes, or not diabetic). All data besides the patient number and ID was utilized in the training of the model since it is not relevant to the prediction of diabetes.
- To enhance accessibility, we have also engineered a Research-Based Model in Python that evaluates the inputs of day-to-day terminologies. We examined the most common and impactful risk factors of type 1, type 2, and gestational diabetes, and we valued this model as accurate according to the test trial by the 2Life Communities at Brighton, MA. 

Results of both models will be presented in four categories: low, medium, high, and very high risks. 
The Research Based Model will predict one of the above four classes for three types of diabetes - Type 1, Type 2, Gestational Diabetes.

"""
)
    
 
    

    colored_header(
        label = "Disclaimer",
        description = "The model presented here serves as a tool to suggest the need for a blood test. However, it should not be considered a replacement for actual blood tests in diagnosing diabetes or substituting medical advice. This research-based machine learning model is not FDA-approved and may contain inaccuracies. Furthermore, the machine learning model was trained using a dataset of 1000 data entries and was not continuously trained on private data, which may introduce additional inaccuracies. DiaAid also acknowledges the diversity of race, ethnicity, and gender, but due to simplicity, these factors are constrained in our model. We understand that user inputs are personal and confidential. By using our products, users grant permission to DiaAid to analyze such information, with an assurance of lawful and non-exploitative data usage. The license for the Machine Learning model is on the GitHub page.",
        color_name = 'red-70')
    
    mobileString = "If you are on a mobile device, click the arrow at the top left of your screen to access the models"
    
    st.write(f"You will be able to locate our Machine Learning Model, Research Based Model, and Personalized Meal Plans on the left side of your screen. **{mobileString}**.")
    


if __name__ == "__main__":
    main()
    
 