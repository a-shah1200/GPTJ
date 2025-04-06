# -*- coding: utf-8 -*-


import streamlit as st
import user

obj=user.User(st.session_state.api_key)
if "first" not in st.session_state:
    st.session_state["first"]="H"
if "last" not in st.session_state:
    st.session_state["last"]='E'
print(st.session_state)
st.write(st.session_state)
string="Welcome, "+str(st.session_state["first"]+ str(st.session_state["last"]))
st.markdown(string)


