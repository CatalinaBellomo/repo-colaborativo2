#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Mar 31 00:51:53 2026

@author: catalinabellomo
"""

def validar_registro(registro):
    """
    Verifica si un registro tiene tipos y valores válidos.
    Parámetros:
    - registro: dict
    Retorna:
    - bool
    """

    claves_esperadas = [
        "id_participante",
        "trial",
        "estimulo",
        "t_inicio",
        "respuesta",
        "tiempo_reaccion",
        "resultado_respuesta",
        "condicion"
    ]

    for clave in claves_esperadas:
        if clave not in registro:
            return False

    if not isinstance(registro["id_participante"], int):
        return False

    if not isinstance(registro["trial"], int):
        return False

    if not isinstance(registro["estimulo"], str):
        return False

    if not isinstance(registro["t_inicio"], (int, float)):
        return False

    if not isinstance(registro["respuesta"], (str, bool)):
        return False

    if not isinstance(registro["tiempo_reaccion"], (int, float)):
        return False

    if not isinstance(registro["resultado_respuesta"], str):
        return False

    if not isinstance(registro["condicion"], str):
        return False

    if registro["trial"] < 0:
        return False

    if registro["tiempo_reaccion"] < 0:
        return False

    if registro["estimulo"].lower() not in ["go", "nogo"]:
        return False

    if registro["resultado_respuesta"].lower() not in ["correcta", "incorrecta"]:
        return False

    if registro["condicion"].lower() not in ["alta_go", "balanceada"]:
        return False
    
    return True






