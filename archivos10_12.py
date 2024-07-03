# -*- coding: utf-8 -*-
"""
Created on Sun Aug 27 20:49:07 2023

@author: user
"""

import json

def get_stored_user_number():
    filename = 'favorito.json'
    try:
        with open(filename) as f:
            numero = json.load(f)
    except FileNotFoundError:
        return None
    else:
        return numero
    
def new_user_number():
    filename = 'favorito.json'
    try:
        numero = input("Introduzca su numero favorito: ")
        with open(filename, 'w') as f:
            json.dump(numero, f)
    except SyntaxError:
        pass
    else:
        return numero
    
def greet_user():
    numero = get_stored_user_number()
    if numero:
        print(f"Su numero es: {numero}")
    else:
        new_user_number()

greet_user()

    
        
        




