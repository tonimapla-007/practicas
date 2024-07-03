# -*- coding: utf-8 -*-
"""
Created on Tue Aug 22 17:59:29 2023

@author: user
"""

#suma de dos numeros con control de errores
print("Introduzca 'q' para salir\n")

while True:        #bucle infinito
    try:
        num1 = input("Introduzca el primer numero ( o 'q' para salir.): ")
        if num1 == 'q':    #comprobamos si acaba la entrada de datos
            break
        if not num1.isdigit():
            print("Introducir solo numeros.")
        num1 = int(num1)
       
        num2 = input("Introduzca el segundo numero (o 'q' para salir.): ")
        if num2 == 'q':
            break
        if not num2.isdigit():
            print("Introducir solo numeros.")
        num2 = int(num2)
      
    except ValueError:
        print("Solo se deben de introducir numeros.")
        
    else:     
        print(f"La suma es {num1 + num2}.")
           
            
            
            
            
            
            
            
            
            
            
            
            
            
            
            
            
            
            
            
            
            
            
            
            
            
            
            
            
            
            
            
            
            
            
            
            
            
            
            
            
            
            
            
            
            
            
            
            
            
            
            
            
            
            
            
            
            
            
            
            
            
            
            
            
            
            
            
            
            
            
            
            
            
            
            
            
            
            
            
            
            
            
            
            
            
            
            
            
            
            
            
            
            
            
            
            
            
            
            
            
            
            
            
            
            
            
            
            
            
            
            
            
            
            
            
            
            
            
            
            
            
            
            
            
            
            
            
            
            
            
            
            
            
            
            
            
            
            
            
            
            
            
            
            
            
            
            
            
            
            
            
            
            
            
            
            
            
            
            
            
            
            
            
            
            
            
            
            
            
            
            
            
            
            
            
            
            
            
            
            
            
            
            
            
            
            
            
            
            
            
            
            
            
            
            
            
            
            
            
            
            
            
            
            
            
            
            
            
            
            
            
            
            
            
            
    
    