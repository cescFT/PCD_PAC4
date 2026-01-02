"""

"""

import pandas as pd

def merge_dataframes(df_1: pd.DataFrame, df_2: pd.DataFrame, merge_columns: list) -> pd.DataFrame:
    """

    :param df_1:
    :param df_2:
    :param merge_columns:
    :return:
    """

    df_merged = pd.merge(
        df_1,
        df_2,
        on=merge_columns,
        how='inner'
    )

    return df_merged