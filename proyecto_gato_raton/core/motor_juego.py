def ejecutar_juego(tablero_inicial, funcion_gato, funcion_raton, mostrar_tablero=True):         # Función que ejecuta el juego
    """Ejecuta el juego completo"""                                                        # tablero_inicial: el estado inicial del juego 
                                                                                        # funcion_gato: la función que decide cómo se mueve el gato(IA, codicioso o humano)
                                                                                        # funcion_raton: la función que decideCómo se mueve el ratón(IA, aleatorio o humano)
                                                                                        # mostrar_tablero: indica si se muestra el tablero en cada turno

    tablero = tablero_inicial                                                       # copia la referencia al tablero inicial

    if mostrar_tablero:                                                             # si mostrar_tablero es True imprimimos el tablero inicial
        print("\n=== INICIO DEL JUEGO ===")
        tablero.mostrar()
    
    while True:                                                                     # bucle infinito que se ejecuta hasta que el juego se termine
        terminado, resultado = tablero.es_juego_terminado()                          # verifica si el juego terminó
        if terminado:                                                                # si el juego terminó
            if mostrar_tablero:                                                      # si mostrar_tablero es True
                print(f"\n=== {resultado} ===")                                      # imprimimos el resultado
            return resultado, tablero.turno_actual                                  # retornamos el resultado y el turno actual
        
        # Turno del gato
        nueva_pos_gato = funcion_gato(tablero)                                      # llama a la función que decide como se mueve el gato
        tablero = tablero.aplicar_movimiento('gato', nueva_pos_gato)                # aplica el movimiento y actualiza el tablero
                                                                                    # aplicar_movimiento retorna un nuevo tablero, no modifica el original
        if mostrar_tablero:                                                         # si mostrar_tablero imprime el movimiento y el tablero actualizado
            print(f"\nGato se mueve a {nueva_pos_gato}")
            tablero.mostrar()                                                       
        
        terminado, resultado = tablero.es_juego_terminado()                          # verifica si el juego terminó
        if terminado:                                                               # si el juego terminó
            if mostrar_tablero:                                                     # porque el gato pudo ganar
                print(f"\n=== {resultado} ===")                                     # si terminó, sale del loop          
            return resultado, tablero.turno_actual                                          
        
        # Turno del ratón
        nueva_pos_raton = funcion_raton(tablero)                                    # Hace lo mismo que el gato
        tablero = tablero.aplicar_movimiento('raton', nueva_pos_raton)              
        
        if mostrar_tablero:
            print(f"Ratón se mueve a {nueva_pos_raton}")
            tablero.mostrar()                                                       # No verificamos si el juego terminó, porque el loop vuelve al inicio y lo verifica arriba
