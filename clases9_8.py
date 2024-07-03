# -*- coding: utf-8 -*-
"""
Created on Wed Aug  2 20:47:17 2023

@author: user
"""
class Usuarios:
    """creamos datos de usuario"""
    def __init__(self, nombre, apellido, edad):
        """inicializamos atributos"""
        self.nombre_usuario = nombre
        self.apellido_usuario = apellido
        self.edad_usuario = edad
       
                
    def datos_usuario(self):
        """imprimimos los datos de usuario"""
        print(f"Nombre de usuario: {self.nombre_usuario}.\n")
        print(f"Apellido usuario: {self.apellido_usuario}.\n")
        print(f"Edad usuario: {self.edad_usuario}.\n")
        
    def saludo_usuario(self):
        """imprimimos un saludo para el usuario"""
        print(f"Hola {self.nombre_usuario} como estas?\n")
        
class Admin(Usuarios):
    
    def coje_privilegios(self, privilegios):
        self.privilegios = privilegios
        for i in privilegios:
            print(i)
        
        #print(f"los privilegios de {self.nombre_usuario} son {self.privilegios}.")

privilegios = ['borrar datos', 'leer datos', 'rectificar datos']

user = Admin('juan', 'hidalgo', 23)
user.datos_usuario()
user.coje_privilegios(privilegios)
user1 = Admin('pitu', 'garcia', 27)
user1.datos_usuario()
user1.coje_privilegios(privilegios)
