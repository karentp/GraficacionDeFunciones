"""

En este archivo se encuentran las funciones que utiliza 
el programa principal
"""

import sys


def leer_linea(path):
    """

    Función que lee el archivo de entrada y retorna la expresion matematica.

    :param string: dirección del archivo
    :return string: Expresión en la primera línea
    """
    try:
        file = open(path, "r")
        first_line = file.readline()
        file.close()
        return first_line
    except IOError:
        print("El archivo no existe o no se tienen los permisos adecuados")
        sys.exit()
