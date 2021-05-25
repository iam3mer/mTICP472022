# CRUD (Create, Read, Update, Delete)

estructuraProductos = {
    'nombreProducto': {
        'categoria': ['Nuevos', 'Estrella', 'Temporada', 'Descuento', 'Alimentos', 'Otros'],
        'marca': ['Pepsi', 'Acer', 'Pietran', 'LG'],
        'precio': 'Precios del producto',
        'comestible': {
            'perecedero': 'True or False',
            'fechaVencimiento': 'dd/mm/yy'
        },
        'inventario': 'Cantidad de productos disponibles'
    }
}

dbProductos = {
    'Gaseosa Pepsi': {
        'categoria': 'Alimentos',
        'marca': 'Pepsi',
        'precio': 5000,
        'comestible': {
            'perecedero': True,
            'fechaVencimiento': '21/05/2021'
        },
        'inventario': 50
    },
    'Portatil VivoBook 14': {
        'categoria': 'Otros',
        'marca': 'Acer',
        'precio': 1800000,
        'comestible': {
            'perecedero': False
        },
        'inventario': 5
    }
}

categorias = ['Nuevos', 'Estrella', 'Temporada', 'Descuento', 'Alimentos', 'Otros']
marcas = ['Pepsi', 'Acer', 'Pietran', 'LG']

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

    db[llaveProducto] = producto

    return db

# READ
def mostrarInfoProducto(db:dict)->None:
    print('Consulta de producto')
    productos = list(db.keys()) # Consulto las llaves y las almaceno en una lista 
    msj = 'Ingrese el nombre del producto a mostrar: '
    producto = verificarElemento(productos, msj)

    #print(db[producto])

    print(f'El producto consultado es: {producto}')
    print(f'Pertenece a la categoria: {db[producto]["categoria"]}')
    print(f'La marca \'del\' producto es: {db[producto]["marca"]}')
    auxPerecedero = db[producto]['comestible']['perecedero']
    print(f'Es comestible? {auxPerecedero}')
    if auxPerecedero == True:
        print(f'Fecha de vencimiento {db[producto]["comestible"]["fechaVencimiento"]}')
    print(f'Unidades en inventario: {db[producto]["inventario"]}')


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
        db[producto]['categoria'] = categoria
    
    msj = 'Desea actualizar la marca? [S/s] Sí [N/n] No '
    if comprobarSN(msj):
        msj = 'Ingrese la marca: '
        marca = verificarElemento(marcas, msj)
        db[producto]['marca'] = marca

    msj = 'Desea actualizar el precio? [S/s] Sí [N/n] No '
    if comprobarSN(msj):
        msj = 'Ingrese el precio: '
        precio = mayorQueCero(msj, 'El precio debe ser mayor que 0.')
        db[producto]['precio'] = precio

    msj = 'Desea actualizar el inventario? [S/s] Sí [N/n] No '
    if comprobarSN(msj):
        msj = 'Ingrese las unidades: '
        inventario = mayorQueCero(msj, 'Debe ingresar almenos una unidad.')
        db[producto]['inventario'] = inventario

    return db
    

# DELETE
def eliminarProducto(db:dict)->dict:
    print('Eliminar producto')
    productos = list(db.keys()) # Consulto las llaves y las almaceno en una lista 
    msj = 'Ingrese el nombre del producto a eliminar: '
    producto = verificarElemento(productos, msj)

    db.pop(producto)

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