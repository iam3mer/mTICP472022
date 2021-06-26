# Conjunto
# set() # Mutable
# frozenset() # Inmutable

conjunto = set()

conjunto = {6,534645,4564,5645,57,745,3463,747,57,4356,356,568}

#print(conjunto)
#print(conjunto[1]) # No se puede hacer

a = {1,2,3,4,5,6,7}
b = {8,9,10,1,5,3,11,12,'g', 'h'}

#print(a.union(b))
#print(a.intersection(b))
#print(a.difference(b))
#print(b.difference(a))

conjunto.add('Cadena')
#print(conjunto)

conjunto.add((234,2345,5436,567))
print(conjunto)

conjunto.pop()
##print(conjunto)
conjunto.pop()
#print(conjunto)

lista = [3245,3453453,4534,5345]
#print(lista)
lista = set(lista)
#print(lista)
lista = list(lista)
#print(lista)

print(57 in conjunto)