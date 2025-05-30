"""
Escriba el codigo que ejecute la accion solicitada en cada pregunta. Los
datos requeridos se encuentran en el archivo data.csv. En este laboratorio
solo puede utilizar las funciones y librerias basicas de python. No puede
utilizar pandas, numpy o scipy.
"""


def pregunta_01():
 ruta = "files/input/data.csv"

 with open(ruta, "r") as f:
        suma=0
        for line in f: 
            columnas = line.strip().split("\t") 
            suma += int(columnas[1]) 

        return suma 
       
   
if __name__ == "__main__":
    print(pregunta_01())


    """
    Retorne la suma de la segunda columna.

    Rta/
    214

    """
