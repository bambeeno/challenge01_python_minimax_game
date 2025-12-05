def movimiento_raton_aleatorio(tablero):                                            # Función que decide como se mueve el ratón
    """El ratón se mueve aleatoriamente"""  
    import random
    movimientos = tablero.obtener_movimientos_raton()                               # Obtiene los movimientos posibles
    if not movimientos:                                                             # Si no hay movimientos posibles
        return tablero.raton.posicion                                               # Devuelve la posición actual
    return random.choice(movimientos)                                               # Devuelve un movimiento aleatorio  

def movimiento_gato_codicioso(tablero):                                             # Función que decide como se mueve el gato
    """El gato se mueve hacia el ratón de forma codiciosa"""
    from utilidades.ayudadores import calcular_distancia                             # Importa la función para calcular la distancia    
    
    movimientos = tablero.obtener_movimientos_gato()                                 # Obtiene los movimientos posibles
    if not movimientos:                                                             # Si no hay movimientos posibles
        return tablero.gato.posicion                                                # Devuelve la posición actual
    
    mejor_movimiento = tablero.gato.posicion                                        # Guarda la mejor posicion 
    min_distancia = calcular_distancia(tablero.gato.posicion, tablero.raton.posicion)   # Guarda la mejor distancia  
    
    for movimiento in movimientos:                                                  # Itera sobre los movimientos posibles
        distancia = calcular_distancia(movimiento, tablero.raton.posicion)              # Calcula la distancia
        if distancia < min_distancia:                                                   # Si la distancia es mejor  
            min_distancia = distancia                                                   # Actualiza la mejor distancia
            mejor_movimiento = movimiento                                               # Actualiza la mejor posicion
    
    return mejor_movimiento                                                             # Devuelve la mejor posicion


def movimiento_humano(tablero, entidad):                                            # Función que decide como se mueve el humano
    """El humano elige su movimiento con las teclas w/a/s/d"""
    if entidad == 'gato':                                                           # Si es el gato
        pos_actual = tablero.gato.posicion                                          # Guarda la posicion actual
        movimientos = tablero.obtener_movimientos_gato()                            # Obtiene los movimientos posibles
        print(f"\nTu posición actual (Gato): {pos_actual}")                         # Muestra la posicion actual
    else:                                                                           # Si es el ratón
        pos_actual = tablero.raton.posicion                                         # Guarda la posicion actual del ratón
        movimientos = tablero.obtener_movimientos_raton()                           # Obtiene los movimientos posibles
        print(f"\nTu posición actual (Ratón): {pos_actual}")                         # Muestra la posicion actual


        # Mapeo de teclas de direcciones
    teclas = {
        'w': (-1, 0),     #Arriba
        's': (1, 0),      #Abajo
        'a': (0, -1),     #Izquierda
        'd': (0, 1)       #Derecha
    }
    
    print("Controles: W(arriba) S(abajo) A(izquierda) D(derecha)")

    while True:
        tecla = input("Tu movimiento: ").lower()

        if tecla not in teclas:
            print("Tecla inválida. Utiliza los comandos sugeridos")
            continue
        # Calcula la nueva posición
        direccion = teclas[tecla]                                                                   # Obtiene la direccion
        nueva_posicion = (pos_actual[0] + direccion[0], pos_actual[1] + direccion[1])                # Calcula la nueva posicion

        # Verifica si el movimiento es válido
        if nueva_posicion in movimientos:                                                         
            return nueva_posicion                                                                 
        else:                                                                                       # Si no es valido
            print("Movimiento inválido (fuera del tablero)")