#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Mar 31 00:50:30 2026

@author: catalinabellomo
"""

import os
import pandas as pd

COLUMNAS = [
    "id_participante", "trial", "estimulo", "tiempo",
    "respuesta", "tiempo_reaccion", "resultado", "condicion"
]


def cargar_datos(ruta):
    """
    Carga el archivo CSV del experimento en un DataFrame de Pandas.

    Reemplaza el procesamiento manual LINEA POR LINEa (with open, split(","))
    por una carga inmediata con pd.read_csv().

    Parametros
    ----------
    ruta : str
        Ruta al archivo CSV con los datos del experimento.

    Returns
    -------
    df : pd.DataFrame
        DataFrame con los datos cargados y columnas nombradas.

    Raises
    ------
    FileNotFoundError
        Si el archivo no existe en la ruta indicada.
    """
    if not os.path.exists(ruta):
        raise FileNotFoundError(
            f"Error en cargar_datos: no se encuentra el archivo '{ruta}'."
        )

    df = pd.read_csv(ruta, header=None, names=COLUMNAS)
    print(f"[OK] Archivo cargado: {len(df)} registros, {len(df.columns)} columnas.")
    return df
