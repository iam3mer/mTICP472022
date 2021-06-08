from pprint import pprint as pp
# Guardar y Leer archivos con Pandas
import pandas as pd

datos = {
    'nombres': ['Nelsi', 'Julian', 'Miguel'],
    'apellidos': ['Miramag', 'Villanueva', 'Nieto'],
    'reto 1': [4.8, 4.5, 5],
    'reto 2': [5, '?', 4.8]
}

dataDF = pd.DataFrame(datos)
# print(dataDF)

# DF a CSV
dataDF.to_csv('infoTripulantes.csv')

leerCSVDF = pd.read_csv(
    'infoTripulantes.csv',
    skiprows=1,
    names=['ID', 'Nombre', 'Apellido', 'Nota Reto 1', 'Nota Reto 2'],
    #index_col='ID'
    index_col=['ID','Apellido'],
    na_values=['?']
)

# print(leerCSVDF)

# DF a XLSX
# pip install openpyxl
leerCSVDF.to_excel('infoTripulantes.xlsx', sheet_name='Tripulantes')

dfXLSXDF = pd.read_excel(
    'infoTripulantes.xlsx',
    sheet_name='Tripulantes',
    index_col=0
)

# print(dfXLSXDF)

# Manipulación de archivos con Python

# Modos
# r : Lectura
# w : Escritura. Sobre escribe el archivo
# a : Escritura. Conserva contenido, los nuevos datos se añaden la final del archivo
# r+, w+, a+
# rb, wb, ab, rb+, wb+, ab+

datos = ['Estamos en la unidad 5 del ciclo 1', 'Se manipulan archivos desde Python']

fichero = open('ejemploArchivo.txt', 'a+')
# print(fichero)

for line in datos:
    # fichero.write(line)
    #print(line, file=fichero)
    pass

fichero.writelines('%s\n' % line for line in datos)

fichero = open('ejemploArchivo.txt', 'r')

lines = fichero.readlines()
# print(lines)
for line in lines:
    # print(line, end='')
    pass

lines = [line.rstrip('\n') for line in lines]
# print(lines)

fichero.close()

datos = {
    'nombres': ['Nelsi', 'Julian', 'Miguel'],
    'apellidos': ['Miramag', 'Villanueva', 'Nieto'],
    'reto 1': [4.8, 4.5, 5],
    'reto 2': [5, '?', 4.8]
}


# Archivos JSON
import json

datos = {}
datos['Tripulantes'] = []

datos['Tripulantes'].append({
    'nombre': 'Nelsi',
    'apellido': 'Miramag',
    'edad': 20,
    'notas': [4.8, 5]
})

datos['Tripulantes'].append({
    'nombre': 'Julian',
    'apellido': 'Villanueva',
    'edad': 22,
    'notas': 4.5
})

with open('infoTripulantes.json', 'w') as fichero:
    json.dump(datos, fichero, indent=4)

with open('infoTripulantes.json') as fichero:
    datosJSON = json.load(fichero)
    pp(datosJSON)
