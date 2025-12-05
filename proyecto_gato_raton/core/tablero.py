from core.entidades import Gato, Raton, Queso

class Tablero:                                                                      # El corazón del juego 
    """Maneja el estado del juego"""
    def __init__(self, tamano, pos_gato, pos_raton, pos_queso, max_turnos):         # Constructor que inicializa el estado del juego  
        self.tamano = tamano                                                        # Guarda el tamaño del tablero
        self.gato = Gato(pos_gato)                                                  # Crea el objeto gato con su posición inicial
        self.raton = Raton(pos_raton)                                               # Crea el objeto ratón con su posición inicial
        self.queso = Queso(pos_queso)                                               # Lo mismo con el queso
        self.max_turnos = max_turnos                                                # Guarda el turno máximo antes de que gane el ratón
        self.turno_actual = 0                                                       # Guarda el turno actual que empieza en 0

    def obtener_movimientos_gato(self):                                             # Función que devuelve los movimientos posibles del gato
        """Obtiene movimientos posibles del gato"""
        from utilidades.ayudadores import obtener_movimientos_posibles              # Importa la función para obtener los movimientos posibles
        from utilidades.constantes import direcciones                               # Importa las constantes
        return obtener_movimientos_posibles(self.gato.posicion, self.tamano, direcciones)       # Retorna los movimientos posibles del gato 

    def obtener_movimientos_raton(self):                                            
        """Obtiene movimientos posibles del ratón"""
        from utilidades.ayudadores import obtener_movimientos_posibles
        from utilidades.constantes import direcciones
        return obtener_movimientos_posibles(self.raton.posicion, self.tamano, direcciones)     # Lo mismo con el ratón

    def aplicar_movimiento(self, entidad, nueva_pos):                               # Función que aplica el movimiento
        """Crea un nuevo estado con el movimiento aplicado"""
        import copy                                                                 # Importa la librería copy, necesario para copiar objetos
        nuevo_tablero = copy.deepcopy(self)                                         # Crea una copia profunda del tablero completo. Deepcopy porque necesitamos
        if entidad == 'gato':                            #Mueve al gato             # un tablero completamente nuevo sin modificar el original. Crucial para Minimax al simular los movimientos sin afectar el juego real
            nuevo_tablero.gato.posicion = nueva_pos                                 # Actualiza la posición del gato en el nuevo tablero, no en el original
        elif entidad == 'raton':                                                    # Mueve al ratón
            nuevo_tablero.raton.posicion = nueva_pos                                # Actualiza la posición del ratón en el nuevo tablero
        nuevo_tablero.turno_actual += 1                                             # Incrementa el turno sumando 1 al contador
        return nuevo_tablero                                                        # Retorna el nuevo tablero con el movimiento aplicado

    def es_juego_terminado(self):                                                   # Función que verifica si el juego terminó
        """Verifica si el juego terminó"""
        # Gato atrapa al ratón
        if self.gato.posicion == self.raton.posicion:                               # Si gato y ratón se encuentran en la misma casilla, 
            return True, "Gato Gana"                                                # retorna la tupla(True, "Gato") indicando que gana el gato
        # Ratón llega al queso
        if self.raton.posicion == self.queso.posicion:
            return True, "Ratón Gana"
        # Se acabaron los turnos
        if self.turno_actual >= self.max_turnos:                                    # Si se acabaron los turnos,    
            return True, "Ratón Escapa (Se acabaron los turnos)"                    # retorna la tupla(True, "Ratón") indicando que gana el ratón
        return False, None                                                          # Retorna la tupla(False, None) indicando que el juego sigue

    def mostrar(self):                                                              # Función que muestra el tablero
        """Muestra el tablero en consola"""
        from utilidades.constantes import simbolo_gato, simbolo_raton, simbolo_queso, simbolo_vacio         # Importa las constantes
        
        tablero_visual = [[simbolo_vacio for _ in range(self.tamano)] for _ in range(self.tamano)]          # Crea un tablero visual en una lista anidada, con simbolos vacios
        
        # Colocar queso
        tablero_visual[self.queso.posicion[0]][self.queso.posicion[1]] = simbolo_queso
        
        # Colocar ratón
        tablero_visual[self.raton.posicion[0]][self.raton.posicion[1]] = simbolo_raton
        
        # Colocar gato
        tablero_visual[self.gato.posicion[0]][self.gato.posicion[1]] = simbolo_gato
        
        print(f"\nTurno: {self.turno_actual}/{self.max_turnos}")                            # Muestra el turno actual y el turno máximo
        print("  " + " ".join(str(i) for i in range(self.tamano)))                          #  Muestra los números de las columnas
        for i, fila in enumerate(tablero_visual):                                           # Itera sobre el tablero visual y muestra cada fila
            print(f"{i} " + " ".join(fila))                                                 # Muestra la fila con los simbolos correspondientes, y une los símbolos con espacios
