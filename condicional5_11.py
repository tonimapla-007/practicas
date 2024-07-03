# -*- coding: utf-8 -*-
"""
Created on Fri Jul  7 15:25:55 2023

@author: user
"""

numeros = ['1', '2', '3', '4', '5', '6', '7', '8' ,'9']

for i in range(len(numeros)):
    num = numeros[i]
    if num == '1':
        num1 = '1st'
        print(num1)
    elif num == '2':
        num1 = '2nd'
        print(num1)
    elif num == '3':
        num1 = '3rd'
        print(num1)
    else:
        print(num+'th')