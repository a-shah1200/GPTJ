# -*- coding: utf-8 -*-

import streamlit as st
import user
st.title("Lets get you started, Shall we")
key=st.session_state["api_key"]

try:
    del st.session_state.button_name
except:
    pass

if "check_1" not in st.session_state:
    st.session_state.check_1="Proceed"
if st.session_state.check_1=="Proceed":
    st.info("First a little bit about you")
first_name=st.text_input("First Name",key="first")
last_name=st.text_input("Last Name",key="last")


st.session_state["api_key"]=key
def make_copy(file):
    with open("data/resume.pdf", "wb") as f:
           f.write(file.read())
    return True
uploaded_pdf = st.file_uploader("📤 Upload you resume", type=["pdf"])

if st.session_state.check_1=="Continue":
    st.info("Press Continue to Proceed Forward")  
if st.button(st.session_state.check_1):
    if st.session_state.check_1=="Continue":
        obj=user.User(st.session_state["api_key"])
        obj.add(first_name,last_name)
        st.session_state.user=1
    with st.spinner("Please wait"):
        check=make_copy(uploaded_pdf)
        if check and st.session_state["first"] and st.session_state["last"]:
            st.session_state.check_1="Continue"
            st.rerun()
           

