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
        path_file_to_read = "data/taxa_abandonament.xlsx"
        df_abandonment_tax = pd.read_excel(path_file_to_read)
        df_performance_students = df
    else:
        path_file_to_read = "data/rendiment_estudiants.xlsx"
        df_abandonment_tax = df
        df_performance_students = pd.read_excel(path_file_to_read)

    print(f"Carreguem el document {path_file_to_read} perquè ja hem carregat"
          f" el document {df.source_file} en l'anterior exercici.")

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

    print("Columnes del dataframe de la taxa d'abandonament reanomenades:\n")
    print(df_abandonment_tax.columns)
    print("\n")


    # Eliminació de les columnes, d'acord amb l'enunciat.
    cols_to_delete = ["Universitat", "Unitat"]
    df_abandonment_tax = delete_columns(df_abandonment_tax, cols_to_delete)

    print(f"Eliminació de les columnes {cols_to_delete}"
          f" del dataframe d'abandonament escolar\n")

    cols_to_delete.append("Crèdits ordinaris superats")
    cols_to_delete.append("Crèdits ordinaris matriculats")
    df_performance_students = delete_columns(df_performance_students, cols_to_delete)

    print(f"Eliminació de les columnes {cols_to_delete}"
          f" del dataframe de la taxa de rendiment escolar.\n")

    cols = []
    for col in df_abandonment_tax.columns:
        if "Estudi" == col:
            continue

        if col in df_performance_students.columns:
            cols.append(col)

    print(f"Columnes a agrupar: {cols}\n")

    # Agrupació dels dataframes d'acord amb l'enunciat de la pràctica
    df_grouped_abandonment = group_dataframe(
        df_abandonment_tax,
        cols,
        "% Abandonament a primer curs"
    )

    print("Dataframe de la taxa d'abandonament agrupat per les columnes:\n")
    print(df_grouped_abandonment)
    print("\n")

    df_grouped_performance = group_dataframe(
        df_performance_students,
        cols,
        "Taxa rendiment"
    )

    print("Dataframe del rendiment agrupat per les columnes:\n")
    print(df_grouped_performance)
    print("\n")

    # Retornem el dataframe ajuntat d'acord amb l'enunciat de la pràctica
    df_merged = merge_dataframes(df_grouped_abandonment, df_grouped_performance, cols)

    print("Dataframe merged després de tractar les columnes d'acord amb l'enunciat\n")
    print(df_merged)

    return df_merged
