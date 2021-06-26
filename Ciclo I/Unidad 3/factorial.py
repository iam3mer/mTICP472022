def factorial(num:int=0): # n! = (n-(n-1)) * (n-(n-2))) * (n-(n-3)) * ... * (n)
    salida = 1            # n! = n * (n-1) * (n-2) * ... * (n-(n-1))
    num_act = 2           # 6! =  6 * 5 * 4 * 3 * ... 1
    while num_act <= num:
        salida = salida * num_act
        num_act = num_act + 1
    return salida

#print(factorial(1))

# Factorial propuesto por la clase P47
def factorial(n: int):
    num = 1
    for i in range(1, n + 1): # [1,2,3,4,5]
        num *= i # num = num * i
    return num

print(factorial(1))