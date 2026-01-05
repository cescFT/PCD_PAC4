"""
Mòdul auxiliar que permet ajuntar dataframes
"""

# Referències:
# * Teoria
# * https://pandas.pydata.org/docs/reference/api/pandas.DataFrame.merge.html

import pandas as pd

def merge_dataframes(df_1: pd.DataFrame, df_2: pd.DataFrame, merge_columns: list) -> pd.DataFrame:
    """
    Funció que permet ajuntar dataframes per les columnes que se li passen per paràmetre.
    
    Args:
        df_1 (pd.Dataframe): dataframe 1.
        df_2 (pd.Dataframe): dataframe 2.
        merge_columns (list): Llista de columnes sobre les quals es col fer merge.

    Returns:
        pd.DataFrame: dataframe unit.
    """

    df_merged = pd.merge(
        df_1,
        df_2,
        on=merge_columns,
        how="inner"
    )

    return df_merged
