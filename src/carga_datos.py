#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Mar 31 00:50:30 2026

@author: catalinabellomo
"""

def parsear_linea(linea):
    '''
    """
   Convierte una línea del archivo CSV en un diccionario con los datos de un ensayo.
    ----------
    linea : str
      Línea del archivo CSV correspondiente a un registro.

    Returns
    -------
    registro: dict
       Diccionario con los datos del registro.

    '''
  
    valores = linea.strip().split(",")
    registro = {
        "id_participante": int(valores[0]),
        "trial": int(valores[1]),
        "estimulo": valores[2],
        "t_inicio": float(valores[3]),
        "respuesta": valores[4].strip().lower() == "true",
        "tiempo_reaccion": float(valores[5]) if valores[5] != "" else 0.0,
        "resultado_respuesta": valores[6],
        "condicion": valores[7]
    }

    return registro


def cargar_datos(ruta):
    """
    Lee un archivo y devuelve una lista de registros.
    -----------
    Parámetros:
    - ruta: str
    Ruta del archivo CSV.
    
    Returns 
    ----------
    -  datos: list
    Lista de diccionarios, uno por cada línea del archivo.
    """
    datos = []

    with open(ruta, "r") as archivo:
           next(archivo)  # salta el encabezado
           for linea in archivo:
               registro = parsear_linea(linea)
               datos.append(registro)

    return datos

