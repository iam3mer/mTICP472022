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
    categorias = ['Nuevos', 'Estrella', 'Temporada', 'Descuento', 'Alimentos', 'Otros']
    marcas = ['Pepsi', 'Acer', 'Pietran', 'LG']

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

#baseProductos = agregarProducto(dbProductos)
#baseProductos = agregarProducto(baseProductos)
#baseProductos = agregarProducto(baseProductos)

mostrarInfoProducto(dbProductos)
