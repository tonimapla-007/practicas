# -*- coding: utf-8 -*-
"""
Created on Sun Jul  2 20:26:59 2023

@author: user
"""

frutas_favoritas = ['platano', 'pera', 'uvas', 'piña', 'melon']

fruta = input("Introduce una fruta: ")

if fruta == frutas_favoritas[0]:
    print("Pues si que le gustan los platanos.")
elif fruta == frutas_favoritas[1]:
    print("Pues si que le gustan las peras.")
elif fruta == frutas_favoritas[2]:
    print("Pues si que le gustan las uvas.")
elif fruta == frutas_favoritas[3]:
    print("Pues si que le gustan las piñas.")
elif fruta == frutas_favoritas[4]:
    print("Pues si que le gusta el melon.")
else:
    print(f"Parece que no le gusta el/las/los", fruta)