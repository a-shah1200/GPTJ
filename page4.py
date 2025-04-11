# -*- coding: utf-8 -*-


import streamlit as st
import utils
import ai_package
import user
dic_temp={}
for i in st.session_state:
    dic_temp[i]=st.session_state[i]
st.session_state["api_key"]=dic_temp["api_key"]
api_key=st.session_state["api_key"]
obj=user.User(api_key)
st.title("Resume Helper Bot")

if "messages" not in st.session_state:
    st.session_state.messages = []

for message in st.session_state.messages:
    with st.chat_message(message["role"]):
        st.markdown(message["content"])
# Button to delete thread and Button to save memory
if prompt := st.chat_input("What is up?"):
    with st.chat_message("user"):
       st.markdown(prompt)
    st.session_state.messages.append({"role": "user", "content": prompt})
    query=utils.Prompts().resume_helper()
    files=["data/resume.pdf"]
    agent_convo=ai_package.FileSearchAgent(api_key,"Resume_bot", query)
    with st.chat_message("assistant"):
        if obj.get_thread()==0 or obj.get_thread()=="0":
            message=agent_convo.search(prompt,files)
            obj.put_thread(agent_convo.get_tid())
        else:
            message=agent_convo.search(prompt,files,check=obj.get_thread())
        response=message[-1].content[-1].text.value
        st.write_stream(utils.streamify(response))
    st.session_state.messages.append({"role": "assistant", "content": response})


