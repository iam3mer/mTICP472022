# Ejercicio 1

cadena = 'Hola Tripulantes del Grupo 47'

def logitud(cadena:str):
    longitudPalabras = []
    palabras = cadena.split()
    for palabra in palabras:
        longitudPalabras.append(len(palabra))
    return longitudPalabras

#print(logitud(cadena))

def longitudPalabras(cadena):
    return list(map(lambda palabra: len(palabra), cadena.split()))
#print(longitudPalabras)

# Ejercicio 2
numeros = [324,5,7,786] # 32457786

def numero(lista:list)->int:
    numero = ''
    for num in lista:
        numero += str(num)
    return numero
#print(numero(numeros))

from functools import reduce
def numero(numeros):
    return reduce(lambda x, y: str(x) + str(y), numeros)
#print(numero)

# Ejercicio 3
palabras = ['carro', 'almacen', 'caballo', 'alaja', 'amarillo']

def filtroCaracter(lista:list, caracter:str)->list:
    palabras = []
    for palabra in lista:
        if palabra[0] == caracter:
            palabras.append(palabra)
    return palabras
print(filtroCaracter(palabras, 'a'))

def filtroCaracter(lista:list, caracter:str):
    return list(filter(lambda palabra: palabra[0] == caracter, lista))
print(filtroCaracter(palabras, 'a'))

# Ejercicio 4
palabra1 = ['o','t','o','r','r','i','n','o','n','a','r','i','n','g','o','l','o','g','o']
palabra2 = 'paranguaricutirimucuaro'
palabra2 = list(map(lambda x: x, palabra2))

def rara(palabra1, palabra2, separador='-'):
    return list(map(lambda x: x[0] + separador + x[1], zip(palabra1, palabra2)))

print(rara(palabra1, palabra2))

def rara2(palabra1, palabra2, separador):
    return list((c1 + separador + c2 for (c1, c2) in zip(palabra1, palabra2)))

print(rara2(palabra1, palabra2, '-'))