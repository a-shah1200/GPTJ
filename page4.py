# -*- coding: utf-8 -*-
"""
Created on Sun Apr  6 17:54:39 2025

@author: Asfahan
"""

import streamlit as st
st.write("page4")
dic_temp={}
for i in st.session_state:
    dic_temp[i]=st.session_state[i]
st.session_state["api_key"]=dic_temp["api_key"]
