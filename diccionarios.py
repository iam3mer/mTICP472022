# Diccionario
# {key: value}

diccionario = {}
#print(type(diccionario))
diccionario = dict()
#print(type(diccionario))

diccionario = {'fruta': 'kiwi', 1: 52455, 2.5: {'Llave': 'Este es el valor'}}
#print(diccionario)
#print(diccionario[1])

profesionales = {
    'Jhon': {
        'ciudad': 'Pereira',
        'profesion': 'Ingeniero de Sistemas y Computación',
        'intereses': {
            'lectura': True,
            'escritura': True,
            'deporte': True
        },
        'habilidades': {
            'programacion': True,
            'bases_de_datos': True,
            'latex': True
        }
    },
    'Astrid': {
        'ciudad': 'Pereira',
        'profesion': 'Licenciada en Educacion Comunicativa',
        'intereses': {
            'lectura': True,
            'escritura': False,
            'deporte': False
        },
        'habilidades': {
            'programacion': True,
            'bases_de_datos': False,
            'latex': False
        }
    }
}

#print(profesionales)

#print(profesionales['Astrid']['intereses'])
#print(profesionales['Astrid']['habilidades']['programacion'])

profesionales['Astrid']['ciudad'] = 'Cali' # actualizo el valor de la ciudad para Astrid
#print(profesionales['Astrid']['ciudad'])

profesional = {
    'ciudad': 'Bogota',
    'profesion': 'Medico',
    'intereses': {
        'lectura': True,
        'escritura': True,
        'deporte': False
    },
    'habilidades': {
        'programacion': True,
        'cirugia': True
    }
}

profesionales['Erika'] = profesional
#print(profesionales)

#print(profesionales.keys())
#print('Angie' in profesionales.keys()) # False
#print('cirugia' in profesionales['Erika']['habilidades'].keys())

#print(profesionales.values())
#print(profesionales['Jhon']['intereses'].values())

profesionales.update(dict(Angie = {}))
#print(profesionales)
profesionales['Angie']['ciudad'] = 'Pereira'
profesionales['Angie']['profesion'] = 'Ingeniera de Sistemas y Computacion'
profesionales['Angie']['intereses'] = dict(lectura=True, escritura=False, deporte=True)
profesionales['Angie']['habilidades'] = {'programacion':True,'bases_de_datos':True,'latex':False}
#print(profesionales['Angie'])

#print(len(profesionales['Angie']['intereses']))

del profesionales['Astrid']
elemento = profesionales.pop('Erika')
#print(profesionales.keys())
#print(elemento)

profesionales.clear()
#print(profesionales)