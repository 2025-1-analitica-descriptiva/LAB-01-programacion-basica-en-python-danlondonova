"""
Escriba el codigo que ejecute la accion solicitada en cada pregunta. Los
datos requeridos se encuentran en el archivo data.csv. En este laboratorio
solo puede utilizar las funciones y librerias basicas de python. No puede
utilizar pandas, numpy o scipy.
"""


def pregunta_11():
    with open("files/input/data.csv", "r") as file:
        resultado = {}
        for linea in file:
            columnas = linea.strip().split("\t")
            if len(columnas) > 4:  # Asegurarse de que hay suficientes columnas
                letra = columnas[3]  # Columna 4
                valor = int(columnas[1])  # Columna 2
                letras = letra.split(",")  # Dividir por comas si hay varias letras
                for letra in letras:
                    if letra in resultado:
                        resultado[letra] += valor
                    else:
                        resultado[letra] = valor
    return dict(sorted(resultado.items()))  # Ordenar el diccionario por clave


if __name__ == "__main__":
    print(pregunta_11())
    
    """
    Retorne un diccionario que contengan la suma de la columna 2 para cada
    letra de la columna 4, ordenadas alfabeticamente.

    Rta/
    {'a': 122, 'b': 49, 'c': 91, 'd': 73, 'e': 86, 'f': 134, 'g': 35}


    """
