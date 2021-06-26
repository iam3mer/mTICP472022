def cambiaNombre(nombre:str)->str:
    print(f'Este es el nombre que ingresa por parametro: {nombre}')
    nombre = 'Vanessa'
    return nombre

nombre = 'Angie'
#print(cambiaNombre(nombre))
#print(nombre)

nombre = cambiaNombre(nombre)
print(nombre)

nombre = 'Juan'
nombre = cambiaNombre(nombre)
print(nombre)