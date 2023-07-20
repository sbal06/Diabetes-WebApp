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
import os

def main():
    select_page = st.sidebar.selectbox("Predict or About", ("Predict", "About"), key = "option1")

    
    if (select_page == 'Predict'):
        diabetespredictionwebapp.explore_webapp_page()
        
    elif (select_page == 'About'):
        aboutpage.about()
        
        
# change this
if __name__ == '__main__':
    main()