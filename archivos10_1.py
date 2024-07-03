# -*- coding: utf-8 -*-
"""
Created on Wed Aug 16 16:19:41 2023

@author: user
"""

filename = 'aprender_python.txt'

with open(filename) as file_object:
    lines = file_object.readlines()
    print(lines)
lineas = lines    
pi_string = ''
for line in lines:
    pi_string += line.strip()
    
print(pi_string)
print(lineas)