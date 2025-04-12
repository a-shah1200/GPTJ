# -*- coding: utf-8 -*-
"""
Created on Fri Apr 11 04:28:37 2025

@author: Asfahan
"""

import streamlit as st
import pandas as pd
import utils
dic_temp={}
for i in st.session_state:
    dic_temp[i]=st.session_state[i]
st.session_state["api_key"]=dic_temp["api_key"]
api_key=st.session_state["api_key"]
st.title("Settings")
@st.dialog("Memory is Full")
def delete_row_pd(df):
    st.write("Deletion is not reversible. Are you sure ?")
    if st.button("yes"):
        df = df[df['del'] == False]
        df.to_csv("data/gen_data/memory.csv",index=False)
        utils.deleion_message()
        st.rerun()
def make_copy(file):
     with open("data/resume.pdf", "wb") as f:
            f.write(file.read())
     return True

    

with st.expander("Resume"):
    uploaded_pdf = st.file_uploader("📤 Upload you resume", type=["pdf"])
    if st.button("Upload"):
        with st.spinner("Please wait"):
            check=make_copy(uploaded_pdf)
            if check:
                st.info("Success")
                
with st.expander("Memory"):
    df=pd.read_csv("data/gen_data/memory.csv")
    char_count=utils.count_chars(df)
    limit=st.session_state.limit_chars
    prog=min(int((char_count*100)/limit),100)
    my_bar = st.progress(prog, text="Memory Used "+str(prog)+"%")
    edited_pd=st.data_editor(df)
    if st.button("Confirm",key="C1"):  
        delete_row_pd(edited_pd)
    