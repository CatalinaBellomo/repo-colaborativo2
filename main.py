#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Mar 31 00:58:02 2026

@author: catalinabellomo
"""
# Importa las funciones necesarias para cargar, validar, filtrar y analizar los datos del experimento

import os
import pandas as pd
import matplotlib.pyplot as plt


from src.carga_datos import cargar_datos
from src.procesamiento_datos import filtrar_por_participante
from src.metricas import calcular_tiempo_reaccion_promedio, calcular_tasa_error

RUTA_CSV = "datos/ReflexLab_mock_data.csv"
CARPETA_GRAFICOS = "graficos"

def grafico_barras_tiempo_reaccion_condicion(df):
    """
    Genera y guarda un gráfico de barras con el tiempo de reacción promedio
    por condición experimental (alta_go vs balanceada).

    Parámetros
    ----------
    df : pd.DataFrame
        DataFrame con los datos del experimento (solo ensayos go con TR > 0).
    """
    df_go = df[(df["estimulo"] == "go") & (df["tiempo_reaccion"] > 0)]
    tr_por_condicion = df_go.groupby("condicion")["tiempo_reaccion"].mean().round(2)

    plt.figure(figsize=(9, 5))
    tr_por_condicion.plot(
        kind="bar",
        color=["#1e3a8a", "#b45309"],
        edgecolor="black",
        alpha=0.85
    )
    plt.title(
        "Tiempo de Reacción Promedio por Condición Experimental",
        fontsize=13, fontweight="bold", pad=15
    )
    plt.xlabel("Condición", fontsize=11)
    plt.ylabel("Tiempo de Reacción Promedio (ms)", fontsize=11)
    plt.xticks(rotation=0)
    plt.grid(True, linestyle="--", alpha=0.5, axis="y")
    plt.tight_layout()

    ruta = os.path.join(CARPETA_GRAFICOS, "comparacion_condiciones.png")
    plt.savefig(ruta, dpi=300)
    plt.close()
    print(f"[OK] Gráfico guardado: {ruta}")


def grafico_lineas_tr_sujeto(df):
    """
    Genera y guarda un gráfico de líneas con la evolución del tiempo de
    reacción por trial para cada participante (solo ensayos go con TR > 0).

    Parámetros
    ----------
    df : pd.DataFrame
        DataFrame con los datos del experimento.
    """
    df_go = df[(df["estimulo"] == "go") & (df["tiempo_reaccion"] > 0)]

    plt.figure(figsize=(11, 5))
    for sujeto_id, grupo in df_go.groupby("id_participante"):
        plt.plot(
            grupo["trial"],
            grupo["tiempo_reaccion"],
            marker="o", markersize=3, linewidth=1.5,
            label=f"Sujeto {sujeto_id}"
        )
    plt.title(
        "Evolución del Tiempo de Reacción por Trial y Participante",
        fontsize=13, fontweight="bold", pad=15
    )
    plt.xlabel("Trial", fontsize=11)
    plt.ylabel("Tiempo de Reacción (ms)", fontsize=11)
    plt.legend(fontsize=9, loc="upper right")
    plt.grid(True, linestyle=":", alpha=0.6)
    plt.tight_layout()

    ruta = os.path.join(CARPETA_GRAFICOS, "evolucion_temporal.png")
    plt.savefig(ruta, dpi=300)
    plt.close()
    print(f"[OK] Gráfico guardado: {ruta}")


def grafico_boxplot_tr_sujeto(df):
    """
    Genera y guarda un boxplot con la distribución del tiempo de reacción
    por participante, para identificar variabilidad y outliers.

    Parámetros
    ----------
    df : pd.DataFrame
        DataFrame con los datos del experimento.
    """
    df_go = df[(df["estimulo"] == "go") & (df["tiempo_reaccion"] > 0)]

    datos_por_sujeto = [
        grupo["tiempo_reaccion"].values
        for _, grupo in df_go.groupby("id_participante")
    ]
    etiquetas = [f"S{s}" for s in df_go["id_participante"].unique()]

    plt.figure(figsize=(9, 5))
    plt.boxplot(
        datos_por_sujeto,
        tick_labels=etiquetas,
        patch_artist=True,
        boxprops=dict(facecolor="#cbd5e1", color="#0f172a"),
        medianprops=dict(color="#b45309", linewidth=2)
    )
    plt.title(
        "Distribución del Tiempo de Reacción por Participante",
        fontsize=13, fontweight="bold", pad=15
    )
    plt.xlabel("Participante", fontsize=11)
    plt.ylabel("Tiempo de Reacción (ms)", fontsize=11)
    plt.grid(True, linestyle="--", alpha=0.4, axis="y")
    plt.tight_layout()

    ruta = os.path.join(CARPETA_GRAFICOS, "distribucion_por_sujeto.png")
    plt.savefig(ruta, dpi=300)
    plt.close()
    print(f"[OK] Gráfico guardado: {ruta}")



def main():
    """
    Ejecuta el flujo principal del programa:
        1. Carga y valida los datos con las funciones de src/ (lógica anterior)
        2. Convierte los datos a DataFrame de Pandas
        3. Aplica validaciones vectorizadas adicionales (sin bucles)
        4. Calcula métricas agrupadas con groupby
        5. Genera y exporta los 3 gráficos en graficos/
        6. Permite consultar métricas por participante

    Raises
    ------
    ValueError
        Si no se encuentran registros válidos o el ID ingresado no existe.
    """
    try:
        # ── Paso 1: carga y validación con src/ (igual que antes) ────────────
        df = cargar_datos("datos/ReflexLab_mock_data.csv")

     

        # ── Paso 3: validaciones vectorizadas con Pandas (sin bucles) ─────────
        if df.isna().any().any():
            raise ValueError("El DataFrame contiene valores NaN.")

        if (df["tiempo_reaccion"] < 0).any():
            raise ValueError("Se detectaron tiempos de reacción negativos.")

        if not df["estimulo"].isin(["go", "nogo"]).all():
            raise ValueError("Estímulos inválidos detectados.")

        if not df["resultado"].isin(["correcto", "incorrecto"]).all():
            raise ValueError("Resultados inválidos detectados.")

        if not df["condicion"].isin(["alta_go", "balanceada"]).all():
            raise ValueError("Condiciones inválidas detectadas.")

        print("[OK] Validaciones vectorizadas de Pandas superadas.")

        # ── Paso 4: métricas agrupadas con Pandas ─────────────────────────────
        df_go = df[(df["estimulo"] == "go") & (df["tiempo_reaccion"] > 0)]

        tr_por_condicion = df_go.groupby("condicion")["tiempo_reaccion"].mean().round(2)
        tasa_aciertos = (
            df.groupby("id_participante")["resultado"]
            .apply(lambda s: (s == "correcto").mean() * 100)
            .round(2)
        )

        print("\n── Tiempo de Reacción Promedio por Condición ──")
        print(tr_por_condicion.to_string())
        print("\n── Tasa de Aciertos por Participante (%) ──")
        print(tasa_aciertos.to_string())

        # ── Paso 5: generar gráficos ───────────────────────────────────────────
        os.makedirs(CARPETA_GRAFICOS, exist_ok=True)
        grafico_barras_tiempo_reaccion_condicion
        grafico_lineas_tr_sujeto(df)
        grafico_boxplot_tr_sujeto(df)

        # ── Paso 6: consulta por participante (igual que antes) ───────────────
        id_participante = int(input("\nIngrese el id del participante: "))
        datos_participante = filtrar_por_participante(datos, id_participante)

        if len(datos_participante) == 0:
            raise ValueError(f"No existe el participante con ID {id_participante}.")

        promedio = calcular_tiempo_reaccion_promedio(datos_participante)
        tasa_error = calcular_tasa_error(datos_participante)

        print(f"\nParticipante {id_participante}:")
        print(f"  Tiempo de reacción promedio : {promedio:.2f} ms")
        print(f"  Tasa de error               : {tasa_error:.2%}")

    except FileNotFoundError as e:
        print(f"[ERROR CRÍTICO] Tipo de error encontrado: {e} | Ubicación: main")
    except ValueError as e:
        print(f"[ERROR CRÍTICO] Tipo de error encontrado: {e} | Ubicación: main")
    except Exception as e:
        print(f"[ERROR CRÍTICO] Tipo de error encontrado: {e} | Ubicación: main")


if __name__ == "__main__":
    main()


    