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
    #self.assistant= Assistant(name=name, model="gpt-4o-mini")
    self.thread=None
    self.prompt = prompt
  def get_assitant(self):
    ai = Assistant(
    name="self.name",
    model="gpt-4o-mini",
    instructions=self.prompt,tools=[FileSearch])
    return ai

  def search_files(self,query,files,New=False):
    if self.thread is None or New==True:
      try:
        self.thread.delete()
      except:
        pass
      self.thread = Thread()
    else:
      self.thread = Thread(id=self.thread.id)
    #print(f"Files being searched: {[file.filename for file in files]}")
    self.thread.add(query,file_search_files=files)
    assistant = self.get_assitant()
    runs = self.thread.run(assistant=assistant)
    messages = self.thread.get_messages()
    self.meta = {"run": runs, "thread": self.thread} # Used for debugging only
    return messages

  def reset(self):
    try:
      self.thread.delete()
    except:
      pass
  




    