#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Jun  1 01:17:49 2026

@author: catalinabellomo
"""

# Diseño del Sistema ReflexLab

## Descripción General
ReflexLab es un sistema de análisis de datos de una tarea cognitiva tipo Go/No-Go.
El sistema carga un archivo CSV con registros experimentales, los valida, calcula
métricas de desempeño y genera visualizaciones.

## Estructura de los Datos
El archivo CSV contiene 8 columnas sin encabezado:

| Columna | Nombre | Tipo | Descripción |
|---|---|---|---|
| 1 | id_participante | int | Identificador del participante |
| 2 | trial | int | Número de ensayo |
| 3 | estimulo | str | Tipo de estímulo: 'go' o 'nogo' |
| 4 | tiempo | float | Tiempo de inicio del estímulo |
| 5 | respuesta | bool | Si el participante respondió (True/False) |
| 6 | tiempo_reaccion | float | Tiempo de reacción en ms (0 si no respondió) |
| 7 | resultado | str | 'correcto' o 'incorrecto' |
| 8 | condicion | str | Condición experimental: 'alta_go' o 'balanceada' |

## Validaciones Implementadas
- Sin campos vacíos o NaN
- Sin tiempos de reacción negativos
- Estímulos válidos: solo 'go' o 'nogo'
- Resultados válidos: solo 'correcto' o 'incorrecto'
- Condiciones válidas: solo 'alta_go' o 'balanceada'
- Tiempo creciente por participante

## Módulos del Sistema (src/)
- `carga_datos.py`: carga el CSV con pd.read_csv() y devuelve un DataFrame
- `validacion_datos.py`: valida tipos y valores de cada registro
- `procesamiento_datos.py`: filtra registros por participante
- `metricas.py`: calcula tiempo de reacción promedio y tasa de error

## Métricas Calculadas
- Tiempo de reacción promedio por condición experimental
- Tasa de aciertos por participante (%)
- Tiempo de reacción promedio individual

## Gráficos Generados
- Barras: TR promedio por condición (alta_go vs balanceada)
- Líneas: evolución del TR por trial y participante
- Boxplot: distribución del TR por participante

## Interfaz Web (app.py)
Dashboard construido con Streamlit que permite:
1. Subir el archivo CSV con st.file_uploader
2. Validar los datos y mostrar errores con st.error
3. Ver KPIs con st.metric
4. Ver los gráficos con st.pyplot
