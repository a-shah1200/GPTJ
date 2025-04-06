# -*- coding: utf-8 -*-


class User():
    def __init__(self,api):
        self.api=api
    def check(self,database=[1]):
        #load the database here
        if self.api not in database:
            return False
        else:
            return True
    def add(self,database=[1]):
        #add the stuff here
        pass