# -*- coding: utf-8 -*-


import streamlit as st
import user
st.title("JobGPT : sunglasses:")

st.write("Before Moving on, please enter your openAI API key")

api=st.text_input("API key", type="password",key="api_key")
obj=user.User(st.session_state.api_key)
if st.button("Proceed"):
    if obj.check():
        st.session_state.user=1
    else:
        st.write("Oh it seems you are new here cowboy, Lets get you registered")
        st.session_state.user=2
        


