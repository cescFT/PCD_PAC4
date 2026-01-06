"""
Pràctica 4: Testing, manteniment i desplegament

Autor: Francesc Ferré Tarrés

Assignatura: Programació per a la Ciència de Dades

Data: Gener 2026

"""

import os
import sys
import argparse
import warnings
from src.modules.exercises.exercise_1 import exercise_1
from src.modules.exercises.exercise_2 import exercise_2
from src.modules.exercises.exercise_3 import exercise_3
from src.modules.exercises.exercise_4 import exercise_4

def main() -> None:
    """
    Funció principal sobre la qual s'executa tot el codi.
    Aquesta funció permet passar-li arguments per línia de comanda.
    Les opcions són -h per l'ajuda i -ex pel número d'exercici vàlid
    sobre el qual vols executar, és a dir, si vols executar del l'1 al 3,
    se li pot passar l'exercici 3. Si no se li passa res, ho executa tot.

    Args:
        None.

    Returns:
        None.
    """

    # Ignoro un warning que hi ha en el moment de llegir els excels, de la llibreria openpyxl
    warnings.filterwarnings(
        "ignore",
        message="Cannot parse header or footer",
        category=UserWarning
    )

    parser = argparse.ArgumentParser(
        description="Execució dels exercicis de la PAC 4"
                    " de l'assignatura de Programació per a la Ciència de Dades."
    )

    parser.add_argument(
        "-ex",
        type=int,
        help="Executa els exercicis des del 1 fins al número indicat"
    )

    parser.add_argument(
        "-file",
        type=str,
        help="Llegeix el fitxer que se li passi per paràmetre."
             " Per exemple: data/rendiment_estudiants.xlsx"
    )

    args = parser.parse_args()

    # Llista dels exercicis programats
    exercises = [
        exercise_1.exercise_1,
        exercise_2.exercise_2,
        exercise_3.exercise_3,
        exercise_4.exercise_4
    ]

    # Revisem si tenim l'exercici passat per paràmetre
    # En cas que no se li passi un valor vàlid d'exercici, retornem un 1,
    # tot indicant que el programa no ha acabat bé. Ara bé, si no se li passa l'argument -ex,
    # el límit és la mateixa mida de l'array creada amb els exercicis.
    if args.ex is not None:
        limit = args.ex
        if limit <= 0 or limit > len(exercises):
            print("Proporciona un exercici vàlid (1-4).")
            sys.exit(1)
    else:
        limit = len(exercises)


    # Part del codi on es revisa si se li passa el fitxer com a argument -file.
    # En cas de passar-li el fitxer, es revisa que sigui un string i que el path passat
    # sigui vàlid, és a dir, que sigui un fitxer i que existexi. Si no existeix el fitxer
    # o no és vàlid, pintem per pantalla un missatge i acabem l'execució del programa amb un 1,
    # indicant que el programa no ha acabat bé.
    file_path = ""
    if args.file is not None:
        file_path = args.file

        try:
            file_path = str(file_path)
        except TypeError as t:
            print(
                "Proporciona un string."
                " Per exemple: data/rendiment_estudiants.xlsx. Error:" + str(t)
            )
            sys.exit(1)

        if not os.path.isfile(file_path) or not os.path.exists(file_path):
            print("Proporciona un path vàlid que sigui un fitxer i que existeixi")
            sys.exit(1)

    # Si tot va bé i arribem en aquest punt, executem els exercicis per ordre,
    # atès que són incrementals, perquè el 2n exercici espera el
    # resultat del 1r, i així.
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

        print("Fi execució exercici " + str(i + 1) + "/" + str(limit) + "\n")

    print("Final d'execució.")
    sys.exit(0)

if __name__ == '__main__':
    main()
