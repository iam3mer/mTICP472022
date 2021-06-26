# Que pasa?
numeros = [345,756,34,0,467,456,-94,63,64,686,543]

impares = list(map(lambda num: num%2 != 0, numeros))
#print(impares)

#print(all(impares))
#print(any(impares))

def esVerdadero(secuencia):
    numeros = []
    for num in secuencia:
        if num:
            numeros.append(True)
        else:
            numeros.append(False)
    return numeros

#print(esVerdadero(numeros))

#print(all(esVerdadero(numeros)))
#print(any(esVerdadero(numeros)))

# Caso especial
#print(all([]))
#print(any([]))


info = [int(input()), input().split(' ')]
print(
    'True'
    if all(
        list(map(
            lambda x: x>0,
            list(map(int, info[1]))))
    )
    and any(
        list(map(
            lambda x: x[0] == x[1] or x[0] == '5',
            list(zip(
                info[1],
                list(map(lambda x: x[-1:(len(x)+1)*-1:-1], info[1]))
            ))))
    )
    else 'False'
)