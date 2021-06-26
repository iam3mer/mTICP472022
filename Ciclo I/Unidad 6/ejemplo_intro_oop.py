from pprint import pprint as pp

libros = [
    {'nombreLibro': 'Los hijos de Húrin', 'nombreAutor': 'J. R. R. Tolkien', 'isbn': '3gh54lkj34'},
    {'nombreLibro': 'Los viajes de Gulliver', 'nombreAutor': 'Jonathan Swift', 'isbn':'k345jh6lk4'},
    {'nombreLibro': 'Conjetura de Golbach', 'nomnbreAutor': 'Apostolos Doxiadis', 'isbn': '4kj5nh64k'}
]

# Consultar libro
def mostrar_libro(dbLibros:list, isbn:str):
    for libro in dbLibros:
        if isbn == libro['isbn']:
            print(f'{libro["nombreLibro"]}, {libro["nombreAutor"]}')
            return
    print('El libro no se encuentra en nuestra biblioteca.')

# Eliminar libro
def borrar_libro(dbLibros:list, isbn:str):
    for i, libro in enumerate(dbLibros):
        if isbn == libro['isbn']:
            del(dbLibros[i])
            print(libro, '> BORRADO')
            return
    print('El libro no se encuentra en nuestra biblioteca.')


# # Mostrar todos los libros
# print('----------------Listado de Libros-----------------')
# pp(libros)

# # Consultar libro
# print('------------------Mostrar Libro-------------------')
# mostrar_libro(libros, '3gh54lkj34')
# mostrar_libro(libros, 'kjl4536kjh')

# # Eliminar libro
# print('------------------Eliminar Libro------------------')
# borrar_libro(libros, 'sdf786s78')
# borrar_libro(libros, '4kj5nh64k')

# # Mostrar todos los libros
# print('----------------Listado de Libros-----------------')
# pp(libros)

# print()

# OOP
# Crea una estructura para los libros
class Libro:

    def __init__(self, nombreLibro, nombreAutor, isbn):
        self.nombreLibro = nombreLibro
        self.nombreAutor = nombreAutor
        self.isbn = isbn

    def __str__(self):
        return '{self.nombreLibro}, {self.nombreAutor}'


# Crea una estructura para la biblioteca
class Biblioteca:

    def __init__(self, libros = []):
        self.libros = libros

    def mostrar_libro(self, isbn:None):
        for libro in self.libros:
            if isbn == libro.isbn:
                print(libro)
                return
        print('El libro no se encuentra en la biblioteca.')

    def borrar_libro(self, isbn:None):
        for i, libro in enumerate(self.libros):
            if isbn == libro.isbn:
                del(self.libros[i])
                print(libro, '> BORRADO')
                return
        print('El libro no se encuentra en la biblioteca.')


# Crear libros
hijos_hurin = Libro('Los hijos de Húrin', 'J. R. R. Tolkien', '3gh54lkj34')
viajes_gulliver = Libro('Los viajes de Gulliver', 'Jonathan Swift', 'k345jh6lk4')
golbach = Libro('Conjetura de Golbach', 'Apostolos Doxiadis', '4kj5nh64k')

# Crea una biblioteca
biblioteca = Biblioteca(libros=[hijos_hurin, viajes_gulliver, golbach])


# Listar toda la biblioteca
print('----------------Libros de la Biblioteca----------------')
print(biblioteca.libros)

# Mostrar un libro
print('--------------------Mostrar un Libro-------------------')
biblioteca.mostrar_libro('4kj5nh64k')
biblioteca.mostrar_libro('dfg87d9fg')

# Eliminar un libro
print('--------------------Eliminar un Libro------------------')
biblioteca.borrar_libro('k345jh6lk4')
biblioteca.borrar_libro('dfg78dfg98')

# Listar toda la biblioteca
print('----------------Libros de la Biblioteca----------------')
print(biblioteca.libros)