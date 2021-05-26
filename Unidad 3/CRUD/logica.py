from datos import *

# CREATE
def agregar(nomProducto:str, infoProducto:dict)->dict:
    dbProductos[nomProducto] = infoProducto
    return dbProductos

# READ
def mostrar(nomProducto:str)->dict:
    return dbProductos[nomProducto]

# UPDATE
def actualizar(nomProducto:str, infoProducto:dict, llaveSec:str)->dict:
    dbProductos[nomProducto][llaveSec] = infoProducto

# DELETE
def eliminar(nomProdcuto:str)->dict:
    return dbProductos.pop(nomProdcuto)


# Funciones de validación

def comprobarSN(msj:str)->bool:
    while True:
        entrada = input(msj)
        if entrada in ['S', 's', 'Si', 'si', 'SI', 'Sí', 'sí']:
            return True
        elif entrada in ['N', 'n', 'No', 'no', 'NO']:
            return False


def mayorQueCero(msjI:str,msjO:str)->int:
    while True:
        valor = input(msjI)
        if valor.isdigit():
            valor = int(valor)
            if valor > 0:
                return valor
            else:
                print(msjO)


def verificarElemento(lista:list, msj:str)->str:
    while True:
        print(lista)
        valor = input(msj)
        if valor in lista:
            return valor


def comprobarFecha(msj:str)->str:
    while True:
        fecha = input(msj) # dd/mm/yy
        if len(fecha) == 8:
            if fecha[2] == '/' and fecha[5] == '/':
                auxFecha = fecha.split('/') # ['dd', 'mm', 'yy']
                if auxFecha[0] == 'dd':
                    continue
                elif auxFecha[0].isdigit and auxFecha[1].isdigit and auxFecha[2].isdigit:
                    if int(auxFecha[0]) > 0 and int(auxFecha[0]) < 31:
                        if int(auxFecha[1]) > 0 and int(auxFecha[1]) < 13:
                            if int(auxFecha[2]) > 20:
                                return fecha
