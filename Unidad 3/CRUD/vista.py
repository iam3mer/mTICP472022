from logica import *
from datos import *


# CREATE
def agregarProducto(db:dict)->dict:

    print('Se va ha agregar un nuevo producto.')

    llaveProducto = input('Ingrese el nombre del producto: ')

    msj = 'Ingrese la categoria: '
    categoria = verificarElemento(categorias, msj)

    msj = 'Ingrese la marca: '
    marca = verificarElemento(marcas, msj)

    msjI = 'Ingrese el precio: '
    msjO = 'Debe ingresar un precio mayor a 0'
    precio = mayorQueCero(msjI,msjO)

    while True:
        comestible = input('El producto es comnestibe? [S/s] Sí, [N/n] No: ')

        if comestible == 'S' or comestible == 's':
            msj = 'Ingrese la fecha de vencimiento: '
            fechaVencimiento = comprobarFecha(msj)
            comestible = {'perecedero': True, 'fechaVencimiento': fechaVencimiento}
            break
        elif comestible == 'N' or comestible == 'n':
            comestible = {'perecedero': False}
            break

    msjI = 'Ingrese la cantidad de elementos a añadir: '
    msjO = 'El inventario debe ser por lo menos 1'
    inventario = mayorQueCero(msjI,msjO)

    producto = {
            'categoria': categoria,
            'marca': marca,
            'precio': precio,
            'comestible': comestible,
            'inventario': inventario
    }

    #db[llaveProducto] = producto
    return agregar(llaveProducto, producto)

# READ
def mostrarInfoProducto(db:dict)->None:
    print('Consulta de producto')
    productos = list(db.keys()) # Consulto las llaves y las almaceno en una lista 
    msj = 'Ingrese el nombre del producto a mostrar: '
    producto = verificarElemento(productos, msj)

    infoProducto = mostrar(producto)

    print(f'El producto consultado es: {producto}')
    print(f'Pertenece a la categoria: {infoProducto["categoria"]}')
    print(f'La marca \'del\' producto es: {infoProducto["marca"]}')
    auxPerecedero = infoProducto['comestible']['perecedero']
    print(f'Es comestible? {auxPerecedero}')
    if auxPerecedero == True:
        print(f'Fecha de vencimiento {infoProducto["comestible"]["fechaVencimiento"]}')
    print(f'Unidades en inventario: {infoProducto["inventario"]}')
    print(f'El precio es: {infoProducto["precio"]}')


#UPDATE
def actualizarProducto(db:dict)->dict:
    print('Actualizar producto')
    productos = list(db.keys()) # Consulto las llaves y las almaceno en una lista 
    msj = 'Ingrese el nombre del producto a actualizar: '
    producto = verificarElemento(productos, msj)

    msj = 'Desea actualizar la categoria? [S/s] Sí [N/n] No '
    if comprobarSN(msj) == True:
        msj = 'Ingrese la categoria: '
        categoria = verificarElemento(categorias, msj)
        actualizar(producto, categoria, 'categoria')
        #db[producto]['categoria'] = categoria
    
    msj = 'Desea actualizar la marca? [S/s] Sí [N/n] No '
    if comprobarSN(msj):
        msj = 'Ingrese la marca: '
        marca = verificarElemento(marcas, msj)
        actualizar(producto, marca, 'marca')
        #db[producto]['marca'] = marca

    msj = 'Desea actualizar el precio? [S/s] Sí [N/n] No '
    if comprobarSN(msj):
        msj = 'Ingrese el precio: '
        precio = mayorQueCero(msj, 'El precio debe ser mayor que 0.')
        actualizar(producto, precio, 'precio')
        #db[producto]['precio'] = precio

    msj = 'Desea actualizar el inventario? [S/s] Sí [N/n] No '
    if comprobarSN(msj):
        msj = 'Ingrese las unidades: '
        inventario = mayorQueCero(msj, 'Debe ingresar almenos una unidad.')
        actualizar(producto, inventario, 'inventario')
        #db[producto]['inventario'] = inventario

    return db
    

# DELETE
def eliminarProducto(db:dict)->dict:
    print('Eliminar producto')
    productos = list(db.keys()) # Consulto las llaves y las almaceno en una lista 
    msj = 'Ingrese el nombre del producto a eliminar: '
    producto = verificarElemento(productos, msj)

    eliminar(producto)

    print(f'El producto {producto} ha sido eliminado.')

    return db


def menu(dbProductos:dict)->None:
    while True:
        print('---------- CRUD ----------')
        print('--------------------------')
        print('-1- Agregar producto.')
        print('-2- Actualizar producto.')
        print('-3- Mostrar iformación de producto.')
        print('-4- Eliminar producto.')
        print('-5- Salir.')

        opcion = input('Ingrese una opción: ')

        if opcion == '1':
            dbProductos = agregarProducto(dbProductos)
        elif opcion == '2':
            dbProductos = actualizarProducto(dbProductos)
        elif opcion == '3':
            mostrarInfoProducto(dbProductos)
        elif opcion == '4':
            dbProductos = eliminarProducto(dbProductos)
        elif opcion == '5':
            break

menu(dbProductos)