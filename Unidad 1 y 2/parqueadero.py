def parqueadero_buses(idBus:int )-> int:
    
    # dict : {}
    # {key: value}
    # {'nombre': 'Jhonatan'}
    
    lotes = {
        'lote1': [1,2,3,4,5,6,7,8,9,10],
        'lote2': [11,12,13,14,15,16,17,18,19,20],
        'lote3': [21,22,23,24,25,26,27,28,29,30,31]
        }

    if idBus in lotes['lote1']:
        return 1
    elif idBus in lotes['lote2']:
        return 2
    elif idBus in lotes['lote3']:
        return 3

print(parqueadero_buses(5))
print(parqueadero_buses(15))
print(parqueadero_buses(27))

    
