#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Jun  1 01:16:29 2026

@author: catalinabellomo
"""
import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import os
import sys

# Agrega src/ al path para poder importar los módulos del proyecto
sys.path.append(os.path.join(os.path.dirname(__file__), "src"))

from carga_datos import cargar_datos
from metricas import calcular_tiempo_reaccion_promedio, calcular_tasa_error

# ─── Configuración de la página ───────────────────────────────────────────────
st.set_page_config(
    page_title="ReflexLab Dashboard",
    page_icon="🧠",
    layout="wide"
)

# ─── Título principal ─────────────────────────────────────────────────────────
st.title("🧠 ReflexLab — Análisis de Datos Go/No-Go")
st.markdown("Cargá el archivo CSV del experimento para visualizar los resultados.")

# ─── Paso 1: Carga dinámica del archivo ───────────────────────────────────────
archivo = st.file_uploader(
    "Arrastrá o seleccioná el archivo CSV del experimento",
    type=["csv"]
)

# Si no se cargó ningún archivo, detiene la ejecución acá
if archivo is None:
    st.info("Esperando archivo CSV...")
    st.stop()

# ─── Paso 2: Validación defensiva ─────────────────────────────────────────────

# Columnas esperadas en el CSV
COLUMNAS = [
    "id_participante", "trial", "estimulo", "tiempo",
    "respuesta", "tiempo_reaccion", "resultado", "condicion"
]

try:
    # Carga el archivo subido directamente en un DataFrame
    df = pd.read_csv(archivo, header=None, names=COLUMNAS)

    # Validación A: sin campos vacíos o NaN
    if df.isna().any().any():
        raise ValueError("El archivo contiene campos vacíos o valores nulos (NaN).")

    # Validación B: sin tiempos de reacción negativos
    if (df["tiempo_reaccion"] < 0).any():
        raise ValueError("Se detectaron tiempos de reacción negativos.")

    # Validación C: estímulos válidos
    if not df["estimulo"].isin(["go", "nogo"]).all():
        raise ValueError("Se detectaron estímulos inválidos. Solo se permite 'go' o 'nogo'.")

    # Validación D: resultados válidos
    if not df["resultado"].isin(["correcto", "incorrecto"]).all():
        raise ValueError("Se detectaron resultados inválidos. Solo se permite 'correcto' o 'incorrecto'.")

    # Validación E: condiciones válidas
    if not df["condicion"].isin(["alta_go", "balanceada"]).all():
        raise ValueError("Se detectaron condiciones inválidas. Solo se permite 'alta_go' o 'balanceada'.")

except ValueError as e:
    # Muestra el error de forma vistosa y bloquea el avance
    st.error(f"❌ Error crítico en los datos: {e}")
    st.stop()

# ─── Archivo válido: continúa el análisis ─────────────────────────────────────
st.success(f"✅ Archivo cargado correctamente: {len(df)} registros, {len(df.columns)} columnas.")

# ─── Paso 3: KPIs ─────────────────────────────────────────────────────────────
st.subheader("📊 Indicadores Clave")

# Filtra solo ensayos go con tiempo de reacción real
df_go = df[(df["estimulo"] == "go") & (df["tiempo_reaccion"] > 0)]

# Calcula métricas generales
tr_promedio_general = round(df_go["tiempo_reaccion"].mean(), 2)
tasa_aciertos_general = round((df["resultado"] == "correcto").mean() * 100, 2)
total_participantes = df["id_participante"].nunique()
total_trials = len(df)

# Muestra las métricas en tarjetas
col1, col2, col3, col4 = st.columns(4)
col1.metric("⏱ TR Promedio (ms)", f"{tr_promedio_general} ms")
col2.metric("✅ Tasa de Aciertos", f"{tasa_aciertos_general}%")
col3.metric("👥 Participantes", total_participantes)
col4.metric("🔢 Total de Trials", total_trials)

# ─── Tabla de métricas por condición ──────────────────────────────────────────
st.subheader("📋 Métricas por Condición Experimental")

tr_por_condicion = df_go.groupby("condicion")["tiempo_reaccion"].mean().round(2)
tasa_por_condicion = (
    df.groupby("condicion")["resultado"]
    .apply(lambda s: round((s == "correcto").mean() * 100, 2))
)
tabla = pd.DataFrame({
    "TR Promedio (ms)": tr_por_condicion,
    "Tasa de Aciertos (%)": tasa_por_condicion
})
st.dataframe(tabla, use_container_width=True)

# ─── Paso 4: Gráficos ─────────────────────────────────────────────────────────
st.subheader("📈 Visualizaciones")

col_izq, col_der = st.columns(2)

# Gráfico 1: Barras — TR promedio por condición
with col_izq:
    st.markdown("**Tiempo de Reacción Promedio por Condición**")
    fig1, ax1 = plt.subplots(figsize=(6, 4))
    tr_por_condicion.plot(
        kind="bar", ax=ax1,
        color=["#1e3a8a", "#b45309"],
        edgecolor="black", alpha=0.85
    )
    ax1.set_xlabel("Condición", fontsize=10)
    ax1.set_ylabel("TR Promedio (ms)", fontsize=10)
    ax1.set_xticklabels(ax1.get_xticklabels(), rotation=0)
    ax1.grid(True, linestyle="--", alpha=0.5, axis="y")
    plt.tight_layout()
    st.pyplot(fig1)
    plt.close()

# Gráfico 2: Líneas — evolución del TR por trial
with col_der:
    st.markdown("**Evolución del TR por Trial y Participante**")
    fig2, ax2 = plt.subplots(figsize=(6, 4))
    for sujeto_id, grupo in df_go.groupby("id_participante"):
        ax2.plot(
            grupo["trial"], grupo["tiempo_reaccion"],
            marker="o", markersize=3, linewidth=1.5,
            label=f"S{sujeto_id}"
        )
    ax2.set_xlabel("Trial", fontsize=10)
    ax2.set_ylabel("TR (ms)", fontsize=10)
    ax2.legend(fontsize=8, loc="upper right")
    ax2.grid(True, linestyle=":", alpha=0.6)
    plt.tight_layout()
    st.pyplot(fig2)
    plt.close()

# Gráfico 3: Boxplot — distribución del TR por participante
st.markdown("**Distribución del TR por Participante**")
fig3, ax3 = plt.subplots(figsize=(9, 4))
datos_por_sujeto = [
    grupo["tiempo_reaccion"].values
    for _, grupo in df_go.groupby("id_participante")
]
etiquetas = [f"S{s}" for s in df_go["id_participante"].unique()]
ax3.boxplot(
    datos_por_sujeto,
    labels=etiquetas,
    patch_artist=True,
    boxprops=dict(facecolor="#cbd5e1", color="#0f172a"),
    medianprops=dict(color="#b45309", linewidth=2)
)
ax3.set_xlabel("Participante", fontsize=10)
ax3.set_ylabel("TR (ms)", fontsize=10)
ax3.grid(True, linestyle="--", alpha=0.4, axis="y")
plt.tight_layout()
st.pyplot(fig3)
plt.close()

# ─── Consulta individual por participante ─────────────────────────────────────
st.subheader("🔍 Consulta por Participante")

ids_disponibles = sorted(df["id_participante"].unique().tolist())
id_seleccionado = st.selectbox("Seleccioná un participante:", ids_disponibles)

df_part = df[df["id_participante"] == id_seleccionado]
registros = df_part.rename(columns={"resultado": "resultado_respuesta"}).to_dict(orient="records")

promedio = calcular_tiempo_reaccion_promedio(registros)
tasa_error = calcular_tasa_error(registros)

c1, c2 = st.columns(2)
c1.metric("⏱ TR Promedio", f"{round(promedio, 2)} ms")
c2.metric("❌ Tasa de Error", f"{round(tasa_error * 100, 2)}%")

