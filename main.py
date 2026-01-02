"""
Pràctica 4: Testing, manteniment i desplegament

Autor: Francesc Ferré Tarrés
Assignatura: Programació per a la Ciència de Dades
Any: 2026
"""

import os
import sys
import argparse
import warnings
from src.modules.exercises import exercise_1
from src.modules.exercises import exercise_2

if __name__ == '__main__':

    warnings.filterwarnings(
        "ignore",
        message="Cannot parse header or footer",
        category=UserWarning
    )

    parser = argparse.ArgumentParser(
        description="Execució dels exercicis de la PAC"
    )

    parser.add_argument(
        "-ex",
        type=int,
        help="Executa els exercicis des del 1 fins al número indicat"
    )

    parser.add_argument(
        "-file",
        type=str,
        help="Llegeix el fitxer que se li passi per paràmetre. Per exemple: data/rendiment_estudiants.xlsx"
    )

    args = parser.parse_args()

    exercises = [
        exercise_1.exercise_1,
        exercise_2.exercise_2,
    ]

    if args.ex:
        limit = args.ex
    else:
        limit = len(exercises)

    file_path = ""
    if args.file:
        file_path = args.file

        try:
            file_path = str(file_path)
        except TypeError as t:
            print("Proporciona un string. Per exemple: data/rendiment_estudiants.xlsx. Error:" + str(t))
            sys.exit(1)

        if not os.path.isfile(file_path) or not os.path.exists(file_path):
            print("Proporciona un path vàlid que sigui un fitxer i que existeixi")
            sys.exit(1)

    for i in range(limit):
        print("Exercici " + str(i + 1) + "/" + str(limit))
        match i:
            case 0:
                df_read = exercises[i](file_path)
            case 1:
                merged_df = exercises[i](df_read)
                print(merged_df)
            case 2:
                pass

        print("Fi execució exercici " + str(i + 1) + "/" + str(limit))