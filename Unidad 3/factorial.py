def factorial(num:int=0): # n! = (n-(n-1)) * (n-(n-2))) * (n-(n-3)) * ... * (n)
    salida = 1            # n! = n * (n-1) * (n-2) * ... * (n-(n-1))
    num_act = 2           # 6! =  6 * 5 * 4 * 3 * ... 1
    while num_act <= num:
        salida = salida * num_act
        num_act = num_act + 1
    return salida

print(factorial(1))