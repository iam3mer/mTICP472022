num = 10
def fun(num):
    return num * 2

print(num)
print(fun(num))
print(num)

lista = [1,2,3,4,5,6,7,8,9]
def fun2(lista):
    return 2 * lista

print(lista)
print(fun2(lista))
print(lista)

diccionario = {1: 'a'}

def fun3(diccionario):
    return diccionario.update({2: 'b'})

print(diccionario)
print(fun3(diccionario))
print(diccionario)