"""
Mòdul que conté la funció que executa l'exercici 1.

L'exercici consisteix en:

1. Lectura d'un fitxer a través de la ruta de l'arxiu (opcional). Si se li passa
   com a argument, llegeix el fitxer indicat.
2. Si no es passa cap ruta, es demana a l'usuari quin fitxer vol llegir.
3. Exploració del DataFrame mostrant informació bàsica.
"""

import pandas as pd
from src.modules.utils.read_file import read_file
from src.modules.utils.explore_dataframe import explore_dataframe

def exercise_1(file_path: str = "") -> dict:
    """
    Executa l'exercici 1.

    Llegeix un fitxer Excel i en mostra informació bàsica mitjançant
    les funcions auxiliars del projecte.

    Args:
        file_path (str): Ruta del fitxer a llegir (opcional).

    Returns:
        pd.DataFrame: DataFrame carregat a partir del fitxer.
    """

    df = read_file(file_path)

    explore_dataframe(df)

    return df
