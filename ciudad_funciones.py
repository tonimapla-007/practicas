def ciudad_pais(ciudad, pais, habitantes=''):
    if habitantes:
        nombre = f"{ciudad}, {pais} - habitantes {habitantes}" 
        return nombre.title()
    else:
        nombre = f"{ciudad}, {pais}."
        return nombre.title()

