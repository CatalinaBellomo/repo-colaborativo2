#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Mar 31 00:58:02 2026

@author: catalinabellomo
"""

from src.carga_datos import cargar_datos
from src.validacion_datos import validar_registro
from src.procesamiento_datos import filtrar_por_participante
from src.metricas import calcular_tiempo_reaccion_promedio, calcular_tasa_error


def main():
    """
    Ejecuta el flujo principal del programa.
    """
    ruta = "datos/datos_proyecto.csv"

    datos = cargar_datos(ruta)

    datos_validos = []
    for registro in datos:
        if validar_registro(registro):
            datos_validos.append(registro)

    id_participante = int(input("Ingrese el id del participante: "))
    datos_participante = filtrar_por_participante(datos_validos, id_participante)

    promedio = calcular_tiempo_reaccion_promedio(datos_participante)
    tasa_error = calcular_tasa_error(datos_participante)

    print("Tiempo de reacción promedio:", promedio)
    print("Tasa de error:", tasa_error)


main()



