# Paradigma Funcional
# higher-order functions

def saludo(nombre:str):
    print(f'Hola {nombre}. Tripulante del Grupo 47')

def despedirse(nombre:str):
    print(f'Hasta luego {nombre}!')

'''
saludo('Selene')
saludo('Selene')
saludo('Selene')
print()
'''

def nVeces(unaFuncion, veces):
    for _ in range(veces):
        unaFuncion('Selene')

#nVeces(saludo, 5)
#nVeces(despedirse, 3)

def par(num):
    esPar = num%2 == 0
    if esPar:
        return True
    return False

# Funciones anonimas
# lambda

def fahrenheit(celcius):
    fah = (celcius * 9/5) + 32
    return fah

def fahrenheit(celcius):
    return (celcius * 9/5) + 32

def fahrenheit(celcius): return (celcius * 9/5) + 32

fahrenheit = lambda celcius: (celcius * 9/5) + 32

#print(fahrenheit(30))

def addX(num, x):
    return num + x

addX = lambda num, x: num + x
#print(addX(5,7))

# Operador MAP: map(funcion, secuencia)
numeros = [345,756,34,5235,467,456,94,63,64,686,543]
#print(numeros)

def addX(secuencia, x):
    auxNumeros = []
    for num in secuencia:
        auxNumeros.append(num + x)
    return auxNumeros

#print(addX(numeros, 7))

addXMAP = list(map(lambda num: num + 7, numeros))
#print(addXMAP)

# Que pasa si usamos filter?
addXMAP = list(filter(lambda num: num + 7, numeros))
#print(addXMAP)

# Operador FILTER: filter(funcion, secuencia)
def funPares(secuencia):
    pares = []
    for num in secuencia:
        if par(num):
            pares.append(num)
    return pares

#print(funPares(numeros))

pares = list(filter(lambda num: num%2 == 0, numeros))
#print(pares)

# Que pasa si uso map?
pares = list(map(lambda num: num%2 == 0, numeros))
#print(pares)

# Operador REDUCE: reduce(funcion, secuencia)

def promedio(secuencia):
    cantidadElementos = len(secuencia)
    acumulador = 0
    for num in secuencia:
        #acumulador = acumulador + num
        acumulador += num
    promedio = acumulador / cantidadElementos
    return round(promedio,2)

#print(promedio(numeros))

from functools import reduce
promedio = reduce(lambda x, y: x + y, numeros) / len(numeros)
#promedio = list(map(lambda x, y: x + y, numeros)) / len(numeros) # No se puede
#print(round(promedio,2))

# ZIP: zip(secuencia1, secuencia2)
s1 = [1,2,6,8,4]
s2 = ['a', 'b', 'c', 'd', 'e']
#print(list(zip(s1,s2)))