"""
Escriba el codigo que ejecute la accion solicitada en cada pregunta. Los
datos requeridos se encuentran en el archivo data.csv. En este laboratorio
solo puede utilizar las funciones y librerias basicas de python. No puede
utilizar pandas, numpy o scipy.
"""


def pregunta_02():
    ruta = "files/input/data.csv"
    data = {}

    with open(ruta, "r") as f:
        for line in f:
            columnas = line.strip().split("\t")  # usar tabulador como separador
            if columnas:
                letra = columnas[0]  # Primera columna
                data[letra] = data.get(letra, 0) + 1  # Contador de ocurrencias
            dupla = sorted(data.items())  # Ordenar alfabéticamente
    return dupla  # Retornar la lista de tuplas ordenadas
 

if __name__ == "__main__":
    print(pregunta_02())
    


    """
    Retorne la cantidad de registros por cada letra de la primera columna como
    la lista de tuplas (letra, cantidad), ordendas alfabéticamente.

    Rta/
    [('A', 8), ('B', 7), ('C', 5), ('D', 6), ('E', 14)]

    """
