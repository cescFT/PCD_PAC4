"""
Mòdul auxiliar de l'exercici 2 per tractar les columnes del dataframe.
"""

# Referències
# * Teoria
# * https://www.w3schools.com/python/ref_func_zip.asp

import pandas as pd

def rename_columns(df: pd.DataFrame, old_columns: list, new_columns: list) -> pd.DataFrame:
    """
    Funció que permet renombrar les columnes antigues per columnes noves.

    Args:
        df (pd.DataFrame): dataframe que es vol reanomenar les columnes
        old_columns (list): Llista de les columnes velles
        new_columns (list): Llista de les columnes noves

    Returns:
        pd.DataFrame: Dataframe amb les columnes noves.
    """

    dict_cols = dict(zip(old_columns, new_columns))
    df = df.rename(columns=dict_cols)

    return df

def delete_columns(df: pd.DataFrame, columns_to_delete: list) -> pd.DataFrame:
    """
    Funció que permet eliminar les columnes del dataframe.

    Args:
        df (pd.DataFrame): dataframe que es vol eliminar les columnes
        columns_to_delete (list): Llista de columnes a eliminar

    Returns:
        pd.DataFrame: Dataframe amb les columnes eliminades.
    """

    return df.drop(columns=columns_to_delete)

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
