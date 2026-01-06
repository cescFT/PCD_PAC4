"""
Mòdul que conté el codi de l'exercici 4.

En aquest exercici ens demanen crear un JSON amb dades referents al dataframe creat en l'exercici 2.

1. Metadades: Dades bàsiques (data de l'anàlisi, nombre de registres del dataframe i
 el període de cursos que hi ha disponibles en el dataframe.
2. Estadístiques globals: Mètriques que resumeixen el comportament general del sistema
 universitari català, sense diferenciar branques.
 En aquest apartat hi ha l'abandonament mitjà, el rendiment mitjà i la correlació entre
l'abandonament i el rendiment.
3. Anàlisi per branca: Es calculen les mitjanes, mínims, màxims,
 desviacions estàndards de la taxa de rendiment i d'abandonament,
 juntament amb la tendència temporal i els anys amb anomalies
(de moment array buit perq no conec quina és la lògica que té darrera).
4. Rànquings: S'identifica quines branques tenen els millors i pitjors resultats
 de taxa de rendiment i d'abandonament.

"""

import pandas as pd

from src.modules.exercises.exercise_4.statistics_functions import analyze_dataset
from src.modules.exercises.exercise_4.statistics_functions import save_statistics

def exercise_4(merged_df: pd.DataFrame) -> None:
    """
    Funció d'execució de l'exercici 4, la qual crida la funció analyze_dataset
     i desa el json d'acord amb el que està establert en l'enunciat.

    Args:
        merged_df (pd.DataFrame): Dataframe merged amb les dades per a ser analitzades.

    Returns:
        None.
    """

    json_data = analyze_dataset(merged_df)
    save_statistics(json_data, "src/report/analisi_estadistic.json")
