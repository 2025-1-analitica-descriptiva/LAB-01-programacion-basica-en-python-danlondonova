"""
Escriba el codigo que ejecute la accion solicitada en cada pregunta. Los
datos requeridos se encuentran en el archivo data.csv. En este laboratorio
solo puede utilizar las funciones y librerias basicas de python. No puede
utilizar pandas, numpy o scipy.
"""


def pregunta_09():
    ruta = "files/input/data.csv"
    data = {}

    with open(ruta, "r") as f:
        for line in f:
            columnas = line.strip().split("\t")  # usar tabulador como separador
            if columnas:
                cod = columnas[4].split(",")  # Columna 5
                for item in cod:
                    if ':' in item:
                        clave, _ = item.split(':')
                        data[clave] = data.get(clave, 0) + 1  # Suma 1 cada vez que aparece
    # Ordenar el diccionario por clave
  
    return data

                     
if __name__ == "__main__":
    print(pregunta_09())
    """
    Retorne un diccionario que contenga la cantidad de registros en que
    aparece cada clave de la columna 5.

    Rta/
    {'aaa': 13,
     'bbb': 16,
     'ccc': 23,
     'ddd': 23,
     'eee': 15,
     'fff': 20,
     'ggg': 13,
     'hhh': 16,
     'iii': 18,
     'jjj': 18}}

    """
