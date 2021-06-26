# Clases y Objetos ------------------------------------

valor = 15
# print(type(valor))

def fun():
    pass

# print(type(fun))

# Forma basica de una clase
class NombreClase:
    pass

miClase = NombreClase()

# print(type(miClase))

class Chocolate:
    pass

chocolate1 = Chocolate()
chocolate2 = Chocolate()

# print(chocolate1)
# print(chocolate2)

# print(Chocolate)
# print(type(chocolate1))
# print(chocolate1.__class__)

# print(Chocolate.__name__)
# print(type(chocolate1).__name__)
# print(chocolate1.__class__.__name__)


# Atributos y Métodos

# Atributos -----------------------------------------------

chocolate3 = Chocolate()
chocolate3.sabor = 'vainilla'
chocolate3.color = 'blanco'

# print(f'El sabor del chocolate es de {chocolate3.sabor} y su color es {chocolate3.color}')

class Chocolate:
    vainilla = True

chocolate = Chocolate()

# if  chocolate.vainilla:
#     print('El chocolate tiene Vainilla')
# else:
#     print('El chocolate no tiene Vainilla')

chocolate.vainilla = False

# if  chocolate.vainilla:
#     print('El chocolate tiene Vainilla')
# else:
#     print('El chocolate no tiene Vainilla')

Chocolate.vainilla = False

nuevo_chocolate = Chocolate()

# print(nuevo_chocolate.vainilla)

# Metodos ------------------------------------------
class Chocolate:
    vainilla = True
    mani = False

    def saludar(soy_el_propio_objeto):
        print('Hola, soy un delicioso chocolate!')
        print(soy_el_propio_objeto)

    def sabor_vainilla(self):
        self.vainilla = False

# Chocolate.saludar()

nuevo_chocolate = Chocolate()
# nuevo_chocolate.saludar()
# print(nuevo_chocolate)

nuevo_chocolate.sabor_vainilla()
# print(nuevo_chocolate.vainilla)

# Metodos Especiales --------------------------------------------

class Chocolate:

    # Constructor de la clase
    def __init__(self, sabor, color, cantidad):
        self.sabor = sabor
        self.color = color
        self.cantidad = cantidad
        # print(f'Acabamos de crear un chocolate sabor {self.sabor} de color {self.color}')
        # print('Soy un chocolate recien salido del molde!')

    # Destructor de la clase
    def __del__(self):
        pass
        # print('Se ha eliminado el chocolate.')

    # String
    def __str__(self):
        return f'Soy un chocolate de color {self.color} y sabor a {self.sabor}'

    # Length
    def __len__(self):
        return self.cantidad

chocolate = Chocolate('vainilla', 'blanco', 15)
# del(chocolate)
# chocolate.__del__()

# print(chocolate)
# print(str(chocolate))
# print(chocolate.__str__())

# print(len(chocolate))
# print(chocolate.__len__())

# Encapsulamiento --------------------------------------------------

class X:
    __atributo_privado = 'Soy un atributo privado y no puedo ser alcanzado desde el exterior.'

    def __metodo_privado(self):
        print('Soy un metodo privado y no puedo ser alcanzado desde el exterior.')

    def atributo_publico(self):
        return self.__atributo_privado

    def metodo_publico(self):
        return self.__metodo_privado()

o = X()
# print(o.__atributo_privado)
# o.__metodo_privado()

# print(o.atributo_publico())
# o.metodo_publico()

# Herencia ----------------------------------------
class Producto:

    def __init__(self, ref, tipo, nombre, pvp, des, productor=None, distribuidor=None, isbn=None, autor=None):
        self.ref = ref
        self.tipo = tipo
        self.nombre = nombre
        self.pvp = pvp
        self.des = des
        self.productor = productor
        self.distribuidor = distribuidor
        self.isbn = isbn
        self.autor = autor

microfono = Producto('545', 'Electronicos', 'Mic Master 2000', 200000, 'Microfono de uso profesional')

# print(microfono)
# print(microfono.des)

class Producto:

    def __init__(self, ref, tipo, nombre, pvp, des):
        self.ref = ref
        self.tipo = tipo
        self.nombre = nombre
        self.pvp = pvp
        self.des = des
    
    def __str__(self):
        return f'REFERENCIA\t {self.ref}\n' \
               f'TIPO\t {self.tipo}\n' \
               f'NOMBRE\t {self.nombre}\n' \
               f'PVP\t {self.pvp}\n' \
               f'DESCRIPCION\t {self.des}\n'

class Libro(Producto):
    isbn = ''
    autor = ''

    def __str__(self):
        return f'TIPO\t {self.tipo}\n' \
               f'NOMBRE\t {self.nombre}\n' \
               f'DESCRIPCION\t {self.des}\n' \
               f'ISBN\t {self.isbn}\n' \
               f'AUTOR\t {self.autor}\n' \
               f'PVP\t {self.pvp}\n'


libro = Libro(3435, 'Libro', 'El Psiconalista', 65000,
'Un psicoanalista atormentado por su pasado busca salvar su vida y la de su familia')
libro.isbn = '346534563fhgh'
libro.autor = 'John Katzenbach'

# print(libro)

def valor_con_descuento(producto, porcentaje):
    producto.pvp = producto.pvp - (producto.pvp * porcentaje / 100)

print(libro)
valor_con_descuento(libro, 10)
print(libro)