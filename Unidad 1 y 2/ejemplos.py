# Variables: inician con letra o guion bajo
# errores
#var 1 = 264
#@var = 458
#1var = 548
#var-1 = 548

var1 = var2 = var3 = 587
'''
print(var1)
print(var2)
print(var3)
'''
var1, var2, var3 = 25, 85, 24
'''
print(var1)
print(var2)
print(var3)
'''

result = 2*(5-2)
result = (2+3)**(5-3)

var = 20
result = var * 10 / 100
result = (var * 10) / 100

'''
# Calcular el area de un cuadrado
L = float(input("Ingrese el valor del lado: "))
area = L * L
print("El area del cuadrado es: ", area)
perimetro = L * 4
print("El perimetro del cuadrado es: ", perimetro)
'''
'''
while True:
    print("-----------MENU-----------")
    print("\t1. Calcular area.")
    print("\t2. Calcular perimetro.")
    print("\t3. Salir")
    print("--------------------------\n")

    opcion = input("Ingrese una opción: ")

    if opcion == '1':
        L = float(input("Ingrese el valor del lado: "))
        area = L * L
        print("El area del cuadrado es: \n", area)
    elif opcion == '2':
        L = float(input("Ingrese el valor del lado: "))
        perimetro = L * 4
        print(f"El perimetro del cuadrado es: {perimetro} \n")
    elif opcion == '3':
        print("Hasta luego! A finalizado la ejecución del programa.")
        break
    else:
        print("Ingreso una opción no valida.")
'''

# Mostrar los primeros 100 numeros primos

'''
contador=0
i=1
primo=0
while contador<=100:
    while i<=contador:  
        if contador%i==0:
            primo+=1
        i+=1
    if primo==2:
        print(contador)
    contador+=1
    primo=0
    i=1
'''

num = 0
aux = 0
while True:
    count = 1
    x = 0
    while count <= num:
        if num % count == 0:
            x = x + 1
        count = count + 1

    if x == 2:
        print(num)
        aux = aux + 1
        
    num = num + 1

    if aux == 10:
        break
