#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Mar 31 00:58:33 2026

@author: catalinabellomo
"""

# Proyecto ReflexLab

Este repositorio contiene el desarrollo colaborativo del proyecto ReflexLab.
El objetivo del programa es leer datos de una tarea cognitiva tipo Go/No-Go, validarlos, procesarlos y calcular métricas básicas de desempeño, como el tiempo de reacción promedio y la tasa de error.


## Integrantes
- Catalina Bellomo
- Ana Maria Piuma 
- Matilda Ivancich
- Allegra Gegenschatz

## Estructura
- src/: funciones del sistema
- `src/carga_datos.py`: carga y parsea los datos desde el archivo CSV.
- `src/validacion_datos.py`: valida que cada registro tenga la estructura, tipos y valores correctos.
- `src/procesamiento_datos.py`: filtra los registros por participante.
- `src/metricas.py`: calcula métricas a partir de los datos validados.
- main.py: programa principal
- datos/: archivos de datos
- diagramas/: diagramas del sistema

## Funciones principales
- `carga_datos.py`: lectura y transformación de datos
- `validacion_datos.py`: validación de tipos y valores
- `procesamiento_datos.py`: filtrado de datos por participante
- `metricas.py`: cálculo de métricas básicas

## Métricas implementadas
- Tiempo de reacción promedio
- Tasa de error

### Errores identificados
Durante el desarrollo se identificaron los siguientes posibles puntos de quiebre:

- Ruta incorrecta o archivo CSV inexistente.
- Líneas mal formadas o con menos columnas de las esperadas.
- Valores no numéricos en campos que deberían ser enteros o flotantes.
- Registros con claves faltantes.
- Valores fuera de rango, por ejemplo:
  - `id_participante <= 0`
  - `trial <= 0`
  - `t_inicio < 0`
  - `tiempo_reaccion < 0`
- Valores inconsistentes en campos categóricos, por ejemplo:
  - `estimulo` distinto de `go` o `nogo`
  - `resultado_respuesta` distinto de `correcto` o `incorrecto`
  - `condicion` distinta de `alta_go` o `balanceada`
- Ingreso de un ID de participante inexistente.
- Ausencia total de registros válidos para procesar.

### Cómo se manejan los errores en cada función

#### `parsear_linea(linea)` en `carga_datos.py`
Esta función convierte una línea del CSV en un diccionario.  
Utiliza `try-except` para capturar:

- `ValueError`: cuando un valor no puede convertirse al tipo esperado.
- `IndexError`: cuando la línea no tiene la cantidad esperada de columnas.

En ambos casos se lanza una excepción con un mensaje claro indicando que el problema ocurrió al parsear una línea del archivo.

#### `cargar_datos(ruta)` en `carga_datos.py`
Esta función abre el archivo CSV y carga todos los registros.  
Utiliza `try-except` para capturar:

- `FileNotFoundError`: cuando la ruta del archivo es incorrecta o el archivo no existe.

Si ocurre este error, se informa claramente que no se pudo encontrar el archivo indicado.

#### `validar_registro(registro)` en `validacion_datos.py`
Esta función verifica que cada registro:
- tenga todas las claves necesarias,
- tenga los tipos de datos esperados,
- respete rangos válidos,
- y contenga valores consistentes según el experimento.

Si alguna validación falla, la función devuelve `False` y el registro no se incluye en la lista de datos válidos.

#### `filtrar_por_participante(datos, id_participante)` en `procesamiento_datos.py`
Esta función selecciona únicamente los registros asociados al participante ingresado.  
Si no se encuentran registros para ese ID, el control del error se realiza en `main.py`.

#### `calcular_tiempo_reaccion_promedio(datos)` en `metricas.py`
Calcula el promedio de los tiempos de reacción mayores a 0.  
Se excluyen los valores iguales a 0 porque no representan un tiempo de reacción real, sino ausencia de respuesta registrada.

Si no hay datos disponibles, devuelve `0.0`.

#### `calcular_tasa_error(datos)` en `metricas.py`
Calcula la proporción de respuestas incorrectas sobre el total de registros del participante.

Si no hay datos disponibles, devuelve `0.0`.

#### `main()` en `main.py`
La función principal coordina todo el flujo del programa.  
Utiliza `try-except` para manejar errores críticos y detener la ejecución de forma controlada.

Se contemplan los siguientes casos:
- archivo no encontrado,
- ausencia de registros válidos,
- ID inexistente,
- ingreso inválido por parte del usuario,
- errores inesperados.

En todos los casos se muestra un mensaje claro en consola indicando el problema detectado.

## Uso de herramientas de IA
Se utilizó IA como herramienta de consulta y apoyo para revisar lógica del código, validaciones, manejo de errores.

##Moldeo del sistema usando Objetos:
- Clase Trial: representa ensayo ndividual de la tarea Go/No-Go
    - Atributos:
        - 'estimulo' / str / tipo de estimulo presentadon('go' o 'nogo'
        - 't_inicio' / float / tiempo de inicio del estimulo
        - 'respuesta' / 'bool' / si el participante respondio o no
        - 'tiempo_reaccion' / float / tiempo transcurrido hasta la respuesta
        - 'resultado_respuesta' / str / si fue correcta o incorrecta
  - Metodo:
      - es_correcto() / devuelve 'True' si el resultado fue correcto
      - es_error_comision() / devuele 'True' si recpondio ante estimulo No-Go
      - es_error_omision()/ devuelve 'True' si no respondio ante un estimulo Go
   
- Clase Paticipante:Represente a un participante y agrupa todos sus ensayos
    Atributos:
      -   id_participante / int / identificador unico del participante
      - condicion / str / condicion experimental
      - trials / list[trial] / lista de ensayos del participante
  Metodo:
    - 'agregar_trial(trial)' / agrega un objeto 'Trial' a la lista
    - 'calcular_tiempo_reaccion_promedio()' / retorna el promedio de tiempos de reaccion
    - calcular_tasa_error()' / retorna proporcion de respuestas incorrectas
    - 'contar_errores_comision()' / cuenta respuestas ante estimulos No-Go
    - 'contar_errores_omision()' / cuenta ausencias de respuesta ante estimulos Go
 
- Clase EExperimento: Contiene y gestiona participantes cargados
  Atributos:
    - participantrs / list[participante] / lista de todos los participantes
  Metodo:
    - 'cargar_desde_archivo(ruta)'/lee el CSV y construye los objetos 'Participante' y 'Trial'
    - 'buscar_participante(id_participante)' / retorna el 'participante' con ese ID
    - 'resumen_general()' / muestra metricas agregadas de todos los participantes 
  
