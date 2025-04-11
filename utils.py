# -*- coding: utf-8 -*-
"""
Created on Wed Apr  9 13:40:54 2025

@author: Asfahan
"""

import time

def streamify(data,t=0.02):
    for word in data.split(" "):
        yield word + " "
        time.sleep(t)


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
    def resume_helper(self,mem=False,mem_file=None):
        q_1= """ You are expert in resume analysis. Analyze the resume provide in pdf file. After the analysis, the user will provide 
        query to you. Your Job is to answer it.  Remember the following things:
        1) Your main purpose is to answer users query. Only use information from resume if you feel it is needed to answer users query. Else dont use it.
        2) If user asks for where to add the new resume, give an answer "Please go to navigation bar and choose settings".
            This thing is fixed and needs to be followed every time
        3) If you feel you need additional information, you should ask user for it.
        4) ) No need to include references for examples, things like this 【4:0†source】
        5) In some cases an additonal context denoted by <memory> tag will be give.
        If it is given read it before answer the query. If not, no need to worry about it
    """
        if mem==False:
            q_2=""""""
        else:
            with open(mem_file,'r') as f:
                data=f.read()
            q_2=f"""<memory>
            {data}
            </memory>"""
        return q_1+q_2
    