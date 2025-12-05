def calcular_distancia(pos1, pos2):                                         # Función para calcular la distancia de Manhattan
    """Calcula la distancia de Manhattan entre dos posiciones"""
    return abs(pos1[0] - pos2[0]) + abs(pos1[1] - pos2[1])                  #  |fila1 - fila2| + |col1 - col2| Suma de las diferencias absolutas de filas y columnas
                                                                            # Se usa para evaluar qué tan cerca está el gato del ratón
def es_posicion_valida(pos, tamano):                                        # Función para verificar si una posición es válida
    """Verifica si una posición está dentro del tablero"""
    fila, col = pos                                                         # Se desempaqueta o desestructura la tupla pos
    return 0 <= fila < tamano and 0 <= col < tamano                         # Verifica si la fila y la columna están dentro del rango del tablero
                                                                            # Retorna True si la posición es válida, False en caso contrario
def obtener_movimientos_posibles(posicion, tamano, direcciones):            # Función para obtener todos los movimientos posibles desde una posición. Retorna una lista
    """Calcula todos los movimientos válidos desde una posición"""
    movimientos = []                                                        # Lista vacía para almacenar los movimientos posibles
    for df, dc in direcciones:                                              # Itera sobre las direcciones de movimiento                             
        nueva_fila = posicion[0] + df                                       # Calcula la nueva fila y la nueva columna sumando el cambio o diferencia
        nueva_col = posicion[1] + dc                                        # Suma la diferencia de filas y la diferencia de columnas
        nueva_pos = (nueva_fila, nueva_col)                                 # Crea una tupla con la nueva fila y la nueva columna
        if es_posicion_valida(nueva_pos, tamano):                           # Verifica si la nueva posición es válida
            movimientos.append(nueva_pos)                                   # Y si es, la agrega a la lista movimientos[]
    return movimientos                                                      # Retorna la lista de movimientos posibles desde la posición dada