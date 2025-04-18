# -*- coding: utf-8 -*-
"""
Created on Wed Apr  9 13:40:54 2025

@author: Asfahan
"""

import time
import streamlit as st
import pandas as pd

def list_format(li):
    count=0
    data=""
    for i in li:
        data+=str(count)+". "+i
        data+="\n"
        count+=1
    return data

def get_values_pd():
    df=pd.read_csv("data/gen_data/memory.csv")
    val=df["values"]
    return val


def streamify(data,t=0.02):
    for word in data.split(" "):
        yield word + " "
        time.sleep(t)
        
def count_chars(df):
    temp_c=df['values'].str.len()
    return sum(temp_c)


def success_message():
    cont=st.empty()
    cont.success("Message added successfully")
    time.sleep(1)
    cont.empty()

def deleion_message():
    cont=st.empty()
    cont.success("Deletions successful")
    time.sleep(1)
    cont.empty()
    

class Prompts():
    def __init__(self):
        pass
    def quotes(self):
        return """You will give a motivational quote
         Remember following things: 
             1) Target audience is jobseekers
             2) Be kind and compassionate
             3) Dont make it too long
             4) Try to make quote appropriate for a variety of audience. As in it should be
                suitable for audience of diverse backgrounds and cultures"""
                
    def professional_summary(self):
        return """Analyze the given resume provided in pdf file. Then based upon that give a short professional summary for the user
         Remember following things: 
             1) Focus on strengths
             2) Use professional and formal language
             3) Maximum of 500 charaters
             4) No need to include references for examples, things like this 【4:0†source】"""
    def resume_helper(self,mem=False):
        q_1= """ You are expert in resume analysis. Analyze the resume provide in pdf file. After the analysis, the user will provide 
        query to you. Your Job is to answer it.  Remember the following things:
        1) Your main purpose is to answer users query. Only use information from resume if you feel it is needed to answer users query. Else dont use it.
        2) If user asks for where to add the new resume, give an answer "Please go to navigation bar and choose settings".
            This thing is fixed and needs to be followed every time
        3) If you feel you need additional information, you should ask user for it.
        4) No need to include references for examples, things like this 【4:0†source】
        5) In some cases an additional context denoted by <memory> tag will be give. Only use this additional context if you feel it is needed to answer users query. Else dont use it
        If it is given read it before answer the query. If not, no need to worry about it
    """
        q_2=""
        if mem:
            mem_li=get_values_pd()
            if len(mem_li)!=0:
                data=list_format(mem_li)
                q_2=f"""<memory>
                {data}
                </memory>"""
        return q_1+q_2
    
    def summarize_chats(self,li,arr):
      
        data=""
      
        for message in li:
            if message["role"]=="user":
                in_tag="<user>"
                out_tag="</user>"
            else:
                in_tag="<agent>"
                out_tag="</agent>"
        
            data+=in_tag+message["content"]+out_tag
            data+="\n"
        
        s_data=list_format(arr)
        return f"""You are an expert in summarizing stuff. You will given a conversation enclosed in <convo> tag,
        between a user (enclosed in <user> tag) and  an AI agent (enclosed in <agent> tag)
        and extra content enclosed by tag <s_m>.
        You will do the following thing:
            1) Extract all the core ideas (main points) from the messages in <convo>. Focus on last messages in <convo> more
            2) Compare each idea to the list of messages in <s_m>.
    
            3) Identify and return which ideas from the <convo> message are *not* present in any of the other messages in <s_m>.
            4) Once you have these unique ideas, construct a less than 1000 character brief final message which is written from perspective of a user as in "User want to ...".
    
            
            
       
        <convo>
            {data}
        <\convo>
    
           <s_m>
               {s_data}
           </s_m>                                                       
    
                 
      
        """
    
    def AskInterviewQuestion(self,interviewQA):

        return f"""
        Given the list {interviewQA}, which each element gives a question and an anwer
        Present one question at a time. 
        After the user submits their answer, compare it to the reference answer provided in the list. 
        Offer feedback based on the comparison, then proceed to the next question.
        """