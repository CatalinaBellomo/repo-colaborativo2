"""
Created on Tue Mar 31 00:58:02 2026

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
=======
import os
import pandas as pd
# Nombres de las columnas del CSV en el orden en que aparecen
COLUMNAS = [
    "id_participante", "trial", "estimulo", "tiempo",
    "respuesta", "tiempo_reaccion", "resultado", "condicion"
]
>>>>>>> 570708aa9447edfe403161b56c34d3829cc9e7c4


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
<<<<<<< HEAD
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


=======
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
>>>>>>> 570708aa9447edfe403161b56c34d3829cc9e7c4
