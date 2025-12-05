class Gato:                                                # Clase Gato
    """Representa al gato en el juego"""
    def __init__(self, posicion):                         # Constructor que se ejecuta al crear un objeto
        self.posicion = posicion                          # Atributo de la clase que almacena donde esta el gato

class Raton:                                              # Clase Raton
    """Representa al ratón en el juego"""
    def __init__(self, posicion):                         # Constructor que se ejecuta al crear un objeto
        self.posicion = posicion                          # Atributo de la clase que almacena donde esta el raton

class Queso:                                              # Clase Queso
    """Representa al queso en el juego"""
    def __init__(self, posicion):                           # Constructor que se ejecuta al crear un objeto
        self.posicion = posicion                            # Atributo de la clase que almacena donde esta el queso

                                                            # Por qué clases separadas si son iguales? Porque aportan claridad y extensibilidad
                                                            # Si en el futuro queremos agregar comportamientos únicos, podemos hacerlo sin afectar el resto,
                                                            # o por el contrario, también podríamos heredar de la clase base y agregar comportamientos adicionales únicos
                                                            # Las clases almacenan la información de las entidades del juego y se encargan de representarlas
                                                            # además de ser responsables de su comportamiento