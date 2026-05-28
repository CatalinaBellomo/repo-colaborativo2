"""
Created on Tue Mar 31 00:58:02 2026

@author: catalinabellomo
"""

import os
import pandas as pd
# Nombres de las columnas del CSV en el orden en que aparecen
COLUMNAS = [
    "id_participante", "trial", "estimulo", "tiempo",
    "respuesta", "tiempo_reaccion", "resultado", "condicion"
]


def cargar_datos(ruta):
    """
    Carga el archivo CSV del experimento en un DataFrame de Pandas.

    Reemplaza el procesamiento manual línea por línea (with open, split(","))
    por una carga inmediata y vectorizada con pd.read_csv().

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
    # Verifica que el archivo exista antes de intentar abrirlo
    if not os.path.exists(ruta):
        raise FileNotFoundError(
            f"Error en cargar_datos: no se encontró el archivo '{ruta}'."
        )
 # Carga el CSV completo en un DataFrame asignando los nombres de columna
    # header=None indica que el archivo no tiene fila de encabezado
    df = pd.read_csv(ruta, header=None, names=COLUMNAS)
    print(f"[OK] Archivo cargado: {len(df)} registros, {len(df.columns)} columnas.")
    return df
