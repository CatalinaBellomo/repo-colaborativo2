#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Mar 31 00:52:40 2026

@author: catalinabellomo
"""

def calcular_tiempo_reaccion_promedio(datos):
    """
    Calcula el tiempo de reacción promedio de una lista de registros.

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

    for registro in datos:
        suma_tiempos += registro["tiempo_reaccion"]
        cantidad += 1

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
    if len(datos) == 0:
        return 0.0

    errores = 0

    for registro in datos:
        if registro["resultado_respuesta"].lower() == "incorrecto":
            errores += 1

    return errores / len(datos)
