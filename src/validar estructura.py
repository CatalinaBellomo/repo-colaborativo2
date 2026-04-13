#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Apr 13 13:07:18 2026

@author: matildaivancich
"""


def validar_estructura(df):
    if df.empty:
        raise TypeError("ERROR, el archivo está vacío")

    if df.shape[1] != 8:
        raise TypeError("ERROR, el archivo no tiene 8 columnas")
