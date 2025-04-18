# -*- coding: utf-8 -*-


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
st.title("Resume Helper Bot")

def add_row_pd(df,data):
    new_row = {'values': data, 'del': False}
    df.loc[len(df)] = new_row
    df.to_csv("data/gen_data/memory.csv",index=False)

@st.dialog("Memory is Full")
def remove():
    st.write("Please delete some memory. Click button below to proceed")
    if st.button("Proceed",key="delete"):
        st.session_state["del_check"]=1
        st.switch_page("pages/settings.py")

if "messages" not in st.session_state:
    st.session_state.messages = []

if st.button("Save in Memory"):
    api_key=st.session_state["api_key"]
    df=pd.read_csv("data/gen_data/memory.csv")
    if utils.count_chars(df)>st.session_state["limit_chars"]:
        remove()
    else:
        if len(st.session_state.messages)!=0:
            with st.spinner("Saving data. Please wait"):
                li=st.session_state.messages
                arr=utils.get_values_pd()
                prompt=utils.Prompts().summarize_chats(li,arr)
                agent_sum=ai_package.StructuredAgent(api_key)
                response=agent_sum.get_response("You will help the user", prompt)
                #print(response)
                if len(response.unique_ideas)==0 or len(response.final_message.strip())==0:
                    pass
                else:
                    data=str(response.final_message)
                    add_row_pd(df, data)
                utils.success_message()

for message in st.session_state.messages:
    with st.chat_message(message["role"]):
        st.markdown(message["content"])
        
        
            
if prompt := st.chat_input("What is up?"):
    with st.chat_message("user"):
       st.markdown(prompt)
    st.session_state.messages.append({"role": "user", "content": prompt})
    li=utils.get_values_pd()
    if len(li)==0:
        mem=False
    else:
        mem=True
    query=utils.Prompts().resume_helper(mem)
    files=["data/resume.pdf"]
    agent_convo=ai_package.FileSearchAgent(api_key,"Resume_bot", query)
    with st.chat_message("assistant"):
        with st.spinner("Generating response. Please wait"):
            if obj.get_thread()==0 or obj.get_thread()=="0":
                message=agent_convo.search(prompt,files)
                obj.put_thread(agent_convo.get_tid())
            else:
                message=agent_convo.search(prompt,files,check=obj.get_thread())
            response=message[-1].content[-1].text.value
        st.write_stream(utils.streamify(response))
    st.session_state.messages.append({"role": "assistant", "content": response})


if st.button("Reset Agent"):
    obj.put_thread(0)
    st.rerun()
    
    