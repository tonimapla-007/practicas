# -*- coding: utf-8 -*-
"""
Created on Wed Jul  5 15:40:19 2023

@author: user
"""

current_user = ['Luis', 'Juan', 'Pedro', 'Carlos', 'Manuel']
new_users = ['Jose', 'Pablo', 'Luis', 'Juan', 'Antonio']




for i in range(len(current_user)):
    current_user[i] = current_user[i].lower()
    
for x in range(len(new_users)):
    new_users[x] = new_users[x].lower()

for i in new_users:
    
        if i in current_user:
            print(f"El nombre de usuario {i}, no esta disponible.")
        else:
            print(f"Nombre de usuario {i} esta disponible.")