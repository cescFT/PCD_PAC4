"""
Mòdul auxiliar de l'exercici 1 que permet la lectura d'un fitxer.
"""

import pandas as pd

def read_file(file_path: str = "") -> pd.DataFrame:
    """
    Llegeix un fitxer Excel i retorna el seu contingut en un DataFrame.

    Si no es proporciona cap ruta com a paràmetre, es demana a l'usuari
    quin dels fitxers disponibles vol carregar.

    Args:
        file_path (str): Ruta del fitxer a llegir. Opcional.

    Returns:
        pd.DataFrame: DataFrame amb les dades del fitxer llegit.
    """

    basic_rel_path_files = "data/"

    valid_files = {
        1: {
            "path": basic_rel_path_files + "rendiment_estudiants.xlsx",
            "name": "rendiment_estudiants.xlsx"
        },
        2: {
            "path": basic_rel_path_files + "taxa_abandonament.xlsx",
            "name": "taxa_abandonament.xlsx"
        }
    }

    if file_path == "":
        file_to_read_is_valid = False
        file_to_read = None

        while not file_to_read_is_valid:
            text_to_display = "Indica quin dels dos datasets disponibles vols carregar\n\n"

            for key, file_data in valid_files.items():
                text_to_display += str(key) + ": " + file_data["name"] + "\n"

            file_to_read = input(text_to_display)

            try:
                file_to_read = int(file_to_read)
                file_to_read_is_valid = True
            except ValueError:
                print("Proporciona un valor vàlid (1, 2)")

        file_path = valid_files[file_to_read]["path"]

    df = pd.read_excel(file_path)
    return df
