"""
Pràctica 4: Testing, manteniment i desplegament

Autor: Francesc Ferré Tarrés
Assignatura: Programació per a la Ciència de Dades
Any: 2026
"""


import argparse
import src.modules.ex1_package.load_data as load_data


if __name__ == '__main__':
    parser = argparse.ArgumentParser(
        description="Execució dels exercicis de la PAC"
    )

    parser.add_argument(
        "-ex",
        type=int,
        help="Executa els exercicis des del 1 fins al número indicat"
    )

    args = parser.parse_args()

    if args.ex is None:
        print(load_data.patata())
    else:
        limit = args.ex
        print(limit)


