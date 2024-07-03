# -*- coding: utf-8 -*-
"""
Created on Sun Aug 27 20:31:08 2023

@author: user
"""

import json

filename = 'favorito.txt'

try:
    numero = input("Introduzca su numero favorito: ")
    with open(filename, 'w')as f:
        json.dump(numero, f)
        
except SintaxError:
    pass
        
    print(numero)