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
     
    Raises 
    -------
    ValueError
        Si no se puede convertir un valor al tipo esperado.
    IndexError
        Si la línea no tiene la cantidad esperada de columnas.

    '''
  
    try: 
        valores = linea.strip().split(",")
        if len(valores) != 8:
           raise IndexError("La línea no tiene la cantidad correcta de columnas.")
        if any(valor.strip() == "" for valor in valores):
           raise ValueError("Hay campos vacíos donde no corresponde.")
        if valores[4].strip() not in ["True", "False"]:
           raise ValueError("respuesta debe ser 'True' o 'False'.")
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
    except ValueError as e:
        raise ValueError(f"Error en parsear_linea: no se pudo convertir un valor. Línea: {linea.strip()}") from e

    except IndexError as e:
        raise IndexError(f"Error en parsear_linea: faltan columnas en la línea. Línea: {linea.strip()}") from e


def cargar_datos(ruta):
    """
    Lee un archivo CSV y devuelve una lista de registros.

    Parámetros:
    - ruta: str
      Ruta del archivo CSV.

    Returns
    -------
    - datos: list
      Lista de diccionarios, uno por cada línea del archivo.
      
    Raises 
    ------
    FileNotFoundError
        Si no se encuentra el archivo en la ruta indicada.
    """
    datos = []
    
    try:

        with open(ruta, "r") as archivo:
            for linea in archivo:
                if linea.strip() == "":
                    continue
                registro = parsear_linea(linea)
                id_participante = registro["id_participante"]
                participante_encontrado = None
                for participante in datos:
                    if participante["id_participante"] == id_participante:
                        participante_encontrado = participante
                        break
                ensayo = {

                    "trial": registro["trial"],
                    "estimulo": registro["estimulo"],
                    "t_inicio": registro["t_inicio"],
                    "respuesta": registro["respuesta"],
                    "tiempo_reaccion": registro["tiempo_reaccion"],
                    "resultado_respuesta": registro["resultado_respuesta"],
                    "condicion": registro["condicion"]

                }

                if participante_encontrado is None:
                    nuevo_participante = {
                        "id_participante": id_participante,
                        "ensayos": [ensayo]
                    }
                    datos.append(nuevo_participante)
                else:
                    participante_encontrado["ensayos"].append(ensayo)

    except FileNotFoundError as e:
        raise FileNotFoundError(
            f"Error en cargar_datos: no se encontró el archivo '{ruta}'."
        ) from e
    return datos

