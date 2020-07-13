"""Main module."""

import argparse
import sys
from sympy import * # NOQA
from funciones import *

if __name__ == '__main__':

    # Declaro el objeto ArgumentParser
    parser = argparse.ArgumentParser()

    parser.add_argument(
        '--terminalinteractiva',
        '-t',
        action="store_true",
    )
    parser.add_argument(
        '--guardar',
        '-g',     
    )
    parser.add_argument(
        '--limiteinferior',
        '-i',
        type=float,
        required='-t' not in sys.argv
   
    )

    parser.add_argument(
        '--limitesuperior',
        '-s',
        type=float,
        required='-t' not in sys.argv
  
    )

    parser.add_argument(
        '--paso',
        '-p',
        type=int,
        required='-t' not in sys.argv

    )
    parser.add_argument(
        '--cifrassignificativas',
        '-c',
        type=int,
        required='-t' not in sys.argv
    )
    parser.add_argument(
        '--derivadas',
        '-d',
        type=int,
        default=0,   
    )

    parser.add_argument(
        '--archivoentrada',
        '-e',
        required='-t' not in sys.argv
    )
    # Obtengo los argumentos y los guardo en args
    args = parser.parse_args()

    if(args.terminalinteractiva is True):

        while(True):
            try:
                yfuncion = parse_expr(
                    input("Ingrese la función de y, a graficar: "))
            except SyntaxError:
                print("La expresión matemática es invalida")
                sys.exit()

            try:
                derivadas = int(input("Número de derivadas por graficar:\n" +
                                      "0 : ninguna, 1: primera derivada, " +
                                      "2: segunda derivada: "))
            except ValueError:
                print("\nError: "
                      + "Las derivadas deben ser entero 0,1,2 o dejarlo vacio")
                continue
            try:
                limite_inferior = float(
                                  input("¿Cuál es el límite inferior de x?: "))
                limite_superior = float(
                                  input("¿Cuál es el límite superior de x?: "))
                assert limite_inferior < limite_superior
            except AssertionError:
                print("\n Error: "
                      + "El límite inferior debe ser menor al límite superior")
                continue

            try:
                paso = float(
                       input("Ingrese el paso (diferencia entre cada x): "))
                assert paso > 0 and paso < (limite_superior-limite_inferior)
            except ValueError:
                print("\n Error: el paso debe ser flotante")
                continue
            except AssertionError:
                print("\n Error: "
                      + "el paso debe ser mayor a 0 y menor al rango de x")
                continue

            try:
                cifras_significativas = int(input("¿Cuántas cifras " +
                                                  "significativas desea: "))
                assert cifras_significativas > 1
            except ValueError:
                print("\n Error: las cifras significativas deben ser enteros")
                continue
            except AssertionError:
                print("\nError:las cifras significativas deben ser mayor a 1")
                continue

            archivo_guardar = input("Ingrese el archivo donde se guardará" +
                                    "la gráfica (opcional): ")
            break
       
    else:

        archivo_entrada = args.archivoentrada
        yfuncion = leer_linea(archivo_entrada)
        try:
            yfuncion = parse_expr(yfuncion)
        except SyntaxError:
            print("La expresión matemática es invalida")
            sys.exit()
       
        derivadas = int(args.derivadas)
        try:
            limite_inferior = float(args.limiteinferior)
            limite_superior = float(args.limitesuperior)
            assert limite_inferior < limite_superior
        except AssertionError:
            print("\n Error: "
                  + "El límite inferior debe ser menor al límite superior\n")
            sys.exit()

        try:
            paso = float(args.paso)
            assert paso > 0 and paso < (limite_superior-limite_inferior)

        except AssertionError:
            print("\n Error: el paso debe ser mayor a 0 y menor al rango de x")
            sys.exit()
 
        try:
            cifras_significativas = int(args.cifrassignificativas)
            assert cifras_significativas > 1
        except AssertionError:
            print("\n Error: las cifras significativas deben ser mayor a 1")
            sys.exit()
             
        archivo_guardar = args.guardar
 
    lista_funciones = determinar_derivadas(derivadas, yfuncion)
    for i in lista_funciones:
        print (i)
    
    graficar_funcion(limite_superior, limite_inferior,
                     paso, lista_funciones, cifras_significativas)
 
