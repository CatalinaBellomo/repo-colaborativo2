#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Apr 13 13:50:22 2026

@author: matildaivancich
"""
import pandas as pd

def main():
    
      ruta = "datos/ReflexLab_mock_data.csv"

      df = pd.read_csv(ruta, header=None)

      df.columns = [ "id_participante","trial","estimulo","t_inicio",
       "respuesta","tiempo_reaccion","resultado_respuesta","condicion"]
#tengo que llamar atoda slas funciones, pero como no as tengo definidas 
#en este archivo, me aparecen como 'undefined name' 
#que hago? las pego a todas aca?
      validar_estructura(df)
      print('estructura: bien')
      
      validar_datos(df)
      print('datos: bien')
      
      validar_consistencia(ruta)
      print('consistencia: bien')
      
      
      print("Archivo validado correctamente")
      print(ruta.head())    
      
#llamo a la funcion que contiene a todas las funciones de la consigna
main()  