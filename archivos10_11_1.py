# -*- coding: utf-8 -*-
"""
Created on Sun Aug 27 20:41:01 2023

@author: user
"""

import json

filename = 'favorito.txt'

try:
    with open(filename) as f:
        numero = json.load(f)
        
except FileNotFoundError:
    print("No se encuentra el archivo")
    
else:
    print(f"el numero es: {numero}")