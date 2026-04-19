#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Mar 31 00:58:02 2026

@author: catalinabellomo
"""
# Importa las funciones necesarias para cargar, validar, filtrar y analizar los datos del experimento
from src.carga_datos import cargar_datos
from src.validacion_datos import validar_registro, validar_tiempo_creciente
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
        ruta = "datos/ReflexLab_mock_data_error05.csv"

         # Se cargan todos los registros del archivo
        datos = cargar_datos(ruta)
        
        for participante in datos:
            for ensayo in participante["ensayos"]:
                registro_completo = {
            "id_participante": participante["id_participante"],
            "trial": ensayo["trial"],
            "estimulo": ensayo["estimulo"],
            "t_inicio": ensayo["t_inicio"],
            "respuesta": ensayo["respuesta"],
            "tiempo_reaccion": ensayo["tiempo_reaccion"],
            "resultado_respuesta": ensayo["resultado_respuesta"],
            "condicion": ensayo["condicion"] }
            
            validar_registro(registro_completo)

        validar_tiempo_creciente(datos)
              
       
        id_participante = int(input("Ingrese el id del participante: "))
        datos_participante = filtrar_por_participante(datos, id_participante)
       
        # Si no hay registros válidos, se detiene la ejecución con un error
        if len(datos_participante) == 0:
            raise ValueError("No se encontraron registros válidos.")

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
    
    