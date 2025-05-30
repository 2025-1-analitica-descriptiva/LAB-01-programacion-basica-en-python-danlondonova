"""
Escriba el codigo que ejecute la accion solicitada en cada pregunta. Los
datos requeridos se encuentran en el archivo data.csv. En este laboratorio
solo puede utilizar las funciones y librerias basicas de python. No puede
utilizar pandas, numpy o scipy.
"""


def pregunta_06():
    ruta = "files/input/data.csv"
    data = {}

    with open(ruta, "r") as f:
        for line in f:
            columnas = line.strip().split("\t")  # usar tabulador como separador
            if columnas:
                cod = columnas[4].split(",")  # Columna 5
                for item in cod:
                    if ':' in item:
                        clave, valor = item.split(':')
                        valor = int(valor)
                        if clave not in data:
                            data[clave] = [valor, valor]
                        else:
                            data[clave][1] = max(data[clave][1], valor)
                            data[clave][0] = min(data[clave][0], valor)
    # Convertir el diccionario a una lista de tuplas y ordenar por letra
    resultado = [(letra, valores[0], valores[1]) for letra, valores in data.items()]
    resultado.sort(key=lambda x: x[0])
    return resultado



if __name__ == "__main__":
    print(pregunta_06())
    """
    La columna 5 codifica un diccionario donde cada cadena de tres letras
    corresponde a una clave y el valor despues del caracter `:` corresponde al
    valor asociado a la clave. Por cada clave, obtenga el valor asociado mas
    pequeño y el valor asociado mas grande computados sobre todo el archivo.

    Rta/
    [('aaa', 1, 9),
     ('bbb', 1, 9),
     ('ccc', 1, 10),
     ('ddd', 0, 9),
     ('eee', 1, 7),
     ('fff', 0, 9),
     ('ggg', 3, 10),
     ('hhh', 0, 9),
     ('iii', 0, 9),
     ('jjj', 5, 17)]

    """
