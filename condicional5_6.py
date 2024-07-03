# -*- coding: utf-8 -*-
"""
Created on Sun Jul  2 20:15:42 2023

@author: user
"""

edad = int(input("Que edad tienes: "))

if edad < 2 :
    print("Eres un bebe.")
elif edad >= 2 and edad < 4:
    print("Eres un infante.")
elif edad > 4 and edad < 13 :
    print("Eres un niño.")
elif edad >= 13 and edad < 21:
    print("Eres un adolescente.")
elif edad >= 21 and edad <65:
    print("Eres un adulto.")
elif edad >= 65:
    print("Eres un anciano.")