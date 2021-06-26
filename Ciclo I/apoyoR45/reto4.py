edadAnimales = {
    'Vertebrados': {
        'Reptiles': [('Cocodrilo', 70), ('Tortuga', 150), ('Tuatara', 117), ('Yacare', 80)],
        'Anfibios': [('Triton', 8), ('Tapalcua', 12), ('Rana', 10)]
    },
    'Invertebrados': {
        'Anelidos': [('Errantes', 50), ('Lombriz', 4), ('Sanguijuela', 26)],
        'Artropodos': [('Escorpion', 6), ('Libelula', .5), ('Cigarra', 10), ('Mariposa', 1)]
    }
}

from functools import reduce

def promedio(data:list)->int:
    promedio = round(reduce(lambda x, y: x + y, data) / len(data), 2)

    return promedio

def consultaAnimales ( opt :int , db:dict , estructura : str = ''):

    promedios = {}
    
    try:
        if opt == 2 and estructura != '':
            respuesta = 'La opción no recibe estructura'

        elif opt == 2:
            for estructura in db:
                animales = []
                tipoAnimales = db[estructura]
                for animal in tipoAnimales:
                    for i in range(len(tipoAnimales[animal])):
                        animales.append(tipoAnimales[animal][i][1])
                promedios[estructura] = promedio(animales)
            respuesta = promedios

        elif opt == 3:
            tipoAnimales = db[estructura]
            for animal in tipoAnimales:
                animales = []
                for i in range(len(tipoAnimales[animal])):
                    animales.append(tipoAnimales[animal][i][1])
                promedios[animal] = promedio(animales)
            respuesta = promedios

        elif opt == 1:
            animalMax = ('',0)
            tipoAnimales = db[estructura]
            for tipo in tipoAnimales:
                animales = tipoAnimales[tipo]
                for animal in animales:
                    if animal[1] > animalMax[1]:
                        animalMax = animal
            respuesta = animalMax

        else:
            respuesta = 'La opción no es valida'
    
    except:
        respuesta = 'La opción ingresada requiere de una estructura animal valida'

    return respuesta