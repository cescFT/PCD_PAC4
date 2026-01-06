"""
Mòdul auxiliar de l'exercici 4 el qual implementa la funció analyze_dataset
 i funcions auxiliars per a poder analitzar el dataframe.
"""

import json
import os
from datetime import datetime

import pandas as pd
import numpy as np
from scipy.stats import linregress, pearsonr


def analyze_dataset(merged_df: pd.DataFrame) -> dict:
    """
    Funció principal d'anàlisi del dataframe, el qual retorna un diccionari per a poder ser desat.

    Args:
        merged_df (pd.DataFrame): Dataframe a analitzat.

    Returns:
        dict: Retorna el diccionari preparat per a ser desat en format JSON.
    """

    json_data = {}

    # Calculem les metadades del JSON a desar
    json_data["metadata"] = calculate_metadata(
        len(merged_df),
        sorted(merged_df["Curs Acadèmic"].unique().tolist()),
    )

    # Calculem les estadístiques globals
    json_data["estadisticas_globales"] = calculate_global_stats(merged_df)

    # Calculem les estadístiques per cada branca d'estudi
    json_data["analisis_por_rama"] = calculate_statistics_per_branch(merged_df)

    # Calculem el ranquing per saber qui té més o menys taxa de rendiment
    # i percentatge d'abandonament
    json_data["ranking_ramas"] = calculate_ranking_by_branch(merged_df)

    return json_data


def calculate_ranking_by_branch(merged_df: pd.DataFrame) -> dict:
    """
    Funció que calcula el rànquing de les branques d'estudi amb una taxa de rendiment
     més alta / baixa, juntament amb el percentatge d'abandonament més alt i
    més baix a primer curs.

    Args:
        merged_df (pd.DataFrame): Dataframe a analitzar.

    Returns:
        dict: Diccionari amb el resultat del rànquing, calculat ordenant el paràmetre d'entrada
         en funció de la taxa de rendiment o el percentatge d'abandonament a primer curs.
    """

    df_ordered_by_tax = merged_df.sort_values(
        by=["Taxa rendiment"],
        ascending=False
    )

    best_performance_tax = df_ordered_by_tax["Branca"].iloc[0]
    worst_performance_tax = df_ordered_by_tax["Branca"].iloc[-1]

    df_ordered_by_abandonment = merged_df.sort_values(
        by=["% Abandonament a primer curs"],
        ascending=False
    )

    best_abandonment = df_ordered_by_abandonment["Branca"].iloc[0]
    wort_abandonment = df_ordered_by_abandonment["Branca"].iloc[-1]

    json_ranking_by_branch = {
        "mejor_rendimiento": [best_performance_tax],
        "peor_rendimiento": [worst_performance_tax],
        "mayor_abandono": [best_abandonment],
        "menor_abandono": [wort_abandonment],
    }

    return json_ranking_by_branch


def calculate_statistics_per_branch(merged_df: pd.DataFrame) -> dict:
    """
    Funció que calcula les estadístiques per branca que es demanen en l'enunciat de la pràctica.

    Args:
        merged_df (pd.DataFrame): Dataframe a analitzar.

    Returns:
        dict: Diccionari amb el resultat de les dades per cada branca d'estudi.
    """

    json_statistics_per_branch = {}
    study_type_branches = sorted(merged_df["Branca"].unique())

    for study_type_branch in study_type_branches:
        branch_data = merged_df[merged_df["Branca"] == study_type_branch]
        mean_abandonment_percentage = format_value(
            branch_data["% Abandonament a primer curs"].mean()
        )

        sd_abandonment_percentage = format_value(
            branch_data["% Abandonament a primer curs"].std()
        )

        min_abandonment_percentage = format_value(
            branch_data["% Abandonament a primer curs"].min()
        )

        max_abandonment_percentage = format_value(
            branch_data["% Abandonament a primer curs"].max()
        )

        mean_tax_performance = format_value(
            branch_data["Taxa rendiment"].mean()
        )

        sd_tax_performance = format_value(
            branch_data["Taxa rendiment"].std()
        )

        min_tax_performance = format_value(
            branch_data["Taxa rendiment"].min()
        )

        max_tax_performance = format_value(
            branch_data["Taxa rendiment"].max()
        )

        tendency_abandonment = calculate_tendency_of_specific_branch(
            branch_data,
            "% Abandonament a primer curs"
        )

        tendency_performance = calculate_tendency_of_specific_branch(
            branch_data,
            "Taxa rendiment"
        )

        json_statistics_per_branch[study_type_branch] = {
            "abandono_medio": mean_abandonment_percentage,
            "abandono_std": sd_abandonment_percentage,
            "abandono_min": min_abandonment_percentage,
            "abandono_max": max_abandonment_percentage,
            "rendimiento_medio": mean_tax_performance,
            "rendimiento_std": sd_tax_performance,
            "rendimiento_min": min_tax_performance,
            "rendimiento_max": max_tax_performance,
            "tendencia_abandono": tendency_abandonment,
            "tendencia_rendimiento": tendency_performance,
            "años_anomalos": []
        }

    return json_statistics_per_branch

def format_value(value: np.float64) -> float:
    """
    Funció auxiliar que passat un float de numpy per paràmetre,
    l'arrodoneix a dos decimals i el passa a float normal.

    Args:
        value (np.float64): Valor a formatar.

    Returns:
        float: Valor en format dos decimals.
    """

    return round(float(value), 2)

def calculate_tendency_of_specific_branch(branch_data: pd.DataFrame, column_to_treat: str) -> str:
    """
    Funció auxiliar que és cridada per totes les branques d'estudi
    la qual permet conèixer la tendència de cada branca.

    Args:
        branch_data (pd.DataFrame): Dataframe amb les dades que tenen a veure amb
         la branca d'estudi específica a analitzar
        column_to_treat (str): Columna del dataframe a ser revisada.

    Returns:
        str: Retorna la tendència de cada branca de estudi en funció del resultat del slope
         de la regressió lineal.
    """

    branch_by_year_abandonment = branch_data.groupby("Curs Acadèmic").agg({
        column_to_treat: "mean"
    }).reset_index()

    years = branch_by_year_abandonment["Curs Acadèmic"].tolist()
    values_abandonment = branch_by_year_abandonment[column_to_treat].tolist()
    slope, _, _, _, _ = linregress(
        range(len(years)),
        values_abandonment
    )

    tendency = "estable"
    if slope < -0.01:
        tendency = "decreixent"
    elif slope > 0.01:
        tendency = "creixent"

    return tendency

def calculate_global_stats(merged_df: pd.DataFrame) -> dict:
    """
    Funció que calcula les estadístiques globals del dataframe a analitzar.

    Args:
        merged_df (pd.DataFrame): Dataframe a analitzar.

    Returns:
        dict: Diccionari amb les dades globals que es demanen en l'enunciat de la pràctica.
    """

    corr, _ = pearsonr(
        merged_df["% Abandonament a primer curs"],
        merged_df["Taxa rendiment"]
    )

    return {
        "abandono_medio": round(float(merged_df["% Abandonament a primer curs"].mean()), 2),
        "rendimiento_medio": round(float(merged_df["Taxa rendiment"].mean()), 2),
        "correlacion_abandono_rendimiento": round(float(corr), 2)
    }


def calculate_metadata(n_elems: int, temporal_period: list) -> dict:
    """
    Funció que calcula les metadades de l'anàlisi del dataframe a analitzar.

    Args:
        n_elems (int): Nombre de files del dataframe a analitzar.
        temporal_period (list): Cursos disponibles en el dataframe a analitzar.

    Returns:
        dict: Diccionari amb les dades que es demanen en l'enunciat de la pràctica
         per a les metadades.
    """

    return {
        "fecha_analisis": datetime.now().strftime("%Y-%m-%d"),
        "num_registros": n_elems,
        "periodo_temporal": temporal_period
    }

def save_statistics(json_data: dict, path: str) -> None:
    """
    Funció que desa les dades del report al path que se li passi per paràmetre.

    Args:
        json_data (dict): Diccionari amb les dades del JSON amb les estadístiques a desar.
        path (str): Path complert on es desarà el JSON.

    Returns:
        None.
    """

    os.makedirs("src/report", exist_ok=True)
    with open(path, "w", encoding="utf-8") as json_file:
        json.dump(json_data, json_file)

    print(f"Fitxer {path} desat correctament.")
