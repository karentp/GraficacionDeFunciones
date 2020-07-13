"""

En este archivo se encuentran las funciones que utiliza
el programa principal
"""

import sys
from numpy import linspace, arange
import matplotlib.pyplot as plt
from matplotlib import gridspec
from sympy import * # NOQA


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


def graficar_funcion(superior, inferior, paso, funciones, cifras, path_guardar):
    """

    Función que realiza las graficas de la funcion y, y sus derivadas
    según el caso, además las guarda en el archivo dado por el usuario. 

    :param float superior: limite superior de x para la gráfica
    :param float inferior: limite inferior de x para la gráfica
    :param int paso: diferencia entre cada punto de x
    :param lista funciones: lista que contiene las funciones a graficar
    :param int cifras: cantidad de cifras significativas

    """
    x = symbols('x')
#    numero_puntos = (superior-inferior)/paso

    dominio_funciony = linspace(inferior, superior)
    codominio_funciony = [funciones[0].subs(x, valor).evalf(cifras)
                          for valor in dominio_funciony]
    
    plt.rcParams["font.family"] = "serif"
    fig = plt.figure(figsize=(10,10))
    ax1 = fig.add_subplot(len(funciones),1, 1)
    ax1.plot(dominio_funciony, codominio_funciony, color='maroon', linewidth = 2)
    ax1.set(title="Función y ", xlabel="x", ylabel="y")
    ax1.legend([str(funciones[0])])
    ax1.xaxis.set_ticks(arange(inferior, superior+1, paso))
    ax1.set_facecolor('xkcd:pale gray')

    if (len(funciones) > 1):
        codominio_funcion_prima = [funciones[1].subs(x, valor).evalf(cifras)
                                   for valor in dominio_funciony]
        ax2 = fig.add_subplot(len(funciones),1, 2)
        ax2.plot(dominio_funciony, codominio_funcion_prima, color='navy', linewidth = 2)
        ax2.set(title="Función primera derivada de y ", xlabel="x", ylabel="y")
        ax2.legend([str(funciones[1])])
        ax2.xaxis.set_ticks(arange(inferior, superior+1, paso))
        ax2.set_facecolor('xkcd:pale gray') 

    if (len(funciones) > 2):
        codominio_prima_prima = [funciones[2].subs(x, valor).evalf(cifras)
                                 for valor in dominio_funciony]
        ax3 = fig.add_subplot(len(funciones),1, 3)
        ax3.plot(dominio_funciony, codominio_prima_prima, 
                 color='green', linewidth = 2)
        ax3.legend([str(funciones[2])])
        ax3.set(title="Función segunda derivada de y ", xlabel="x", ylabel="y")
        ax3.xaxis.set_ticks(arange(inferior, superior+1, paso))
        ax3.set_facecolor('xkcd:pale gray') 
       
    fig.tight_layout(pad=3.0)

    if (path_guardar != " "):
        plt.savefig(path_guardar)
   
    plt.show()
  

graficar_funcion(10, 0, 3, 
                   [parse_expr("x**2"), parse_expr("x+3"),
                    parse_expr("x**3")], 2, " ")


def determinar_derivadas(orden, funciony):
    """

    Función que calcula las derivadas de la función según el 
    orden dado por el usuario. 

    :param int orden: número de derivadas a calcular
    :param Sympy funciony: funcion que se derivará respecto a x
    :returnlista funciones: lista que contiene la funcion y sus derivadas
    para graficar. 

    """
    x = symbols("x")
    funciones = []
    funciones.append(funciony)

    if (orden == 1 or orden == 2):
        prima = diff(funciony, x)
        funciones.append(prima)

    if (orden == 2):
        prima_segunda = diff(funciony, x, 2)
        funciones.append(prima_segunda)

    return funciones


