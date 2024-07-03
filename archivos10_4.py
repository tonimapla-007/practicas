# -*- coding: utf-8 -*-
"""
Created on Sat Aug 19 18:45:38 2023

@author: user
"""

filename = 'libro_invitados.txt'

fin = 'q'
nombre = 0

while nombre != '':
    print("Para acabar presione enter.\n")
    nombre = input("Introduzca su nombre: ")
    with open(filename,'a')as file_object:
        file_object.write(f"{nombre}\n")
        
