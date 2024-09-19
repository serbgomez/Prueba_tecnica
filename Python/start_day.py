# -*- coding: utf-8 -*-
"""
Created on Wed Sep 18 09:07:21 2024

@author: serbg
"""

import datetime

def week_start_date(date, on_monday):
    """
    Calcula la fecha de comienzo de la semana a la que pertenece una fecha dada.

    Parameters
    ----------
    date: str
        Fecha en formato "dd/mm/yyyy"
    on_monday : bool
        True si la semana empieza en lunes, False si empieza en domingo

    Returns
    -------
    str: fecha de inicio de la semana de la fecha indicada

    """
    
    # Convertir la fecha a objeto de la clase datetime
    date_obj = datetime.datetime.strptime(date, '%d/%m/%Y')
    
    # Obtener índice del día de la semana (0 = lunes, 1 = martes, ...)
    num = date_obj.weekday()
    
    # Si el primer día de la semana es el domingo, se ajustan los índices
    # para que quede (0 = domingo, 1 = lunes, ...)
    if not on_monday:
        num = (num+1)%7
    
    # Con esta corrección, lo que se busca ahora es retroceder de forma que el 
    # ínice quede a 0. Para eso basta con restar tantos días como número indique 
    # el índice del día de la semana
    
    date_new = date_obj - datetime.timedelta(days=num)
    
    # Finalmente se cambia el formato de la nueva fecha a string
    return date_new.strftime('%d/%m/%Y')