# -*- coding: utf-8 -*-
"""
Created on Mon Jul  3 19:50:14 2023

@author: user
"""

user = []

nombre = input("Nombre de usuario: ")
for i in user:
    if nombre == 'admin':
        print("Hola admin, quieres ver un informe de estado?")
        break
    elif i in user:
        print(f"hola {nombre}, gracias por volver.")
        break
    
if len(user) == 0:
    print("Necesitamos encontrar usuarios.")