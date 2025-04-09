# -*- coding: utf-8 -*-


import streamlit as st
import user
import os
import ai_package as ap

try:
    del st.session_state.check_1
except:
    pass
dic_temp={}
for i in st.session_state:
    dic_temp[i]=st.session_state[i]
obj=user.User(st.session_state.api_key)
first,last=obj.get_data()
if "first" not in st.session_state:
    st.session_state["first"]=first
if "last" not in st.session_state:
    st.session_state["last"]=last

string="Welcome, "+str(st.session_state["first"]+" "+ str(st.session_state["last"]))
st.markdown(string)

st.info("Go to the Nav bar and explore the options")




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

if int(obj.is_gen_r(check=1))==0:
    prompt="""Please read the resume and give a professional summary"""
    query="""Analyze the given resume provided in pdf file. Then based upon that give a short professional summary for the user
     Remember following things: 
         1) Focus on strengths
         2) Use professional and formal language
         3) Maximum of 500 charaters
         4) No need to include references for examples, things like this 【4:0†source】"""
    files=["data/resume.pdf"]
    agent=ap.Agent(dic_temp["api_key"],"Professional Summary",prompt)
    message=agent.search_files(query, files,New=True)
    m_text=message[-1].content[-1].text.value
    obj.is_gen_r(check=0,val=1)
    with open("data/gen_data/professional_summary.txt","w") as f:
        f.write(m_text)
else:
    with open("data/gen_data/professional_summary.txt","r") as f:
        m_text=f.read()


st.info("Professional Summary")
string='<div class="container">'+m_text+'</div>'
st.markdown(string, unsafe_allow_html=True)



