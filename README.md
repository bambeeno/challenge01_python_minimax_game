Juego del Gato y el Ratón

Un juego de estrategia donde el gato intenta atrapar al ratón antes de que llegue al queso. Implementado con el algoritmo Minimax y diferentes modos de juego.

Descripción

Este proyecto simula un juego de persecución en un tablero de 8x8 donde:

El gato debe atrapar al ratón
El ratón debe llegar al queso sin ser atrapado
Si pasan 20 turnos sin captura, el ratón gana por tiempo

Modos de Juego

1- IA vs IA: Dos algoritmos Minimax compitiendo entre sí
2- Codicioso vs Aleatorio: Gato busca al ratón de forma directa, ratón se mueve aleatoriamente
3- Humano vs IA: El humano controla al gato o al ratón contra la IA

Controles (Modo Humano)

W - Mover arriba
S - Mover abajo
A - Mover izquierda
D - Mover derecha

Cómo Ejecutar:

bash
python main.py

Luego se elige el modo de juego que se prefiera.

Estructura del Proyecto

proyecto_gato_raton/
├── main.py                     # Punto de entrada del juego
├── core/
│   ├── tablero.py              # Maneja el estado del juego
│   ├── entidades.py            # Clases Gato, Ratón y Queso
│   ├── ia_minimax.py           # Algoritmo Minimax con poda alfa-beta
│   ├── logica_movimiento.py    # Estrategias de movimiento
│   └── motor_juego.py          # Loop principal del juego
└── utilidades/
    ├── constantes.py           # Configuración del juego
    └── ayudadores.py           # Funciones auxiliares


Algoritmo Minimax

El proyecto implementa el algoritmo Minimax con poda alfa-beta para simular jugadores inteligentes:

- Profundidad: 3 niveles de búsqueda
- Evaluación: Basada en distancia Manhattan entre gato y ratón
- Optimización: Poda alfa-beta para reducir nodos explorados

Modificaciones posibles mediante estos parámetros en utils/constantes.py:

- tamano_tablero: Tamaño del tablero (default: 8x8)
- max_turnos: Turnos máximos antes de que gane el ratón (default: 50)
- profundidad_ia: Profundidad del algoritmo Minimax (default: 3)

Ejemplo de Tablero

Turno: 5/20
  0 1 2 3 4 5 6 7
0 . . . . . . . .
1 . . . G . . . .
2 . . . . . . . .
3 . . . . . . . .
4 . . . . . . . .
5 . . . R . . . .
6 . . . . . . . .
7 . . . . . . . Q

G = Gato
R = Ratón
Q = Queso
. = Casilla vacía

Reglas del Juego

El gato y el ratón se mueven por turnos
Solo pueden moverse a casillas adyacentes (arriba, abajo, izquierda, derecha)
Gato gana si alcanza la misma posición que el ratón
Ratón gana si llega al queso o si sobrevive 20 turnos

Requisitos

- Python 3.7 o superior
- No requiere librerías externas


Características Técnicas

- Código modular y organizado
- Algoritmo Minimax optimizado con poda alfa-beta
- Evaluación heurística simple pero efectiva
- Diferentes estrategias de movimiento (IA, codicioso, aleatorio, humano)
- Interfaz de consola clara y minimalista

Nota

Este proyecto fue desarrollado como parte del estudio de algoritmos de búsqueda adversarial y teoría de juegos. El código está escrito en español para facilitar su comprensión y documentación.


Autor: Alejandro Ruiz Diaz
Lenguaje: Python
Tema: Inteligencia Artificial - Algoritmo Minimax

# Cat and Mouse Game

A strategy game where the cat tries to catch the mouse before it reaches
the cheese. Implemented using the Minimax algorithm and multiple game
modes.

## Description

This project simulates a chase game on an 8x8 board where:

-   The cat must catch the mouse\
-   The mouse must reach the cheese without getting caught\
-   If 20 turns pass with no capture, the mouse wins by timeout

## Game Modes

1.  **AI vs AI:** Two Minimax algorithms competing against each other\
2.  **Greedy vs Random:** Cat moves directly toward the mouse, mouse
    moves randomly\
3.  **Human vs AI:** The player controls either the cat or the mouse
    against the AI

## Controls (Human Mode)

-   **W** -- Move up\
-   **S** -- Move down\
-   **A** -- Move left\
-   **D** -- Move right

## How to Run

``` bash
python main.py
```

Then select the preferred game mode from the menu.

## Project Structure

    proyecto_gato_raton/
    ├── main.py                     # Game entry point
    ├── core/
    │   ├── tablero.py              # Manages game state
    │   ├── entidades.py            # Cat, Mouse, and Cheese classes
    │   ├── ia_minimax.py           # Minimax algorithm with alpha-beta pruning
    │   ├── logica_movimiento.py    # Movement strategies
    │   └── motor_juego.py          # Main game loop
    └── utilidades/
        ├── constantes.py           # Game configuration
        └── ayudadores.py           # Helper functions

## Minimax Algorithm

This project implements the Minimax algorithm with alpha-beta pruning to
simulate intelligent agents:

-   **Depth:** 3 search levels\
-   **Evaluation:** Based on Manhattan distance between the cat and the
    mouse\
-   **Optimization:** Alpha-beta pruning reduces explored nodes

You can modify the following parameters in `utils/constantes.py`:

-   **tamano_tablero:** Board size (default: 8x8)\
-   **max_turnos:** Maximum turns before mouse wins (default: 50)\
-   **profundidad_ia:** Minimax search depth (default: 3)

## Example Board

    Turn: 5/20
      0 1 2 3 4 5 6 7
    0 . . . . . . . .
    1 . . . G . . . .
    2 . . . . . . . .
    3 . . . . . . . .
    4 . . . . . . . .
    5 . . . R . . . .
    6 . . . . . . . .
    7 . . . . . . . Q

    G = Cat
    R = Mouse
    Q = Cheese
    . = Empty cell

## Game Rules

-   Cat and mouse move in alternating turns\
-   They can only move to adjacent cells (up, down, left, right)\
-   Cat wins if it reaches the same position as the mouse\
-   Mouse wins if it reaches the cheese or survives 20 turns

## Requirements

-   Python 3.7 or higher\
-   No external libraries required

## Technical Features

-   Clean and modular code\
-   Minimax algorithm with alpha-beta pruning\
-   Simple but effective heuristic evaluation\
-   Multiple movement strategies (AI, greedy, random, human)\
-   Clear, minimalist console interface

## Note

This project was developed as part of the study of adversarial search
algorithms and game theory. The code is written in Spanish to keep
documentation and learning accessible.

**Author:** Alejandro Ruiz Diaz\
**Language:** Python\
**Topic:** Artificial Intelligence -- Minimax Algorithm
