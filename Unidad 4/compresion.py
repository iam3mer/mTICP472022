from pprint import pprint as pp
from random import randint, randrange, random, uniform

# Estructuras por extensión

numeros = [1,5,3,4,8,2,5,7]
edades = {'Juan': 30, 'Camila': 28}

# Estructuras por compresión

# numeros pares del 2 al 100
numerosPares = []
for num in range(2,101):
    if num % 2 == 0:
        numerosPares.append(num)
#print(numerosPares)

numerosPares = []
for num in range(2,101,2):
    numerosPares.append(num)
#print(numerosPares)

# listaComprension = [definicionElementoAgregar for varible in otraLista]

listaCompresion = [num*2 for num in [2,3,4,5,6,7,8,9,10]]
#print(listaCompresion)

# numeros pares del 2 al 100, por comprension
numerosPares = [num for num in range(2,101) if num % 2 == 0]
#print(numerosPares)

# numeros entre 0 y 100, divisibles por 3
divisible3 = []
for num in range(101):
    #print(f'{num} % 3 = {num % 3}')
    if num % 3 == 0:
        divisible3.append(num)
#print(divisible3)

divisible3 = [num for num in range(101) if num % 3 == 0]
#print(divisible3)

# numeros pares entre 0 y 100, divisibles por 3
paresDivisibles3 = [num for num in range(101) if num % 3 == 0 and num in range(0,101,2)]
#print(paresDivisibles3) 

# Compresion usando funciones
# Numeros pares
def esPar(num:int)->int:
    if num % 2 == 0:
        return num

numerosPares = [num for num in range(0,101) if esPar(num) != None]
#print(numerosPares)

# Area de un cuadrado
ladoCuadrados = [2,4,6,8,10,12,14,16]
areaCuadrados = [l*l for l in ladoCuadrados]
#print(areaCuadrados)

# Construir una funcion que retorne una lista con las llaves de un diccionario (no usar keys)
diccionario = {1:'a', 2:'b', 3:'c'}
#print(list(diccionario.keys()))

keys = []
def myKeys(diccionario:dict)->list:
    for key in diccionario:
        keys.append(key)
    return keys
#print(myKeys(diccionario))

keys = [key for key in diccionario]
#print(keys)

# Construir una funcion que retorne una lista con los valores de un diccionario (no usar values)
diccionario = {1:'a', 2:'b', 3:'c'}
#print(list(diccionario.values()))

values = []
def myValues(diccionario:dict)->list:
    for key in diccionario:
        values.append(diccionario[key])
    return values
#print(myValues(diccionario))

values = [diccionario[key] for key in diccionario]
#print(values)

# Encontrar elementos repetidos en una lista
a = ['Andres', 'Julian', 'Edison', 'Edwin', 'Felipe']
b = ['Francisco', 'Juan', 'Andres', 'Julian', 'Felipe']

repetidos = []
def repetido(a:list,b:list)->list:
    for x in a:
        if x in b:
            repetidos.append(x)
    return repetidos
#print(repetido(a,b))

repetidos = [x for x in a if x in b]
#print(repetidos)

repetidos = []
def repetido(a:list,b:list)->list:
    for x in a:
        for y in b:
            if x == y:
                repetidos.append(x)
    return repetidos
#print(repetido(a,b))

repetidos = [x for x in a for y in b if x == y]
#print(repetidos)

# Tablas de multiplicar
# tablasDict = {2: [4,6,8,10,12,14,16,18], 3: []}
tablasDict = {}
def tablas(num:int)->dict:
    for n in range(2,num+1):
        auxLista = []
        for z in range(2,10):
            auxLista.append(n*z)
        tablasDict[f'Tabla del {n}'] = auxLista
    return tablasDict

#print(tablas(10))

tablasDict = {f'Tabla del {n}': [n*z for z in range(2,10)] for n in range(2,11)}
#print(tablasDict)
#pp(tablasDict)

'''
# Generar numeros aleatorios
# Genera un numero entero de forma aleatoria entre los limites dados
for num in range(10):
    print(randint(10,100), end=' ')
print()

aleatorioRandint = [randint(10,100) for num in range(10)]
print(aleatorioRandint)

# Genera un numero entero de forma aleatoria entre los limites dados
# Opcionalmente se puede indicar un step
for num in range(10):
    print(randrange(10,100,20), end=' ')
print()

aleatorioRandrange = [randrange(10,100,20) for num in range(10)]
print(aleatorioRandrange)

# Genera decimales entre 0 y 1 (no se incluye)
for num in range(10):
    print(random(), end=' ')
print()

aleatorioRandom = [random() for num in range(10)]
print(aleatorioRandom)

# Genera un numero decimal de forma aleatoria entre un punto inicial y uno final
for num in range(10):
    print(uniform(10,100), end=' ')

aleatorioUniform= [uniform(10,100) for num in range(10)]
print(aleatorioUniform)
'''

# ciudadesDict = {(a,b): 85, (a,c): 71, ...}
listaCiudades = ['a','b','c','d','e','f','g']

# Generar todos los arcos para la lista
arcos = {}
for i in listaCiudades:
    auxLista = []
    for j in listaCiudades:
        if j != i:
            auxLista.append((i,j))
    arcos[i] = auxLista
#pp(arcos)

arcos = {i: [(i, j) for j in listaCiudades if j != i] for i in listaCiudades}
#pp(arcos)

# Obtener una lista con todos los arcos por ciudades
arcos = list(arcos.values())
#print(arcos)

# Obtener los arcos "unicos"
auxArcos = []
i = 0
def seleccionarArcos(i:int,auxArcos:list)->list:
    for fila in arcos:
        aux = fila[i:len(fila)]
        if aux != []:
            auxArcos.append(aux)
        i += 1
    return auxArcos

arcos = seleccionarArcos(i,auxArcos)

# Cuantas distancias se deben generar?
numDistancias = 0
for lista in arcos:
    numDistancias += len(lista)
#print(numDistancias)


# Lista con los arcos 
auxArcos = []
for lista in arcos:
    for par in lista:
        auxArcos.append(par)
#print(len(auxArcos))

auxArcos = [par for lista in arcos for par in lista]
#print(auxArcos)

# Generar las distancias
numDistancias = len(auxArcos)
distancias = []
for km in range(numDistancias):
    distancias.append(randrange(60,800,40))
print(distancias)

# Añadir a los arcos sus distancias
