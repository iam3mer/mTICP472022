# Datatypes --------------------------------------
# Enteros (int)
# 34
# 534
# -34
print(type(-2))

# Flotantes (float)
# 5.0
# 4.2
# -0.25
print(type(0.052))

# String (str)
print(type('Hola Mundo'))
print(type("Hola Mundo"))
print(type('''Hola Mundo'''))
print(type("""Hola Mundo"""))

# Booleanos (bool)
# True -> ...-3, -2, -1, 1, 2, 3...
# False -> 0
print(type(True))
print(type(False))

# Variables ------------------------------------
nombreClave = 'nombreClave almacena esta cadena' # Camel Case
nombre_clave = 'nombre_clave almacena esta cadena' # Snake Case
NombreClave = 'NombreClave almecena esta cadena' # Pascal

print(type(nombreClave))
nombreClave = 7
print(type(nombreClave))

var1, var2, var3 = 1, 2, 3

numeroSTR = '10'
print(type(numeroSTR))
numero = int(numeroSTR)
print(type(numero))
numero = float(numeroSTR)
print(type(numero))
print(numero)

print(int(True))
print(int(False))

print(chr(47))
print(ord('/'))

# Colecciones ---------------------------------------------------
# Lista (list)
lista_vacia = []
mi_lista = [456,345,574,463,4532,5356,3456.34,35.54,'Cadena',['eras', 'dfg', 'fdgswd']]
print(mi_lista[0])
print(mi_lista[8])
print(len(mi_lista))
print(mi_lista[len(mi_lista)-1])
print(mi_lista[9][1])
print(mi_lista[7:45])
print(mi_lista[:-1]) # Omite el ultimo elemento de la coleccion
print(mi_lista[::-1]) # Invierte el orden de los elementos de la coleccion

mi_lista[9][2] = 'TIC'
print(mi_lista)

print(dir(mi_lista))

mi_lista.append('Otra cadena')
print(mi_lista)
mi_lista.pop()
print(mi_lista)
un_elemento_de_la_misma = mi_lista.pop(5)
print(mi_lista)
print(un_elemento_de_la_misma)

print(lista_vacia.__sizeof__())
print(mi_lista.__sizeof__())

mi_lista.insert(0, [345,345,345,345,346,45,645,63,453,6,4576,47])
print(mi_lista)
print(mi_lista.__sizeof__())

# Tuplas (tuple)
tupla_vacia = ()
una_tupla = (34,5345,345,345,345)
otra_tupla = 34,5345,345,345,345
print(type(tupla_vacia), type(una_tupla), type(otra_tupla))

print(dir(tupla_vacia))
# otra_tupla[1] = 'Otro' # No se puede hacer
print(otra_tupla[1])
print(otra_tupla[len(otra_tupla)-1])
print(otra_tupla[1:4])

print((34,521,52) < (34,465,86))

# Conjuntos (set)
un_set = {1,345,345,345,345,23654,35764,74567,567,476}
print(type(un_set))
print(un_set)
# print(un_set[0]) # No se puede hacer
print(dir(un_set))
print(len(un_set))

otro_set = {345345,34534,534,345,75463563,451,356,356,15,1,34534}
union1 = un_set.union(otro_set)
union2 = otro_set.union(un_set)
print(union1)
print(union2)
interseccion = un_set.intersection(otro_set)
print(interseccion)
diferencia1 = otro_set.difference(un_set)
diferencia2 = un_set.difference(otro_set)
print(diferencia1)
print(diferencia2)

# Diccionarios (dict)
# {key: value}
diccionario_vacio = {}

otro_diccionario = {
    'nombre': 'Jhonatan',
    'apellido': 'Barrera',
    'Adicionales' : ['Risaralda', 'Pereira', {'profesion': 'Ingeniero de Sistemas y Computación',
                                              'universidad': 'Universidad Tecnológica de Pereira'}]
}

print(otro_diccionario['Adicionales'][2]['profesion'])

print(dir(otro_diccionario))

ultimo_elemento_del_diccionario = otro_diccionario['Adicionales'][2].pop('universidad')
print(ultimo_elemento_del_diccionario)
print(otro_diccionario)
print()
print(list(otro_diccionario.keys()), list(otro_diccionario.values()))

print(list(otro_diccionario.items()))

otro_diccionario['nueva llave'] = 8768
print(otro_diccionario)
otro_diccionario['nueva llave'] = 'Nuevo valor'
print(otro_diccionario)

otro_diccionario.update((('codigo', 'Mat54'), ('nombre', 'Matematicas Discretas')))
otro_diccionario.update(nueva_llave = {'codigo': 'Mat54', 'nombre': 'Matematicas Discretas'})

print(otro_diccionario)

# Condicionales -----------------------------------------------
if otro_diccionario['nueva llave'] == 'Nuevo valor':
    print('Son iguales')
    # instruccion 2
    # instruccion 3
# instruccion 4

if otro_diccionario['nueva llave'] == 8768:
    pass
    # print('Son iguales')
else:
    print('No son iguales')

numero1= [23,234,345,567]
numero2= [2345,56,5476,56]

if numero1[0] == numero2[0]:
    print('Son iguales')
elif numero1[0] < numero2[0]:
    print(f'{numero1[0]} es menor que {numero2[0]}')
else:
    print(f'{numero1[0]} es mayor que {numero2[0]}')

if True:
    print('Esto siempre se va a mostrar (Siempre es verdadero)')

if False:
    pass
else:
    print('Esto siempre se va a mostrar (Nunca sera verdadero)')

# Ciclos (for, while)
for item in numero1:
    print(item, end=' - ')
print()

# for i in range(len(numero1)):
#     print(i, end=' - ')

for i in range(len(numero2)):
    if numero1[i] == numero2[i]:
        print('Son iguales')
    elif numero1[i] < numero2[i]:
        print(f'{numero1[i]} es menor que {numero2[i]}')
    else:
        print(f'{numero1[i]} es mayor que {numero2[i]}')

for key in otro_diccionario:
    print(otro_diccionario[key])

for k, v in otro_diccionario.items():
    print(k, v)

band = True
contador = 0
while band:
    contador = contador + 1
    print(contador, end=' ')
    if contador == 7:
        break
print()

i = 0
while i < len(numero2):
    if numero1[i] == numero2[i]:
        print('Son iguales')
    elif numero1[i] < numero2[i]:
        print(f'{numero1[i]} es menor que {numero2[i]}')
    else:
        print(f'{numero1[i]} es mayor que {numero2[i]}')

    i = i + 1

print('---------------------------------------')
# Funciones
def compara(num1:int, num2:int)->str:
    if num1 == num2:
        return 'Son iguales'
    elif num1< num2:
        return f'{num1} es menor que {num2}'
    else:
        return f'{num1} es mayor que {num2}'

print(compara(345,564))

for i in range(len(numero1)):
    print(compara(numero1[i], numero2[i]))