def despacho_buses(personas_bus: int, personas_estacion: int)->bool:
    """ La estación de Megabus
    Parámetros:
      personas_bus (int): Número de personas en el bus que va a detenerse
      personas_estacion (int): Número de personas esperando el bus en la estación
    Retorno:
      bool: Retorna el valor True si se debe despachar un bus nuevo y retorna False de lo contrario.
    """

    # Capacidad igual a 150 personas
    # Capacidad maxima igual a 200 personas
    # Las personas se suben a bus con sobre cupo si hay 40 o más usuarios en 
    # plataforma

    # Si bus se va con sobre cubo o si en plataforma quedan 50 o mas usuarios
    # despachar bus

    CAPACIDAD = 150

    cupo = CAPACIDAD - personas_bus
    #cupo = 150 - 50 = 100
    enPlataforma = personas_estacion - cupo
    #enPlataforma = 200 - 100 = 100
    
    if personas_bus > CAPACIDAD or enPlataforma >= 40:
        return True
    else:
        return False

print(despacho_buses(50,200)) # True, Se suben 150 usuarios al bus
print(despacho_buses(170,10)) # True, No se sube ningun usuario al bus
print(despacho_buses(50,10))  # False, Se suben todos los usuarios al bus (10)
print(despacho_buses(50,50))  # False, Se suben todos los usuarios al bus (50)
print(despacho_buses(140,20)) # False, Se suben 10 usuarios al bus
print(despacho_buses(149,30)) # False, se sube una persona
print(despacho_buses(100,90)) # True, se suben 50 personas