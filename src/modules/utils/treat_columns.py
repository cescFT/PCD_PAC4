"""

"""

import pandas as pd

def rename_columns(df: pd.DataFrame, old_columns: list, new_columns: list) -> pd.DataFrame:
    """

    :param df:
    :param old_columns:
    :param new_columns:
    :return:
    """

    dict_cols = dict(zip(old_columns, new_columns))
    df = df.rename(columns=dict_cols)

    return df

def delete_columns(df: pd.DataFrame, columns_to_delete: list) -> pd.DataFrame:
    """

    :param df:
    :param columns_to_delete:
    :return:
    """

    return df.drop(columns=columns_to_delete)