# -*- coding: utf-8 -*-
"""
Created on Tue Apr  8 01:42:13 2025

@author: Asfahan
"""

import instructor
from pydantic import BaseModel
from openai import OpenAI
from typing import List


import marvin
from marvin.beta.assistants import (
    Assistant,
    CodeInterpreter,
    FileSearch,
    Thread,
    PrintHandler,
)

class Response(BaseModel):
  main_ideas_convo: List[str]
  unique_ideas:List[str]
  final_message:str

  
    

class StructuredAgent():
  def __init__(self,_API_KEY):
    open_ai = OpenAI(api_key=_API_KEY)
    self.client=instructor.from_openai(open_ai, mode=instructor.Mode.TOOLS_STRICT)
  
  def get_response(self,developer_instruction, user_instruction):
    return self.client.chat.completions.create(
        model="gpt-4o-mini",
        response_model=Response,
        messages=[
            {
                "role": "developer",
                "content": f"{developer_instruction}",
            },
            {
                "role": "user",
                "content": f"{user_instruction}",
            },
        ],
    )
        


class Agent():
  def __init__(self,_API_KEY,name,prompt):
    self.client=OpenAI(api_key=_API_KEY)
    marvin.settings.openai.api_key = _API_KEY
    self.name=name
    self.t_id=None
    #self.assistant= Assistant(name=name, model="gpt-4o-mini")
    self.thread=None
    self.prompt = prompt
 
  def get_tid(self):
      return self.t_id

  def get_assitant(self):
    ai = Assistant(
    name=self.name,
    model="gpt-4o-mini",
    instructions=self.prompt)
    return ai

  def search(self,query,New=False):
    if self.thread is None or New==True:
      try:
        self.thread.delete()
      except:
        pass
      self.thread = Thread()
    else:
      self.thread = Thread(id=self.thread.id)
    self.thread.add(query)
    assistant = self.get_assitant()
    runs = self.thread.run(assistant=assistant)
    messages = self.thread.get_messages()
    self.t_id=self.thread.id
    self.meta = {"run": runs, "thread": self.thread} # Used for debugging only
    return messages

  def reset(self):
    try:
      self.thread.delete()
    except:
      pass

    
    
class FileSearchAgent(Agent):
    def get_assitant(self):
      ai = Assistant(
      name=self.name,
      model="gpt-4o-mini",
      instructions=self.prompt,tools=[FileSearch])
      return ai

    def search(self,query,files,New=False,check=None):
      if check==None:
          if self.thread is None or New==True:
            try:
              self.thread.delete()
            except:
              pass
            self.thread = Thread()
          else:
              self.thread = Thread(id=self.thread.id)
      else:
         self.thread=Thread(id=check)
         #print("We in check",check)
      self.thread.add(query,file_search_files=files)
      assistant = self.get_assitant()
      runs = self.thread.run(assistant=assistant)
      messages = self.thread.get_messages()
      self.t_id=self.thread.id
      self.meta = {"run": runs, "thread": self.thread} # Used for debugging only
      return messages
    


    