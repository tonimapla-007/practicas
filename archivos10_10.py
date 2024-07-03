# -*- coding: utf-8 -*-
"""
Created on Sat Aug 26 17:51:21 2023

@author: user
"""
filename = 'moby_dick.txt'
lista = []
try:
    with open(filename, encoding='utf-8') as file_object:
        archivo = file_object.read()
        numero = archivo.count('the ')
        print(numero)
except SyntaxError:
    print("Error de sintaxis")
    
  