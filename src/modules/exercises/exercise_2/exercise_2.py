"""
Mòdul que conté la funció que executa l'exercici 2.

L'exercici consisteix en:

1. Reanomenar les columnes del dataset taxa_abandonament.xlsx perquè coincideixi amb el dataset rediment_estudiants.xlsx
2. Eliminació de les columnes "Universitat" i "Unitat" dels dos dataframes i "Crèdits ordinaris superats" i "Crèdits ordinaris matriculats" en el cas del dataset de rendiment.
3. Cr
"""

import pandas as pd
from src.modules.exercises.exercise_2.treat_columns import rename_columns
from src.modules.exercises.exercise_2.treat_columns import delete_columns
from src.modules.exercises.exercise_2.merge_dataframes import merge_dataframes

def exercise_2(df: pd.DataFrame) -> pd.DataFrame:
    """

    :param df:
    :return:
    """

    # 2.1
    if "rendiment_estudiants.xlsx" in df.source_file:
        df_abandonment_tax = pd.read_excel("data/taxa_abandonament.xlsx")
        df_performance_students = df
    else:
        df_abandonment_tax = df
        df_performance_students = pd.read_excel("data/rendiment_estudiants.xlsx")


    old_columns = df_abandonment_tax.columns.tolist()
    new_columns = [
        'Curs Acadèmic',
        'Tipus universitat',
        'Universitat',
        'Sigles',
        'Unitat',
        'Tipus Estudi',
        'Branca',
        'Estudi',
        'Sexe',
        'Integrat S/N',
        '% Abandonament a primer curs'
    ]

    df_abandonment_tax = rename_columns(
        df_abandonment_tax,
        old_columns,
        new_columns
    )

    #2.2. Eliminar les columnes de "Universitat", "Unitat" en ambdós dataframes, i també "Crèdits ordinaris superats" i "Crèdits ordinaris matriculats" en el cas del dataset de rendiment.
    cols_to_delete = ['Universitat', 'Unitat']
    df_abandonment_tax = delete_columns(df_abandonment_tax, cols_to_delete)

    cols_to_delete.append('Crèdits ordinaris superats')
    cols_to_delete.append('Crèdits ordinaris matriculats')
    df_performance_students = delete_columns(df_performance_students, cols_to_delete)

    # 2.3

    print("cols abandonment: {}".format(df_abandonment_tax.columns.tolist()))
    print("cols performance: {}".format(df_performance_students.columns.tolist()))

    cols = []
    for col in df_abandonment_tax.columns:
        if "Estudi" == col:
            continue

        if col in df_performance_students.columns:
            cols.append(col)

    df_grouped_abandonment = group_dataframe(df_abandonment_tax, cols, '% Abandonament a primer curs')
    df_grouped_performance = group_dataframe(df_performance_students, cols, 'Taxa rendiment')

    # 2.4.

    return merge_dataframes(df_grouped_abandonment, df_grouped_performance, cols)


def group_dataframe(df: pd.DataFrame, group_cols:list, value_column: str) -> pd.DataFrame:
    """
    Agrupa el dataframe per les columnes indicades i calcula
    la mitjana de la columna especificada.

    Args:
        df (pd.DataFrame): Dataframe d'entrada
        group_cols (list): Lista de columnes que volem usar per a agrupar
        value_column (str): Columna numèrica a agregar

    Returns:
        pd.DataFrame: Dataframe agregat
    """

    df_grouped = (
        df
        .groupby(group_cols, as_index=False)[value_column]
        .mean()
    )

    return df_grouped
