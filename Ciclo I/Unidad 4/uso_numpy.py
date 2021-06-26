# Numpy
# Instalar Numpy: pip install numpy
# np.array(lista o tupla)

import numpy as np

# array 
a1 = np.array([1,2,3])
#print(a1)
#print(a1.shape)

# array de dos dimensiones
a2 = np.array([[1,2,3],[4,5,6]])
#print(a2)
#print(a2.shape)

# array de tres dimensiones
a3 = np.array([[[1,2,3,13],[4,5,6,14]],[[7,8,9,15],[10,11,12,16]]])
#print(a3)
#print(a3.shape)

#print(a3.shape[2])
#print(a3[0][1][2])

#print(np.zeros([4,4]))
#print(np.ones([3,2]))
#print(np.identity(5))
#print(np.full([5,7], 7))
#print(np.arange(10,50,5))
#print(np.random.random([5,4]))

m1 = np.random.random([5,4])
m2 = np.random.random([5,4])

print(m1,'\n\n',m2,'\n')
print(m1 + m2,'\n')
print(m1 - m2,'\n')
print(m1 / m2,'\n')

print(m1 * m2,'\n')

m1 = np.random.random([3,5])
m2 = np.random.random([5,4])
print(m1.dot(m2))