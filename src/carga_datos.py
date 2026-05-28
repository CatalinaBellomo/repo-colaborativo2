"""
Módulo de carga de datos del experimento ReflexLab.
Reemplaza el paradigma manual (with open / split) por carga vectorizada con Pandas.
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

    Reemplaza el procesamiento manual línea por línea (with open, split(","))
    por una carga inmediata y vectorizada con pd.read_csv().

    Parámetros
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
            f"Error en cargar_datos: no se encontró el archivo '{ruta}'."
        )

    df = pd.read_csv(ruta, header=None, names=COLUMNAS)
    print(f"[OK] Archivo cargado: {len(df)} registros, {len(df.columns)} columnas.")
    return df
