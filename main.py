#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Mar 31 00:58:02 2026

@author: catalinabellomo
"""
# Importa las funciones necesarias para cargar, validar, filtrar y analizar los datos del experimento
from src.carga_datos import cargar_datos
from src.validacion_datos import validar_registro
from src.procesamiento_datos import filtrar_por_participante
from src.metricas import calcular_tiempo_reaccion_promedio, calcular_tasa_error


def main():
    '''
    Ejecuta el flujo principal del programa.

    Raises
    ------
    ValueError
        Si no se encuentran registros válidos o si el ID ingresado no existe.
        
    Returns
    -------
    None.

    '''


    try: 
        # Se define la ruta del archivo CSV con los datos 
        ruta = "datos/ReflexLab_mock_data_error01.csv"
        

         # Se cargan todos los registros del archivo
        datos = cargar_datos(ruta)

         # Se crea una lista para guardar solo los registros válidos
        datos_validos = []
       
        # Se recorre cada registro y se verifica si cumple las validaciones 
        for registro in datos:
            if validar_registro(registro):
                datos_validos.append(registro)
        
        # Si no hay registros válidos, se detiene la ejecución con un error
        if len(datos_validos) == 0:
            raise ValueError("No se encontraron registros válidos.")

        # Se pide al usuario el ID del participante a analizar
        id_participante = int(input("Ingrese el id del participante: "))
        
        # Se filtran solo los datos del participante ingresado
        datos_participante = filtrar_por_participante(datos_validos, id_participante)
        
        # Si no se encontraron datos para ese participante, se informa el error
        if len(datos_participante) == 0:
            raise ValueError(f"No existe el participante con ID {id_participante}.")
    
        # Se calculan las métricas para ese participante
        promedio = calcular_tiempo_reaccion_promedio(datos_participante)
        tasa_error = calcular_tasa_error(datos_participante)
        
        print("Tiempo de reacción promedio:", promedio)
        print("Tasa de error:", tasa_error)

     # Error si no se encuentra el archivo CSV
    except FileNotFoundError as e:
        print(f"[ERROR CRÍTICO] Tipo de error encontrado: {e} | Ubicación: main")

      # Error si ocurre un problema con los datos o con el ID ingresado
    except ValueError as e:
       print(f"[ERROR CRÍTICO] Tipo de error encontrado: {e} | Ubicación: main")
    
    # Captura cualquier otro error inesperado
    except Exception as e:
       print(f"[ERROR CRÍTICO] Tipo de error encontrado: {e} | Ubicación: main")

  
# Ejecuta la función principal solo si este archivo se corre directamente
if __name__ == "__main__":
    main()
    
    