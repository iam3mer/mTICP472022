def desperdicio_de_gaseosa(amigo_1:dict,amigo_2:dict,amigo_3:dict,capacidad_boton:float, contador:int=0)->str:
    
    contador = contador + 1

    # Que vaso se rego?
    vaso1 = (amigo_1['capacidad_actual'] + capacidad_boton) - amigo_1['capacidad_vaso'] 
    vaso2 = (amigo_2['capacidad_actual'] + capacidad_boton) - amigo_2['capacidad_vaso'] 
    vaso3 = (amigo_3['capacidad_actual'] + capacidad_boton) - amigo_3['capacidad_vaso'] 

    aux1 = vaso1 > 0
    aux2 = vaso2 > 0
    aux3 = vaso3 > 0

    #print(aux1, aux2, aux3)

    # Que vaso se rego primero?
    amigo_1['reboso1'] = amigo_1['capacidad_vaso'] - amigo_1['capacidad_actual'] 
    amigo_2['reboso2'] = amigo_2['capacidad_vaso'] - amigo_2['capacidad_actual'] 
    amigo_3['reboso3'] = amigo_3['capacidad_vaso'] - amigo_3['capacidad_actual'] 

    primero = min(amigo_1['reboso1'],amigo_2['reboso2'],amigo_3['reboso3'])

    if aux1 and aux2 and aux3:
        if amigo_1['reboso1'] == primero:
            return amigo_1['nombre'], contador
        if amigo_2['reboso2'] == primero:
            return amigo_2['nombre'], contador
        if amigo_3['reboso3'] == primero:
            return amigo_3['nombre'], contador
    elif aux1 and aux2:
        if amigo_1['reboso1'] == primero:
            return amigo_1['nombre'], contador
        if amigo_2['reboso2'] == primero:
            return amigo_2['nombre'], contador
    elif aux1 and aux3:
        if amigo_1['reboso1'] == primero:
            return amigo_1['nombre'], contador
        if amigo_3['reboso3'] == primero:
            return amigo_3['nombre'], contador
    elif aux2 and aux3:
        if amigo_1['reboso1'] == primero:
            return amigo_1['nombre'], contador
        if amigo_2['reboso2'] == primero:
            return amigo_2['nombre'], contador
    elif aux1:
        return amigo_1['nombre'], contador
    elif aux2:
        return amigo_2['nombre'], contador
    elif aux3:
        return amigo_3['nombre'], contador
    else:
        return None, contador


#------------------------------------
servir = 5.2

amigo1 = {
    'nombre': 'Raul',
    'capacidad_actual': 7.0,
    'capacidad_vaso': 820.0
    #'reboso1': 5.0
}

amigo2 = {
    'nombre': 'Camilo',
    'capacidad_actual': 6.0,
    'capacidad_vaso': 100.0
}

amigo3 = {
    'nombre': 'Angelica',
    'capacidad_actual': 7.0,
    'capacidad_vaso': 10.0
}

#print(desperdicio_de_gaseosa(amigo1,amigo2,amigo3,servir))

_, contador = desperdicio_de_gaseosa(amigo1,amigo2,amigo3,servir)

_, contador = desperdicio_de_gaseosa(amigo1,amigo2,amigo3,servir, contador)

_, contador =  desperdicio_de_gaseosa(amigo1,amigo2,amigo3,servir, contador)

print(contador)