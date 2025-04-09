# -*- coding: utf-8 -*-


import streamlit as st
import user
st.title("JobGPT : sunglasses:")

st.write("Before Moving on, please enter your openAI API key")

api=st.text_input("API key", type="password",key="api_key")
obj=user.User(st.session_state.api_key)
if "button_name" not in st.session_state:
    st.session_state.button_name = "Proceed"
if st.session_state.button_name=="Lets Get Registered":
    st.write("Oh it seems you are new here cowboy, Lets get you registered")
if st.button(st.session_state.button_name):
    if st.session_state.button_name=="Lets Get Registered":
        st.session_state.user=2
    if obj.check():
        st.session_state.user=1
        st.rerun()
    else:
        st.session_state.button_name="Lets Get Registered"
        st.rerun()
        




