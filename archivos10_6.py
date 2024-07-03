# -*- coding: utf-8 -*-
"""
Created on Mon Aug 21 16:43:45 2023

@author: user
"""

#suma de dos numeros con control de errores
num1 = int(input("Introduzca el prier numero: "))
num2 = int(input("Introduzca el segundo numero: "))

try:
    resultado = num1 + num2
        
except ValueError:
    print("Solo se pueden introducir numeros")

else:
    print(f"El resultado de la suma es {resultado}")
    
