# -*- coding: utf-8 -*-
"""
Created on Sat Aug 28 18:52:07 2021

@author: admin
"""

import requests 
from data_input import data_in, data_in2,data_in3

URL = 'http://127.0.0.1:5000/predict'
headers = {"Content-Type": "application/json"}
data = {"input": data_in}

r = requests.get(URL,headers=headers, json=data) 

r.json()
print(r.json())