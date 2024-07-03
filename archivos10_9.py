# -*- coding: utf-8 -*-
"""
Created on Sat Aug 26 17:45:57 2023

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
    print("No se encuentra el archivo.")

print("\n")    
    
try:    
    with open(filename2, encoding='utf-8') as d:
        lines2 = d.readlines()
        for line2 in lines2:
            print(line2.rstrip())
            
except FileNotFoundError:
    print("No se ha encontrado el archivo {filename2}")  
