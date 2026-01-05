"""

"""

import os
import json
import pandas as pd
from datetime import datetime
from scipy.stats import pearsonr
from scipy.stats import linregress

def analyze_dataset(merged_df: pd.DataFrame) -> dict:
    """

    :param merged_df:
    :return:
    """

    json_data = {}

    json_data["metadata"] = calculate_metadata(
        len(merged_df),
        sorted(merged_df["Curs Acadèmic"].unique().tolist()),
    )

    json_data["estadisticas_globales"] = calculate_global_stats(merged_df)

    json_data["analisis_por_rama"] = calculate_statistics_per_branch(merged_df)

    json_data["ranking_ramas"] = calculate_ranking_by_branch(merged_df)

    return json_data


def calculate_ranking_by_branch(merged_df: pd.DataFrame) -> dict:
    """

    :param merged_df:
    :return:
    """

    df_ordered_by_tax = merged_df.sort_values(by=["Taxa rendiment"], ascending=False)
    print(df_ordered_by_tax)
    best_performance_tax = df_ordered_by_tax["Branca"].iloc[0]
    worst_performance_tax = df_ordered_by_tax["Branca"].iloc[-1]

    df_ordered_by_abandonment = merged_df.sort_values(by=["% Abandonament a primer curs"], ascending=False)
    print(df_ordered_by_abandonment)
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

    :param merged_df:
    :return:
    """

    json_statistics_per_branch = {}
    study_type_branches = sorted(merged_df["Branca"].unique())

    for study_type_branch in study_type_branches:
        branch_data = merged_df[merged_df["Branca"] == study_type_branch]
        mean_abandonment_percentage = round(float(branch_data["% Abandonament a primer curs"].mean()), 2)
        sd_abandonment_percentage = round(float(branch_data["% Abandonament a primer curs"].std()), 2)
        min_abandonment_percentage = round(float(branch_data["% Abandonament a primer curs"].min()), 2)
        max_abandonment_percentage = round(float(branch_data["% Abandonament a primer curs"].max()), 2)
        mean_tax_performance = round(float(branch_data["Taxa rendiment"].mean()), 2)
        sd_tax_performance = round(float(branch_data["Taxa rendiment"].std()), 2)
        min_tax_performance = round(float(branch_data["Taxa rendiment"].min()), 2)
        max_tax_performance = round(float(branch_data["Taxa rendiment"].max()), 2)

        print(type(branch_data))
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

def calculate_tendency_of_specific_branch(branch_data: pd.DataFrame, column_to_treat: str) -> str:
    """

    :param branch_data:
    :param column_to_treat:
    :return:
    """

    branch_by_year_abandonment = branch_data.groupby("Curs Acadèmic").agg({
        column_to_treat: "mean"
    }).reset_index()

    years = branch_by_year_abandonment["Curs Acadèmic"].tolist()
    values_abandonment = branch_by_year_abandonment[column_to_treat].tolist()
    slope, intercept, r_value, p_value, std_err = linregress(
        range(len(years)),
        values_abandonment
    )

    tendency_abandonment = "estable"
    if slope < -0.01:
        tendency_abandonment = "decreixent"
    elif slope > 0.01:
        tendency_abandonment = "creixent"

    return tendency_abandonment

def calculate_global_stats(merged_df: pd.DataFrame):
    """

    :param merged_df:
    :return:
    """

    corr, p_value = pearsonr(
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

    :param n_elems:
    :param temporal_period:
    :return:
    """

    return {
        "fecha_analisis": datetime.now().strftime("%Y-%m-%d"),
        "num_registros": n_elems,
        "periodo_temporal": temporal_period
    }

def save_statistics(json_data: dict, path: str) -> None:
    """

    :param json_data:
    :param path:
    :return:
    """

    os.makedirs("src/report", exist_ok=True)
    with open(path, "w") as json_file:
        json.dump(json_data, json_file)

    print("Fitxer {} desat correctament.".format(path))