def evaluar_estado(tablero):                                                    # Función para evaluar el estado del juego
    """Evalúa qué tan bueno es el estado para el gato"""
    from utilidades.ayudadores import calcular_distancia                        # Importa la función para calcular la distancia
    
    # Si el juego terminó
    terminado, resultado = tablero.es_juego_terminado()                         # Verifica si el juego terminó y obtiene el resultado. Desempaqueta la tupla de retorno de es_juego_terminado
    if terminado:                                                               # Si el juego terminó 
        if resultado == "Gato Gana":                                            # Si el resultado es "Gato Gana"
            return 100                                                          # Retorna 100 para el gato
        elif "Ratón" in resultado:                                              # Si el resultado contiene "Ratón"
            return -100                                                         # Retorna -100 para el gato
    
    # Evaluación simple: negativa de la distancia entre gato y ratón
    # Menor distancia = mejor para el gato = puntuación más 
    # Mayor distancia = peor para el gato = puntuación menos
    
    distancia = calcular_distancia(tablero.gato.posicion, tablero.raton.posicion)   # Manhattan enter gato y ratón
    return -distancia                                                               # Retorna la distancia negativa porque el gato quiere minimizar la distancia.
                                                                                    # En otras palabras, el gato quiere maximizar la puntuación, reduciendo la distancia respecto al ratón
def minimax(tablero, profundidad, es_turno_gato, alfa, beta):                        # Función para implementar el algoritmo minimax
    """Algoritmo minimax con poda alfa-beta"""
    # Caso base: profundidad 0 o juego terminado    
    terminado, _ = tablero.es_juego_terminado()                                     # Verifica si el juego terminó y obtiene el resultado. Desempaqueta la tupla de retorno de es_juego_terminado
    if profundidad == 0 or terminado:                                               # Si la profundidad es 0 o el juego terminó
        return evaluar_estado(tablero), None                                        # Retorna la puntuación del estado del juego
    
    if es_turno_gato:
        # Gato maximiza
        mejor_valor = float('-inf')                                                 # Inicializa el mejor valor con un valor negativo infinito
        mejor_movimiento = None                                                     # Inicializa el mejor movimiento con None
        
        for movimiento in tablero.obtener_movimientos_gato():                           # Itera sobre los movimientos posibles del gato
            nuevo_tablero = tablero.aplicar_movimiento('gato', movimiento)               # Aplica el movimiento al nuevo tablero   
            valor, _ = minimax(nuevo_tablero, profundidad - 1, False, alfa, beta)       # Llama recursivamente a minimax con el nuevo tablero(obtiene la puntuacion, ignora el movimiento con _)
            
            if valor > mejor_valor:                                                     # Si el valor es mayor que el mejor valor
                mejor_valor = valor                                                     # Actualiza el mejor valor
                mejor_movimiento = movimiento                                           # Actualiza el mejor movimiento
            
            alfa = max(alfa, valor)                                                     # Actualiza el valor de alfa
            if beta <= alfa:                                                            # Si beta es menor o igual a alfa no tiene que seguir explorando esta rama
                break                                                                   # Rompe el bucle
        
        return mejor_valor, mejor_movimiento                                            # Retorna el mejor valor y el mejor movimiento
    
    else:
        # Ratón minimiza
        mejor_valor = float('inf')                                           # Inicializa el mejor valor con un valor positivo infinito
        mejor_movimiento = None                                              # Inicializa el mejor movimiento con None
        
        for movimiento in tablero.obtener_movimientos_raton():                       # Itera sobre los movimientos posibles del ratón
            nuevo_tablero = tablero.aplicar_movimiento('raton', movimiento)           # Aplica(simula) el movimiento al nuevo tablero
            valor, _ = minimax(nuevo_tablero, profundidad - 1, True, alfa, beta)      # Llama recursivamente(con True, ahora piensa el gato) a minimax con el nuevo tablero(obtiene la puntuacion, ignora el movimiento con _ )
            
            if valor < mejor_valor:                                                 # Si el valor es menor que el mejor valor           
                mejor_valor = valor                                                 # El ratón busca minimizar(valores más bajos)
                mejor_movimiento = movimiento
            
            beta = min(beta, valor)                                                 # Actualiza el mejor valor para el minimizador
            if beta <= alfa:                                                        # Poda desde el lado del ratón
                break
        
        return mejor_valor, mejor_movimiento                                        # Retorna el mejor valor y el mejor movimiento para el ratón

def movimiento_gato_minimax(tablero, profundidad):                                    # Funciones wrappers
    """Calcula el mejor movimiento del gato usando minimax"""                           #Llama a minimax con True, ahora piensa el gato
    _, movimiento = minimax(tablero, profundidad, True, float('-inf'), float('inf'))    # Ignora la puntuacion, solo quiere el movimiento
    return movimiento if movimiento else tablero.gato.posicion                          # Si no hay movimiento válido se queda donde está

def movimiento_raton_minimax(tablero, profundidad):                                     # Acá lo mismo, pero con False, porque es turno del ratón
    """Calcula el mejor movimiento del ratón usando minimax"""
    _, movimiento = minimax(tablero, profundidad, False, float('-inf'), float('inf'))
    return movimiento if movimiento else tablero.raton.posicion
