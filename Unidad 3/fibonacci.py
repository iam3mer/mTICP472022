def fibonacci(fibo:int=100)->None: # Serie de Fibonacci hasta valor menor que 100
    num1, num2 = 0, 1
    while num2 < 100:
        print(num2)
        num1, num2 = num2, num1 + num2

valor = 100
#fibonacci(valor)


def fibonacciModificado(limite:int=100): # los "100" primeros numeros de Fibonacci
    n = 0
    auxLimite = 0
    auxN = n + 1
    while auxLimite < limite:
        auxLimite = auxLimite + 1
        print(n)
        n, auxN = auxN, n + auxN

limite = 50
fibonacciModificado(limite)
