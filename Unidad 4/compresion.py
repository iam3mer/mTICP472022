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
print(numerosPares)

