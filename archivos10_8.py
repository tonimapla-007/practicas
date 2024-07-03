# -*- coding: utf-8 -*-
"""
Created on Fri Aug 25 20:44:47 2023

@author: user
"""

filename1 = 'gatos.txt'
filename2 = 'perros.txt'
f_string1 = ''
d_string2 = ''
try:
    with open(filename1, encoding='utf-8') as file_object:
        lines1 = file_object.readlines()
        for line1 in lines1:
            print(line1.rstrip())
            
except FileNotFoundError:
    print(f"No se ha encontrado el archivo {filename1}")

print("\n")    
    
try:    
    with open(filename2, encoding='utf-8') as d:
        lines2 = d.readlines()
        for line2 in lines2:
            print(line2.rstrip())
            
except FileNotFoundError:
    print("No se ha encontrado el archivo {filename2}")  

          