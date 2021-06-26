nombres = ['Andres', 'Derly', 'Edison', 'Edwin', 'Karla']

print('Elementos con While')

nElementos = len(nombres) # 5
contador = 0
while contador < nElementos: # 0,1,2,3,4
    print(nombres[contador])
    contador = contador + 1

print('\nElementos con For')
range(nElementos) # [0,1,2,3,4]

for contador in range(nElementos):
    print(nombres[contador])

print('\nElementos directamente iterados')
for nombre in nombres:
    print(nombre)