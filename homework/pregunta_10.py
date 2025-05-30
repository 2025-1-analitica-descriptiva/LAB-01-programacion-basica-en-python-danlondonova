"""
Escriba el codigo que ejecute la accion solicitada en cada pregunta. Los
datos requeridos se encuentran en el archivo data.csv. En este laboratorio
solo puede utilizar las funciones y librerias basicas de python. No puede
utilizar pandas, numpy o scipy.
"""


def pregunta_10():
    with open("files/input/data.csv", "r") as file:
        resultado = []  
        for linea in file:
            columns = linea.strip().split("\t")
            if columns:
                letra = columns[0]
                columna4 = columns[3]
                columna5 = columns[4]
                Ccolumna4 = len(columna4.split(",")) if columna4 else 0
                Ccolumna5 = len(columna5.split(",")) if columna5 else 0
                resultado.append((letra, Ccolumna4, Ccolumna5))
    return resultado



if __name__ == "__main__":
    print(pregunta_10())

    """
    Retorne una lista de tuplas contengan por cada tupla, la letra de la
    columna 1 y la cantidad de elementos de las columnas 4 y 5.

    Rta/
    [('E', 3, 5),
     ('A', 3, 4),
     ...
     ('E', 2, 3),
     ('E', 3, 3)]


    """
