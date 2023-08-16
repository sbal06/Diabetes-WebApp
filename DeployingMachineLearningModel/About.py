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

#from streamlit_extras.no_default_selectbox import selectbox
#from streamlit_extras.switch_page_button import switch_page

# Get the current directory of the file (predictive.py)
current_directory = os.path.dirname(os.path.realpath(__file__))
# Construct the relative path to the model file within the app's directory
model_filename = "diaaid.jpg"
model_path = os.path.join(current_directory, model_filename)





st.set_page_config(layout="wide")


def main():
    st.title("About Page")
    add_logo(model_path, height = 100)
  

    st.subheader("On the side, you can find our Machine Learning Model and our Research-Based Model.")
    
    
            
    
    




if __name__ == "__main__":
    main()
    
   #  st.write("Click here to access our research-based model")
   #  if (st.button("Research-Based Model")):
    #     switch_page('Research-Based Model')
        
        
   #  st.write("Click here to access our machine-learning model")
 