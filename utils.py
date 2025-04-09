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