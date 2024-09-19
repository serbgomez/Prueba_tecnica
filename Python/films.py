# -*- coding: utf-8 -*-
"""
Created on Wed Sep 18 08:31:17 2024

@author: serbg
"""

# Se usa pandas únicamente para cargar un fichero con datos arbitrarios
import pandas as pd

# Cargar datos simulados
######
# Nota: en caso de error revisar delimitador
######
df = pd.read_csv('films.csv', delimiter=',')


#Convertir los datos de dataframe al formato pedido
data = [tuple(row) for row in df.to_records(index=False)]


# Pregunta 1: Buscar los grupos categoría idioma con más de 20 películas
def more_20(data=data):
    """
    Localiza los grupos categoría/idioma en data que tengan más de 20 películas

    Parameters
    ----------
    data : List
        Listado del número de películas agrupadas por categoría e idioma, 
        recogidas en tuplas en el formato "(Género, Idioma, Número)"

    Returns
    -------
    Lista con los grupos con más de 20 películas

    """
    
    return [i for i in data if i[2] > 20]

def is_lang(lang, data=data):
    """
    Data una lista de idiomas, se comprueba si hay alguna película en al menos uno de ellos

    Parameters
    ----------
    lang : List
        Lista de idiomas
    data : List
        Listado del número de películas agrupadas por categoría e idioma, 
        recogidas en tuplas en el formato "(Género, Idioma, Número)"

    Returns
    -------
    Bool. True si existe alguna película en alguno de los idiomas en lang

    """
    
    for i in data:
        #Para cada tupla de datos, se comprueba si el idioma está en la lista pasada como argumento
        if i[1] in lang:
            return True
    return False



def num_cat(cat, data=data):
    """
    Cuenta el total de películas que hay de una categoría concreta, sin 
    importar el idioma

    Parameters
    ----------
    cat : str
        Categoría a contar
    data : List
        Listado del número de películas agrupadas por categoría e idioma, 
        recogidas en tuplas en el formato "(Género, Idioma, Número)"

    Returns
    -------
    int. Número de películas de la categoría solicitada
    
    """
    # Inicializar suma
    suma = 0
    
    for i in data:
        # Comprobar que la categoría es la solicitada
        if i[0] == cat:
            # En caso afirmativo, sumar el número de películas
            suma += i[2]
    
    return suma


def group_cat(data=data):
    """
    Agrupa las películas por categoría, contando cuantas hay de cada

    Parameters
    ----------
    data : List
        Listado del número de películas agrupadas por categoría e idioma, 
        recogidas en tuplas en el formato "(Género, Idioma, Número)"

    Returns
    -------
    Diccionario con el número de películas en cada categoría

    """
    # Inicializar diccionario (output)
    dic = {}
    
    for i in data:
        # Variable auxiliar con la categoría
        aux = i[0]
        # Si la categoría del elemento actual aún no está en el diccionario,
        # se añade, inicializado al número de películas del elemento actual
        if aux not in dic:
            dic[aux] = i[2]
            
        # En caso contrario, se suma el número de películas a la categoría
        else:
            dic[aux] += i[2]
    
    return dic
        
    