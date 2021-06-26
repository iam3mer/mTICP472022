# PANDAS
# pip install pandas

import pandas as pd

# Series (vector columna)
# Series(datos, indices, tipo)
s = pd.Series(['Artes', 'Ingles', 'Matematicas'], dtype='string')
#print(s)

s = pd.Series({'Artes': 5, 'Ingles': 4.5, 'Matematicas': 5})
#print(s)

# Propiedades
# print(s.size)
# print(s.index)
# print(s.dtype)

# Acceso a valores por posición
# print(s[0])
# print(s['Artes'])

# Acceso a valores por índice
# print(s[0:1])
# print(s[['Ingles', 'Matematicas']])
# ---------

# print(s.mean())
# print(s.min())
# print(s.max())

from math import ceil
# print(s.apply(ceil))
# print(s.sum())
# print(s[s > 4.6])

# Eliminar datos desconocidos de una serie
import numpy as np
s = pd.Series(['a','b',None,'c',np.NaN, 'd'])
# print(s)
# print(s.dropna())

# DataFrame (tabla, matriz)
# DataFrame(datos, indiceF, indiceC, tipos)

datos = {
    'nombres': ['Derly', 'Francisco', 'Nelsi'],
    'edades': [19,23,20],
    'asignaturas': ['artes', 'ingles', 'matematicas'],
    'notas': [4.8,5,4]
}

dataDF = pd.DataFrame(datos)
# print(dataDF)

# print(dataDF['nombres'][2])
# print(dataDF.loc[2, 'nombres'])
# print(dataDF.iloc[0,3])

datos = [
    {'nombre': 'Derly', 'edad': 19},
    {'nombre': 'Francisco', 'edad': 23},
    {'nombre': 'Nelsi'}
]

dataDF = pd.DataFrame(datos)
# print(dataDF)

# Propiedades
# print(dataDF.info())
# print(dataDF.shape)
# print(dataDF.columns)
# print(dataDF.index)
# print(dataDF.head(2))
# print(dataDF.tail(2))

# Añadir un campo (columna) a un DataFrame
# df[nombrecol] = serie
dataDF['ciudades'] = ['Medellin', 'Tulua', 'Santa Marta']
print(dataDF)

# Eliminar columnas
del dataDF['ciudades']
serie = dataDF.pop('edad')

# Panel (cubos)

