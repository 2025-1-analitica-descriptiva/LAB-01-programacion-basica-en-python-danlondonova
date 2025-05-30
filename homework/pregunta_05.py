"""
Escriba el codigo que ejecute la accion solicitada en cada pregunta. Los
datos requeridos se encuentran en el archivo data.csv. En este laboratorio
solo puede utilizar las funciones y librerias basicas de python. No puede
utilizar pandas, numpy o scipy.
"""


def pregunta_05():
    ruta = "files/input/data.csv"
    data = {}

    with open(ruta, "r") as f:
        for line in f:
            columnas = line.strip().split("\t")  # usar tabulador como separador
            if columnas:
                letra = columnas[0]
                valor = int(columnas[1])
                if letra not in data:
                    data[letra] = [valor, valor]  # [max, min]
                else:
                    data[letra][0] = max(data[letra][0], valor)
                    data[letra][1] = min(data[letra][1], valor)
    # Convertir el diccionario a una lista de tuplas y ordenar por letra
    resultado = [(letra, valores[0], valores[1]) for letra, valores in data.items()]
    resultado.sort(key=lambda x: x[0])
    return resultado

if __name__ == "__main__":
    print(pregunta_05())

        
    """
    Retorne una lista de tuplas con el valor maximo y minimo de la columna 2
    por cada letra de la columa 1.

    Rta/
    [('A', 9, 2), ('B', 9, 1), ('C', 9, 0), ('D', 8, 3), ('E', 9, 1)]

    """
