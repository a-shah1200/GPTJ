# -*- coding: utf-8 -*-
"""
Created on Tue Apr  8 01:42:13 2025

@author: Asfahan
"""

from openai import OpenAI
import marvin
from marvin.beta.assistants import (
    Assistant,
    CodeInterpreter,
    FileSearch,
    Thread,
    PrintHandler,
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
         print("We in check",check)
      self.thread.add(query,file_search_files=files)
      assistant = self.get_assitant()
      runs = self.thread.run(assistant=assistant)
      messages = self.thread.get_messages()
      self.t_id=self.thread.id
      self.meta = {"run": runs, "thread": self.thread} # Used for debugging only
      return messages
    


    