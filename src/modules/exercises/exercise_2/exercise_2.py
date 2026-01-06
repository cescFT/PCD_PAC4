"""
Mòdul que conté la funció que executa l'exercici 2.

L'exercici consisteix en:

1. Reanomenar les columnes del dataset taxa_abandonament.xlsx perquè coincideixi amb el dataset
 rediment_estudiants.xlsx
2. Eliminació de les columnes "Universitat" i "Unitat" dels dos dataframes i
 "Crèdits ordinaris superats" i "Crèdits ordinaris matriculats" en el cas del dataset de rendiment.
3. Crear i aplicat als datasets una funció per a agrupar totes les files que comparteixen
 les mateixes característiques, i una columna que tigui el rendiment mitjà i la taxa mitjana.
4. Creació d'una funció per per tal de fusionar ambdos datasets.
"""

import pandas as pd
from src.modules.exercises.exercise_2.treat_columns import rename_columns
from src.modules.exercises.exercise_2.treat_columns import delete_columns
from src.modules.exercises.exercise_2.treat_columns import group_dataframe
from src.modules.exercises.exercise_2.merge_dataframes import merge_dataframes

def exercise_2(df: pd.DataFrame) -> pd.DataFrame:
    """
    Funció d'execució de l'exercici 2.

    Args:
        df (pd.DataFrame): Dataframe d'entrada llegit per l'usuari

    Returns:
        pd.DataFrame: Dataframe unit d'acord amb l'enunciat de l'exercici 2
    """

    # En aquest snippet de codi el que fem és llegir el document contrari que ha escollit l'usuari
    # per a poder fer el merge final.
    if "rendiment_estudiants.xlsx" in df.source_file:
        df_abandonment_tax = pd.read_excel("data/taxa_abandonament.xlsx")
        df_performance_students = df
    else:
        df_abandonment_tax = df
        df_performance_students = pd.read_excel("data/rendiment_estudiants.xlsx")

    # Renombrar les columnes d'acord amb el que s'estableix a l'enunciat
    old_columns = df_abandonment_tax.columns.tolist()
    new_columns = [
        "Curs Acadèmic",
        "Tipus universitat",
        "Universitat",
        "Sigles",
        "Unitat",
        "Tipus Estudi",
        "Branca",
        "Estudi",
        "Sexe",
        "Integrat S/N",
        "% Abandonament a primer curs"
    ]

    df_abandonment_tax = rename_columns(
        df_abandonment_tax,
        old_columns,
        new_columns
    )

    # Eliminació de les columnes, d'acord amb l'enunciat.
    cols_to_delete = ["Universitat", "Unitat"]
    df_abandonment_tax = delete_columns(df_abandonment_tax, cols_to_delete)

    cols_to_delete.append("Crèdits ordinaris superats")
    cols_to_delete.append("Crèdits ordinaris matriculats")
    df_performance_students = delete_columns(df_performance_students, cols_to_delete)

    cols = []
    for col in df_abandonment_tax.columns:
        if "Estudi" == col:
            continue

        if col in df_performance_students.columns:
            cols.append(col)

    # Agrupació dels dataframes d'acord amb l'enunciat de la pràctica
    df_grouped_abandonment = group_dataframe(
        df_abandonment_tax,
        cols,
        "% Abandonament a primer curs"
    )

    df_grouped_performance = group_dataframe(
        df_performance_students,
        cols,
        "Taxa rendiment"
    )

    # Retornem el dataframe ajuntat d'acord amb l'enunciat de la pràctica
    df_merged = merge_dataframes(df_grouped_abandonment, df_grouped_performance, cols)

    print("Dataframe merged després de tractar les columnes d'acord amb l'enunciat\n")
    print(df_merged)

    return df_merged
