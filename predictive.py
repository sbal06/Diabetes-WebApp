# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""

import numpy as np
import streamlit as st
import pickle
import diabetespredictionwebapp
import aboutpage

def main():
    select_page = st.sidebar.selectbox("Predict or About", ("Predict", "About"))
    
    if (select_page == 'Predict'):
        diabetespredictionwebapp.explore_webapp_page()
        
    elif (select_page == 'About'):
        aboutpage.about()
        

main()