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
        # Elimina espacios/saltos de línea y separa por comas
        valores = linea.strip().split(",")
        # Verifica que la línea tenga las 8 columnas esperadas
        if len(valores) != 8:
           raise IndexError("La línea no tiene la cantidad correcta de columnas.")
        # Revisa si hay campos vacíos
        if any(valor.strip() == "" for valor in valores):
           raise ValueError("Hay campos vacíos donde no corresponde.")
        # Controla que respuesta sea True o False
        if valores[4].strip() not in ["True", "False"]:
           raise ValueError("respuesta debe ser 'True' o 'False'.")
        # Convierte los datos al tipo correspondiente y arma diccionario
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
        # Error si falla alguna conversión de tipo
        raise ValueError(f"Error en parsear_linea: no se pudo convertir un valor. Línea: {linea.strip()}") from e

    except IndexError as e:
        # Error si faltan columnas
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
        # Abre el archivo en modo lectura
        with open(ruta, "r") as archivo:
            # Recorre línea por línea
            for linea in archivo:
                # Salta líneas vacías
                if linea.strip() == "":
                    continue
                # Convierte la línea en diccionario
                registro = parsear_linea(linea)
                id_participante = registro["id_participante"]
                participante_encontrado = None
                # Busca si ese participante ya fue cargado antes
                for participante in datos:
                    if participante["id_participante"] == id_participante:
                        participante_encontrado = participante
                        break
                # Guarda solo la información del ensayo actual
                ensayo = {

                    "trial": registro["trial"],
                    "estimulo": registro["estimulo"],
                    "t_inicio": registro["t_inicio"],
                    "respuesta": registro["respuesta"],
                    "tiempo_reaccion": registro["tiempo_reaccion"],
                    "resultado_respuesta": registro["resultado_respuesta"],
                    "condicion": registro["condicion"]

                }

                # Si el participante no existe, lo crea
                if participante_encontrado is None:
                    nuevo_participante = {
                        "id_participante": id_participante,
                        "ensayos": [ensayo]
                    }
                    datos.append(nuevo_participante)
                # Si ya existe, agrega el ensayo a su lista
                else:
                    participante_encontrado["ensayos"].append(ensayo)

    except FileNotFoundError as e:
        # Error si no se encuentra el archivo
        raise FileNotFoundError(
            f"Error en cargar_datos: no se encontró el archivo '{ruta}'."
        ) from e
    return datos


