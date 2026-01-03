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
from src.modules.exercises.exercise_1 import exercise_1
from src.modules.exercises.exercise_2 import exercise_2
from src.modules.exercises.exercise_3 import exercise_3
from src.modules.exercises.exercise_4 import exercise_4

def main():
    warnings.filterwarnings(
        "ignore",
        message="Cannot parse header or footer",
        category=UserWarning
    )

    parser = argparse.ArgumentParser(
        description="Execució dels exercicis de la PAC 4 de l'assignatura de Programació per a la Ciència de Dades."
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
        exercise_3.exercise_3,
        exercise_4.exercise_4
    ]

    if args.ex is not None:
        limit = args.ex
        if limit <= 0 or limit > len(exercises):
            print("Proporciona un exercici vàlid (1-4).")
            sys.exit(1)
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
            case 2:
                exercises[i](merged_df)
            case 3:
                exercises[i](merged_df)

        print("Fi execució exercici " + str(i + 1) + "/" + str(limit))

    print("Final d'execució.")

if __name__ == '__main__':
    main()