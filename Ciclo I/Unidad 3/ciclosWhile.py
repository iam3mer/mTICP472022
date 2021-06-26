# While
# Mientras X, haga Y

seg = 10
veces = 6
def whileSimple():
    while veces > 0:
        aux = 0
        while aux < 10:
            print(aux)
            aux = aux + 1
        #print(aux)
        print('MisiónTIC 2022')
        veces = veces - 1

def whileInfinito():
    aux = 0
    while True:
        print(aux)
        aux = aux + 1
        if aux == 5:
            break # Termina la ejecución del ciclo

#whileInfinito()

def whileContinuo():
    aux = 0
    while aux < 30:
        aux = aux + 1
        if aux % 2 == 0:
            continue # Salta las instrucciones en adelante
        print(aux)

#whileContinuo()

def whileElse():
    aux = 3
    while aux > 0:
        print(aux)
        aux = aux - 1
    else:
        print('Termino la ejecución de while.') # Siempre se ejecuta.

#whileElse()