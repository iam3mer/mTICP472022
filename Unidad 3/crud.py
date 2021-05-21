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
    'Gasesosa Pepsi': {
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


# CREATE
def agregarProducto(db:dict)->dict:
    categorias = ['Nuevos', 'Estrella', 'Temporada', 'Descuento', 'Alimentos', 'Otros']
    marcas = ['Pepsi', 'Acer', 'Pietran', 'LG']

    print('Se va ha agregar un nuevo producto.')

    llaveProducto = input('Ingrese el nombre del producto: ')

    categoria = input('Ingrese la categoria: ')

    marca = input('Ingrese la marca: ')

    while True:
        precio = input('Ingrese el precio: ')

        if precio > 0:
            break
        else:
            print('Debe ingresar un precio mayor a 0')

    while True:
        comestible = input('El producto es comnestibe? [S/s] Sí, [N/n] No: ')

        if comestible == 'S' or comestible == 's':
            fechaVencimiento = input('Ingrese la fecha de vencimiento: ')
            comestible = {'perecedero': True, 'fechaVencimiento': fechaVencimiento}
            break
        elif comestible == 'N' or comestible == 'n':
            comestible = {'perecedero': False}
            break

    while True:
        inventario = input('Ingrese la cantidad de elementos a añadir: ')

        if inventario > 0:
            break
        else:
            print('El inventario debe ser por lo menos 1')

    producto = {
            'categoria': categoria,
            'marca': marca,
            'precio': precio,
            'comestible': comestible,
            'inventario': inventario
    }

    db[llaveProducto] = producto

    return db

print(agregarProducto(dbProductos))