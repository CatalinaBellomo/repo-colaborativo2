#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Mar 31 00:52:40 2026

@author: catalinabellomo
"""

def calcular_tiempo_reaccion_promedio(datos):
    """
    Calcula el tiempo de reacción promedio de una lista de registros,
    considerando solo los tiempos mayores a 0.

    Parámetros:
    - datos: list
        Lista de registros válidos.

    Retorna:
    - float
        Tiempo de reacción promedio.
    """
    if len(datos) == 0:
        return 0.0

    suma_tiempos = 0
    cantidad = 0
#por cada timepo de reaccion anotado, si ese timepo es mayor a 0, se agrega para ser considerado en el promedio.
    for registro in datos:
        # Solo se consideran tiempos de reacción mayores a 0, ya que los valores 0 representan ausencia de respuesta registrada y no un tiempo de reacción real.
        if registro["tiempo_reaccion"] > 0:
            suma_tiempos += registro["tiempo_reaccion"]
            cantidad += 1
#si el tiempo de reaccion es 0, devuelve 0.0 la funcion.
    if cantidad == 0:
        return 0.0
#si el timpo de reaccion es distinto a 0, devuelve el promedio de todos los registros de tiempo de reaccion.
    return suma_tiempos / cantidad


def calcular_tasa_error(datos):
    """
    Calcula la proporción de respuestas incorrectas en una lista de registros.

    Parámetros:
    - datos: list
        Lista de registros válidos.

    Retorna:
    - float
        Tasa de error.
    """
#si no hay registro de datos devuelve 0.0
    if len(datos) == 0:
        return 0.0
    errores = 0
#por cada tiempo de reaccion registrado, si contiene un error, se agrega a la variable errores.
    for registro in datos:
        if registro["resultado_respuesta"].lower() == "incorrecto":
            errores += 1

    return errores / len(datos)

