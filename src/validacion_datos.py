#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Mar 31 00:51:53 2026

@author: catalinabellomo
"""

def validar_registro(registro):
    '''
    Verifica si un registro tiene las claves, tipos y valores válidos.
    '''

    #Lista de claves que TODO registro debe tener
    claves_esperadas = ["id_participante","trial","estimulo","t_inicio",
        "respuesta","tiempo_reaccion","resultado_respuesta","condicion"]

   #Recorremos cada clave esperada para verificar que exista en el diccionario
    for clave in claves_esperadas:
        if clave not in registro:
            # Si falta alguna clave → error
            raise ValueError(f"Falta la clave obligatoria: {clave}")

#VALIDACIÓN DE TIPOS DE DATOS : chequeamos que cada campo tenga el tipo de dato correcto
    if not isinstance(registro["id_participante"], int):
        raise ValueError("id_participante debe ser un entero.")

    if not isinstance(registro["trial"], int):
        raise ValueError("trial debe ser un entero.")

    if not isinstance(registro["estimulo"], str):
        raise ValueError("estimulo debe ser un string.")

    if not isinstance(registro["t_inicio"], (int, float)):
        raise ValueError("t_inicio debe ser numérico.")

    if not isinstance(registro["respuesta"], bool):
        raise ValueError("respuesta debe ser booleano.")

    if not isinstance(registro["tiempo_reaccion"], (int, float)):
        raise ValueError("tiempo_reaccion debe ser numérico.")

    if not isinstance(registro["resultado_respuesta"], str):
        raise ValueError("resultado_respuesta debe ser string.")

    if not isinstance(registro["condicion"], str):
        raise ValueError("condicion debe ser string.")

# VALIDACIÓN DE VALORES 
 # validamos que los valores numéricos tengan sentido
    if registro["id_participante"] <= 0:
        raise ValueError("id_participante debe ser mayor a 0.")

    if registro["trial"] <= 0:
        raise ValueError("trial debe ser mayor a 0.")

    if registro["t_inicio"] < 0:
        raise ValueError("t_inicio no puede ser negativo.")

    if registro["tiempo_reaccion"] < 0:
        raise ValueError("tiempo_reaccion no puede ser negativo.")

    # VALIDACIÓN DE VALORES 
   #usamos lower() para evitar problemas con mayúsculas/minúsculas
    if registro["estimulo"].lower() not in ["go", "nogo"]:
        raise ValueError("estimulo debe ser 'go' o 'nogo'.")

    if registro["resultado_respuesta"].lower() not in ["correcto", "incorrecto"]:
        raise ValueError("resultado_respuesta debe ser 'correcto' o 'incorrecto'.")

    if registro["condicion"].lower() not in ["alta_go", "balanceada"]:
        raise ValueError("condicion debe ser 'alta_go' o 'balanceada'.")

    # Si pasó todas las validaciones entonces el registro es válido
    return True

def validar_tiempo_creciente(datos):
    for participante in datos:
        tiempos = []

        for ensayo in participante["ensayos"]:
            tiempos.append(ensayo["t_inicio"])

        for i in range(1, len(tiempos)):
            if tiempos[i] < tiempos[i - 1]:
                raise ValueError(
                    f"El tiempo t_inicio no está en orden creciente para el participante {participante['id_participante']}.")

