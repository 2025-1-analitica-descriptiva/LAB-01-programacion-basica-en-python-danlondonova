"""
Escriba el codigo que ejecute la accion solicitada en cada pregunta. Los
datos requeridos se encuentran en el archivo data.csv. En este laboratorio
solo puede utilizar las funciones y librerias basicas de python. No puede
utilizar pandas, numpy o scipy.
"""


def pregunta_12():
    with open("files/input/data.csv", "r") as file:  # Abrir el archivo
        sumacolumna = {}  
        for linea in file:
            columns = linea.strip().split("\t")  # Dividir la línea en columnas
            if columns:  
                letraC1 = columns[0]  
                valorC5 = columns[4]  
            
                suma_valores = 0
                for item in valorC5.split(","): 
                    clave, valor = item.split(":")  
                    suma_valores += int(valor)  
           
                if letraC1 in sumacolumna:
                    sumacolumna[letraC1] += suma_valores
                else:
                    sumacolumna[letraC1] = suma_valores  # Inicializar con el valor

                    
    
    return sumacolumna
if __name__ == "__main__":
    print(pregunta_12())
    """
    Genere un diccionario que contengan como clave la columna 1 y como valor
    la suma de los valores de la columna 5 sobre todo el archivo.

    Rta/
    {'A': 177, 'B': 187, 'C': 114, 'D': 136, 'E': 324}

    """
