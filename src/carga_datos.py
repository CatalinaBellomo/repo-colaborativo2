#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Mar 31 00:50:30 2026

@author: catalinabellomo
"""

def parsear_linea(linea):
    """
    Convierte una línea del archivo en un diccionario.
    Parámetros:
    - linea: str
    Retorna:
    - dict
    """
    valores = linea.strip().split(",")
    valores[0] = int(valores[0])
    valores[1] = int(valores[1])
    valores[5] = float(valores[5]) if valores[5] != '' else None
    return valores
    pass


def cargar_datos(ruta):
    """
    Lee un archivo y devuelve una lista de registros.
    Parámetros:
    - ruta: str
    Retorna:
    - list
    """
      registro_participante = {}
    with open(ruta, 'r') as archivo:
        next(archivo)
        for linea in archivo:
            valores = parsear_linea(linea)
            id_participante = valores[0]
            if id_participante not in registro_participante:
                registro_participante[id_participante] = {"id_participante": id_participante, 'trial': [],'estimulo':[], 't_inicio':[],'respuesta': [], 'tiempo_reaccion': [], 'res_respuesta': [], 'condicion':[]}
            registro_participante[id_participante]['trial'].append(valores[1])
            registro_participante[id_participante]['estimulo'].append(valores[2])
            registro_participante[id_participante]['t_inicio'].append(valores[3])
            registro_participante[id_participante]['respuesta'].append(valores[4])
            registro_participante[id_participante]['tiempo_reaccion'].append(valores[5])
            registro_participante[id_participante]['res_respuesta'].append(valores(6))
            registro_participante[id_participante]['condicion'].append(valores[7])
    return list(registro_participante.values())
    pass


