# -*- coding: utf-8 -*-

import streamlit as st
import user
st.title("Lets get you started, Shall we")
st.write(st.session_state)
print(st.session_state)
key=st.session_state["api_key"]
st.info("First a little bit about you")
first_name=st.text_input("First Name",key="first")
last_name=st.text_input("Last Name",key="last")
print(st.session_state)
obj=user.User(st.session_state["api_key"])
#obj.add(first_name,last_name)
#st.markdown("Upload a PDF file, and its content will be copied to a new PDF file on the server.")
st.session_state["api_key"]=key
def make_copy(file):
    with open("data/resume.pdf", "wb") as f:
           f.write(file.read())
    return True
    

uploaded_pdf = st.file_uploader("📤 Upload you resume", type=["pdf"])
if st.button("Proceed"):
    with st.spinner("Please wait"):
        check=make_copy(uploaded_pdf)
        if check and st.session_state["first"] and st.session_state["last"]:
            st.session_state.user=1
            st.info("Now lets move forward")
           

