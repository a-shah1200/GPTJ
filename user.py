# -*- coding: utf-8 -*-

import json
class User():
    def __init__(self,api):
        self.api=api
        with open("data/database.json", 'r') as f:
            data = json.load(f)
        self.data=data
    def check(self): 
        if self.api not in self.data["api_key"]:
            return False
        else:
            return True
    def add(self,first,last):
        count=0
        if len(self.data["id"])==0:
            count=0
        else:
            count=int(self.data["id"][-1])+1
        self.data["id"].append(int(count))
        self.data["api_key"][self.api]=int(count)
        self.data["first_name"][int(count)]=first
        self.data["last_name"][int(count)]=last
        self.data["generate_r"][int(count)]=0
        with open("data/database.json", 'w') as f:
            json.dump(self.data,f)
    
            
    def get_data(self):
        if self.check():
            try:
                i_d=str(self.data["api_key"][self.api])
                return self.data["first_name"][i_d],self.data["last_name"][i_d]
            except:
                i_d=int(self.data["api_key"][self.api])
                return self.data["first_name"][i_d],self.data["last_name"][i_d]
            
                
        else:
            raise Exception("Something Has Gone Wrong, User Should be registered")
    
    def is_gen_r(self,check=1,val=0):
        i_d=self.data["api_key"][self.api]
        if check:
            try:
                return self.data["generate_r"][str(i_d)]
            except:
                return self.data["generate_r"][int(i_d)]
        else:
            self.data["generate_r"][str(i_d)]=val
            with open("data/database.json", 'w') as f:
                json.dump(self.data,f)
            
            
            
        
            
        
        
        