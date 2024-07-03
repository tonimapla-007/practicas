# -*- coding: utf-8 -*-
"""
Created on Sat Aug 19 18:35:45 2023

@author: user
"""
filename = 'invitado.txt'
nombre = input("Introduzca su nombre: ")

with open(filename, 'w') as file_object:
    file_object.write(nombre)