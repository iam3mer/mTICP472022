# 'E': 5.0 - 4.9
# 'S': 4.8 - 4
# 'A': 3.9 - 3
# 'I': 2.9 - 2
# 'D': 1.9 - 0

# Decisiones simples / secuenciales
def notas1(calificacion:float)->str:

    if 2 > calificacion >= 0:
        print('D')
    if calificacion >= 2 and calificacion < 3:
        print('I')
    if calificacion >= 3 and calificacion < 4:
        print('A')
    if calificacion >= 4 and calificacion < 4.9:
        print('S')
    if calificacion >= 4.9 and calificacion <= 5:
        print('E')


# Decisiones en Cascada
def notas2(calificacion:float)->str:

    if 2 > calificacion >= 0:
        print('D')
    else:
        if calificacion >= 2 and calificacion < 3:
            print('I')
        else:
            if calificacion >= 3 and calificacion < 4:
                print('A')
            else:
                if calificacion >= 4 and calificacion < 4.9:
                    print('S')
                else:
                    if calificacion >= 4.9 and calificacion <= 5:
                        print('E')

# Cascada en Python
def notas3(calificacion:float)->str:

    if 2 > calificacion >= 0:
        print('D')
    elif calificacion >= 2 and calificacion < 3:
        print('I')
    elif calificacion >= 3 and calificacion < 4:
        print('A')
    elif calificacion >= 4 and calificacion < 4.9:
        print('S')
    elif calificacion >= 4.9 and calificacion <= 5:
        print('E')

#notas2(3.5)

# Decisiones Anidadas
def numeros(num: int)->str:

    if num > 0:
        if 9 < num < 100:
            print(f"{num} es de dos digitos")
    else:
        if -99 > num > -1000:
            print(f"{num} es de tres digitos")

#numeros(-254)