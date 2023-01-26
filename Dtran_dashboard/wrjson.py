# -*- coding: utf-8 -*-
"""
Created on Tue Oct  4 10:15:16 2022

@author: robert
"""

import json
import os
 
"""
Read and Write Json file

WRITE:
    input: file -> file path+name / content -> dict type
    
READ:
    input: file -> file path+name / sort -> key value ["key1","key2"]
    output: stored -> [[key1 value, key2 value], [key1 value, key2 value],...]
"""
def write_json(file, content):
# Data to be written
    # Serializing json
    if os.path.isfile(file):
        addline_json(file, content)
    else:
        json_object = json.dumps(content)
         
        # Writing to sample.json
        with open(file, "w") as outfile:
            outfile.write(json_object + '\n')
        
def addline_json(file, content):
     
    json_object = json.dumps(content)
    # Writing to sample.json
    with open(file, "a") as outfile:
        outfile.write(json_object + '\n')
     
def read_json(file, sort):        
    # Opening JSON file
    stored = []
    if sort == 'all':
        with open(file, 'r') as openfile:
            for obj in openfile:
                json_object = json.loads(obj)
                stored.append(json_object)
    else:
        with open(file, 'r') as openfile:
            for obj in openfile:
                json_object = json.loads(obj)
             
                stored.append([json_object[x] for x in sort])
    
    return stored

def del_json(file, key, value):#value={key: value}
    stored = []
    with open(file, 'r') as openfile:
        for obj in openfile:
            json_object = json.loads(obj)
            if json_object[key] != value:
                stored.append(json_object)
    #print(stored)
    with open(file, "w") as outfile:
        for i in stored:
            outfile.write(json.dumps(i) + '\n')