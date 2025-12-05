from core.tablero import Tablero
from core.ia_minimax import movimiento_gato_minimax, movimiento_raton_minimax
from core.logica_movimiento import movimiento_gato_codicioso, movimiento_raton_aleatorio, movimiento_humano
from core.motor_juego import ejecutar_juego
from utilidades.constantes import tamano_tablero, max_turnos, profundidad_ia

def main():
    print("=== JUEGO DEL GATO Y EL RATÓN ===")
    print("El ratón debe llegar al queso (Q)")
    print("El gato debe atrapar al ratón\n")
    

    
    # Configuración inicial
    pos_gato = (0, 0)
    pos_raton = (7, 0)
    pos_queso = (3, 4)
    
    tablero_inicial = Tablero(                                              # Creamos un tablero con las posiciones iniciales
        tamano=tamano_tablero,                                              # Tamano del tablero
        pos_gato=pos_gato,                                                  # Posicion del gato     
        pos_raton=pos_raton,                                                # Posicion del raton
        pos_queso=pos_queso,                                                # Posicion del queso
        max_turnos=max_turnos                                               # Turnos
    )
    
    print("Elige el modo de juego:")
    print("1. Gato (IA) vs Ratón (IA)")
    print("2. Gato (Codicioso) vs Ratón (Aleatorio)")
    print("3. Humano (Gato) vs IA (Ratón)")
    print("4. IA (Gato) vs Humano (Ratón)")
    
    opcion = input("\nOpción (1,2,3 o 4): ")
    
    if opcion == "1":
        print("\n--- Modo: IA vs IA ---")
        ejecutar_juego(
            tablero_inicial,
            lambda t: movimiento_gato_minimax(t, profundidad_ia),                        # lambda es una función anonima
            lambda t: movimiento_raton_minimax(t, profundidad_ia),
            mostrar_tablero=True
        )
    elif opcion == "2":
        print("\n--- Modo: Codicioso vs Aleatorio ---")
        ejecutar_juego(
            tablero_inicial,
            movimiento_gato_codicioso,
            movimiento_raton_aleatorio,
            mostrar_tablero=True
        )


# Y luego en los casos:
    elif opcion == "3":
        print("\n---Modo: Humano al gato vs IA al ratón---")
        ejecutar_juego(
            tablero_inicial,
            lambda t: movimiento_humano(t, 'gato'),
            lambda t: movimiento_raton_minimax(t, profundidad_ia)
    )    
        
    elif opcion == "4":
        print("\n---Modo: IA al gato vs Humano al ratón---")
        ejecutar_juego(
            tablero_inicial,
            lambda t: movimiento_gato_minimax(t, profundidad_ia),
            lambda t: movimiento_humano(t, 'raton')
        )

    else:
        print("Opción no válida")

if __name__ == "__main__":
    main()


