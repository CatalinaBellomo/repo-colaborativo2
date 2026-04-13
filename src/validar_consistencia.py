#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Apr 13 13:33:03 2026

@author: matildaivancich
"""

def validar_consistencia(registro):
    for i in range(len(registro)):
        tipo = str(registro.loc[i, "estimulo"]).strip().lower()
        respondio = registro.loc[i, "respuesta"]
        tiempo = float(registro.loc[i, "tiempo_reaccion"])
        resultado = str(registro.loc[i, "resultado_respuesta"]).strip().lower()


        if str(respondio).strip().lower() == "true" and tiempo <= 0:
            raise ValueError(f"ERror: en fila {i}: respondió pero tiene un tiempo inválido")

        if str(respondio).strip().lower() == "false" and tiempo != 0:
            raise ValueError(f"Error: en fila {i}: no respondió pero tiene tiempo de reacción")



        if tipo == "go":
            if str(respondio).strip().lower() == "true" and resultado != "correcto":
                raise ValueError(f"ERROR: en fila {i}: si responde a gO, el resultado debe ser correcto")

            if str(respondio).strip().lower() == "false" and resultado != "incorrecto":
                raise ValueError(f"ERROR: en fila {i}: si no responde a gO, el resultado debe ser incorrecto")



        if tipo == "nogo":
            if str(respondio).strip().lower() == "false" and resultado != "correcto":
                raise ValueError(f"ERROR: en fila {i}: si no responde a NOgo, el resultado debe ser correcto")

            if str(respondio).strip().lower() == "true" and resultado != "incorrecto":
                raise ValueError(f"ERROR: en fila {i}: si responde a NOgo, el resultado debe ser incorrecto")
