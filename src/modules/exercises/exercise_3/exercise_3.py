"""
Mòdul que conté el codi de l'exercici 3.

Aquest exercici el que demana és generar un gràfic amb dos subplots:

1. Evolució del % d'Abandonament per curs acadèmic.
2. Evolució de la Taxa de Rendiment per curs acadèmic.

Finalment, es desa en el directori corresponent i amb la configuració que es descriu
en l'enunciat.
"""

# Referències:
# * Teoria
# * https://matplotlib.org/stable/gallery/subplots_axes_and_figures/subplots_demo.html
# * https://matplotlib.org/stable/api/_as_gen/matplotlib.pyplot.savefig.html


import os

import pandas as pd
import matplotlib.pyplot as plt

from src.modules.exercises.exercise_3.subplot_create import create_subplot_with_specific_data


def exercise_3(df_grouped: pd.DataFrame) -> None:
    """
    Funció que dona resposta a l'exercici 3. Genera els subplots i tot el que es demana en l'exercici.

    Args:
        df_grouped (pd.DataFrame): dataframe agrupat.

    Returns:
        None.
    """

    # Generem el plot amb dos subplots.
    fig, axes = plt.subplots(nrows=2, ncols=1, figsize=(14, 10), sharex=True)
    study_type = sorted(df_grouped["Branca"].unique())

    # Creem el primer gràfic per a mostrar el percentatge d'abandonament mitjà en el primer curs per curs acadèmic
    # i branca d'estudi.
    ax1 = axes[0]
    result = create_subplot_with_specific_data(
        axes=ax1,
        df_grouped=df_grouped,
        study_factor="% Abandonament a primer curs",
        study_type=study_type,
        title="Evolució del % d'Abandonament mitjà per curs acadèmic i branca",
        y_label="% Abandonament mitjà"
    )
    all_lines = result["all_lines"]
    all_labels = result["all_labels"]

    # Creem el segon gràfic per a mostrar la taxa de rendiment mitjà per curs acadèmic i branca d'estudi.
    ax2 = axes[1]
    create_subplot_with_specific_data(
        axes=ax2,
        df_grouped=df_grouped,
        study_factor="Taxa rendiment",
        study_type=study_type,
        title="Evolució de la Taxa de Rendiment mitjà per curs acadèmic",
        y_label="Taxa rendiment mitjà",
        x_label="Curs Acadèmic"
    )

    # Configuració per a rotar les etiquetes de l'eix X, és a dir, les del curs academic.
    plt.setp(ax2.get_xticklabels(), rotation=45, ha="right")

    # Preparació del layout
    fig.tight_layout(rect=[0, 0.03, 1, 0.92])

    # Pintar una única llegenda per a tots dos subplots.
    fig.legend(
        all_lines,
        all_labels,
        loc='upper center',
        ncol=len(all_labels),
        bbox_to_anchor=(0.5, 0.97),
        frameon=False,
        fontsize=10
    )

    # Desar el gràfic en la carpeta destí i amb el nom que es comenta en l'enunciat de la pràctica.
    os.makedirs("src/img/", exist_ok=True)
    output_file = "src/img/evolucio_francesc_ferre_tarres.png"

    plt.savefig(output_file, dpi=300, bbox_inches='tight')

    print(f"Figura desada correctament a: {output_file}")
