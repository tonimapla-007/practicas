# -*- coding: utf-8 -*-
"""
Created on Sun Aug 20 20:08:44 2023

@author: user
"""

filename = 'alice.txt'

try:
    with open(filename, encoding='utf-8') as f:
        contens = f.read()
except FileNotFoundError:
    print(f"No se encontro el archivo {filename}.")
else:
    #cuenta el numero de palabras en la fila
    words = contens.split()
    num_words = len(words)
    print(f"The file {filename} has about {num_words} words.")
    