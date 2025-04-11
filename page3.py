# -*- coding: utf-8 -*-


import streamlit as st
import user
import utils
import ai_package as ap
import time
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


if int(obj.is_gen_r(check=1))==0:
    with st.spinner("Loading, Please wait"):
        prompt="""Please read the resume and give a professional summary"""
        query=utils.Prompts().professional_summary()
        files=["data/resume.pdf"]
        agent=ap.FileSearchAgent(dic_temp["api_key"],"Professional Summary",prompt)
        message=agent.search(query, files,New=True)
        m_text=message[-1].content[-1].text.value
        obj.is_gen_r(check=0,val=1)
        with open("data/gen_data/professional_summary.txt","w") as f:
            f.write(m_text)
else:
    with open("data/gen_data/professional_summary.txt","r") as f:
        m_text=f.read()

with st.chat_message("assistant"):
        st.info("Professional Summary")
        st.session_state["api_key"]=dic_temp["api_key"]
        st.write(m_text)
       
            
            
            
with st.expander("Daily Motivation",expanded=True):
    off = st.toggle("Off")
    st.session_state["api_key"]=dic_temp["api_key"]
    if off:
        pass
    else:
        if int(obj.is_gen_q(check=1))==0:
            with st.spinner("Loading, Please wait"):
                agent_q=ap.Agent(dic_temp["api_key"], "quotes","Give a motivational quote" )
                query=utils.Prompts().quotes()
                message_q=agent_q.search(query=query,New=True)
                m_text_q=message_q[-1].content[-1].text.value
                obj.is_gen_q(check=0,val=1)
                with open("data/gen_data/quotes.txt","w") as f:
                    f.write(m_text_q)
        else:
           with open("data/gen_data/quotes.txt","r") as f:
               m_text_q=f.read()
        st.write_stream(utils.streamify(m_text_q))
        
        if st.button("New Quote"):
            st.session_state["api_key"]=dic_temp["api_key"]
            obj.is_gen_q(check=0,val=0)
            time.sleep(0.02)
            st.rerun()




