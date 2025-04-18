# -*- coding: utf-8 -*-
"""
Created on Sun Apr  6 17:54:46 2025

@author: Asfahan
"""


import streamlit as st
import utils
import ai_package
import user
import pandas as pd
dic_temp={}
for i in st.session_state:
    dic_temp[i]=st.session_state[i]
st.session_state["api_key"]=dic_temp["api_key"]
api_key=st.session_state["api_key"]
obj=user.User(api_key)
st.title("Interview Practice")
            
if "message1" not in st.session_state:
    st.session_state.message1 = []
       
if prompt := st.chat_input("Let's start our inverview question practice"):
    with st.chat_message("user"):
       st.markdown(prompt)
    st.session_state.message1.append({"role": "user", "content": prompt})
    li=utils.get_values_pd()
    if len(li)==0:
        mem=False
    else:
        mem=True
    df = pd.read_csv('data/Software Questions.csv')  
    sampled_df = df.sample(n=10)
    questions=list(sampled_df["Question"])
    answers=list(sampled_df["Answer"])
    interviewQA=[]
    for i in range(len(questions)):
        interviewQA.append((questions[i],answers[i]))
    query=utils.Prompts().AskInterviewQuestion(interviewQA)
    agent_convo=ai_package.FileSearchAgent(api_key,"Resume_bot", query)
    files = []
    with st.chat_message("assistant"):
        with st.spinner("Generating response. Please wait"):
            if obj.get_thread()==0 or obj.get_thread()=="0":
                message=agent_convo.search(prompt,files)
                obj.put_thread(agent_convo.get_tid())
            else:
                message=agent_convo.search(prompt,files,check=obj.get_thread())
            response=message[-1].content[-1].text.value
        st.write_stream(utils.streamify(response))
    st.session_state.message1.append({"role": "assistant", "content": response})






