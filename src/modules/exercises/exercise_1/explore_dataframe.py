"""
Mòdul auxiliar de l'exercici 1 que permet l'exploració del DataFrame.
"""

import pandas as pd

def explore_dataframe(df: pd.DataFrame) -> None:
    """
    Explora el DataFrame rebut i mostra per pantalla:

    - Les cinc primeres files
    - Les columnes del DataFrame
    - La informació general del DataFrame

    Args:
        df (pd.DataFrame): DataFrame a explorar.

    Returns:
        None
    """

    print("Cinc primeres línies del dataframe:\n")
    print(df.head())
    print("\n")
    print("Columnes del dataframe:\n")
    print(df.columns)
    print("\n")
    print("Informació del dataframe:\n")
    print(df.info())
    print("\n")
