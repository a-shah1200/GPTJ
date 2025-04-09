# -*- coding: utf-8 -*-


import streamlit as st
import user
import os
import ai_package as ap
dic_temp={}
for i in st.session_state:
    dic_temp[i]=st.session_state[i]
obj=user.User(st.session_state.api_key)
first,last=obj.get_data()
if "first" not in st.session_state:
    st.session_state["first"]=first
if "last" not in st.session_state:
    st.session_state["last"]=last

st.write(st.session_state)
string="Welcome, "+str(st.session_state["first"]+" "+ str(st.session_state["last"]))
st.markdown(string)

st.write("Go to the Nav bar and explore the options")


"""if len(os.listdir("data/Progress"))==0:

else:
    # Display the progress"""
    


# Custom CSS for positioning the container box
st.markdown("""
    <style>
        .container {
            position: fixed;
            bottom: 100px;
            left: 50%;
            transform: translateX(-50%);
            background-color: rgba(0, 0, 0, 0.7);
            color: white;
            padding: 20px;
            border-radius: 20px;
            box-shadow: 0 4px 8px rgba(0, 0, 0, 0.2);
            font-size: 18px;
            max_width: 80%;
            width: auto;
            
        }
    </style>
""", unsafe_allow_html=True)

#prompt=""" """
#query="""Analyze the given resume provided in pdf file. Then based upon that give a short professional summary for the user
#Remember on following things: 
 #   1) Focus on strengths
  #  2) Use professional and formal language
   # 3) Maximum of 500 charaters"""
#files=["data/resume.pdf"]
#agent=ap.Agent(dic_temp["api_key"],"Professional Summary",prompt)
#messages=agent.search_files(query, files,new=True)
# Text inside the container
st.markdown('<div class="container">This is the text inside the container box!This is the text inside the container boxThis is the text inside the container boxThis is the text inside the container boxThis is the text inside the container boxThis is the text inside the container boxThis is the text inside the container boxThis is the text inside the container box</div>', unsafe_allow_html=True)



