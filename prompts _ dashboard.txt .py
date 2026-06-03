#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Jun  1 01:16:29 2026

@author: catalinabellomo
"""

1. PROMPT SEMILLA (ROCA)

ROL:
Sos un experto en desarrollo de interfaces web con Python y Streamlit,
especializado en dashboards científicos y visualización de datos experimentales.

OBJETIVO:
Construir el archivo app.py que funcione como interfaz gráfica interactiva
(Dashboard) del sistema ReflexLab, conectándose con los módulos existentes
en src/.

CONTEXTO:
El sistema ReflexLab analiza datos de una tarea cognitiva Go/No-Go.
El backend ya está implementado con los siguientes módulos en src/:
- carga_datos.py: carga el CSV con pd.read_csv() y devuelve un DataFrame
- validacion_datos.py: valida tipos y valores de cada registro
- procesamiento_datos.py: filtra registros por participante
- metricas.py: calcula tiempo de reacción promedio y tasa de error

El CSV tiene 8 columnas sin encabezado:
id_participante, trial, estimulo, tiempo, respuesta,
tiempo_reaccion, resultado, condicion

Los valores válidos son:
- estimulo: 'go' o 'nogo'
- resultado: 'correcto' o 'incorrecto'
- condicion: 'alta_go' o 'balanceada'

ACCIÓN:
Programá el archivo app.py con Streamlit que cumpla este flujo:
1. st.file_uploader para cargar el CSV
2. Validaciones vectorizadas con Pandas, mostrando errores con st.error
3. KPIs con st.metric: TR promedio, tasa de aciertos, participantes, trials
4. 3 gráficos con st.pyplot: barras, líneas y boxplot
5. Selector de participante con st.selectbox para consulta individual


2. REGISTRO DE ITERACIONES Y CORRECCIONES

ITERACIÓN 1:
La IA generó el código usando importaciones absolutas que fallaban
al correr desde la raíz del proyecto.

PROMPT DE CORRECCIÓN:
"El import de src/ falla con ModuleNotFoundError. Agregá al inicio del
archivo las líneas necesarias para que Python encuentre los módulos
en la carpeta src/ independientemente de desde dónde se corra el script."

RESULTADO: Se agregó sys.path.append() para resolver el problema.

3. REFLEXIÓN TÉCNICA


La estrategia que mejor funcionó fue estructurar el prompt con el método
ROCA (Rol, Objetivo, Contexto, Acción) y adjuntar el diseño.md con la
descripción exacta del sistema. Proveer los nombres de columnas, los
valores válidos y la estructura de módulos existente evitó que la IA
generara código genérico o incompatible con el backend. Las correcciones
necesarias fueron mínimas porque el contexto era preciso desde el inicio.
