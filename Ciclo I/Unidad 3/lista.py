# Listas

unaLista = []
unaLista = list()
unaLista = [423,453453,65346,45,34563,'Una Cadena', [354,345], 45] #Mutable

#print(unaLista[3])

unaLista.append('Otra Cadena')

'''
palabra = 'Esta es una cadena'
print(palabra[0])

for caracter in palabra:
    print(caracter)
'''

unaLista.extend([2,4,6])
unaLista.extend('b')
#print(unaLista)

#unaLista.extend(52)
#print(unaLista)

unaLista.extend('Nueva')
unaLista.append('Nueva')
#print(unaLista)

#print(unaLista)
#print(unaLista.count('Una Cadena'))

unaLista.insert(2,{'nombre':'Angie'})
#print(unaLista)

elemento = unaLista.pop(1)
#print(unaLista)
#print(elemento)

unaLista.remove(45)
#print(unaLista)

#print(unaLista,'\n')
unaLista.reverse()
#print(unaLista)

num = [234,2343,645,7656798,6789,5563,453,4756,7845,64]
num.sort()
#print(num)

nombres = ['Karla', 'Andres', 'Edison', 'ana', 'Derly', 'Edwin']
nombres.sort()
#print(nombres)

# Consultar el 345 en la lista anidada
#print(unaLista,'\n')
#print(unaLista[12][1])

matriz = [[1,2,3,4,5,], [6,7,8,9,10], [11,12,13,14,15]]
#obtener el 9
#print(matriz[1][3])

# Primer elemento de cada lista (primer columna de la matriz)
for numeros in matriz:
    print(numeros[0])
print('-----')
for i in range(len(matriz)):
    print(matriz[i][0])
print('-----')
# Todos los elementos de la matriz uno a uno
for numeros in matriz:
    for num in numeros:
        print(num)

