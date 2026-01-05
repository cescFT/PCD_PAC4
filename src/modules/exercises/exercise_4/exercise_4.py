"""
Mòdul que conté el codi de l'exercici 4.

En aquest exercici ens demanen crear una

"""

import pandas as pd

from src.modules.exercises.exercise_4.statistics_functions import analyze_dataset
from src.modules.exercises.exercise_4.statistics_functions import save_statistics

def exercise_4(merged_df: pd.DataFrame):
    json_data = analyze_dataset(merged_df)
    save_statistics(json_data, "src/report/analisi_estadistic.json")
