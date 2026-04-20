#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Mar 31 00:52:18 2026

@author: catalinabellomo
"""

def filtrar_por_participante(datos, id_participante):
    """
    Filtra los datos correspondientes a un participante específico.

    Parámetros:
    - datos: list
        Lista de registros del experimento.
    - id_participante: int
        Identificador del participante que se quiere filtrar.

    Retorna:
    - list
        Lista con los registros del participante indicado.
    """
# por cada participante en la lista 'datos'recorre su identificador numerico y devuelve una lista con los registros de in participante en particular.
    for participante in datos:
        if participante["id_participante"] == id_participante:
            return participante["ensayos"]

    return []



