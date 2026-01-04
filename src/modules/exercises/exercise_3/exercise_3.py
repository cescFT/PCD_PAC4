"""
Mòdul que conté el codi de l'exercici 3.
"""

# Referències:
# * Teoria
# * https://matplotlib.org/stable/gallery/subplots_axes_and_figures/subplots_demo.html
# * https://matplotlib.org/stable/api/_as_gen/matplotlib.pyplot.savefig.html


import pandas as pd
import matplotlib.pyplot as plt
import os
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
    study_type = sorted(df_grouped['Branca'].unique())

    # Creem el primer gràfic per a mostrar el percentatge d'abandonament mitjà en el primer curs per curs acadèmic
    # i branca d'estudi.
    ax1 = axes[0]
    result = create_subplot_with_specific_data(
        ax1,
        df_grouped,
        '% Abandonament a primer curs',
        study_type,
        "Evolució del % d'Abandonament mitjà per curs acadèmic i branca",
        "% Abandonament mitjà"
    )
    all_lines = result['all_lines']
    all_labels = result['all_labels']

    ax2 = axes[1]
    create_subplot_with_specific_data(
        ax2,
        df_grouped,
        'Taxa rendiment',
        study_type,
        "Evolució de la Taxa de Rendiment mitjà per curs acadèmic",
        "Taxa rendiment mitjà",
        "Curs Acadèmic"
    )

    plt.setp(ax2.get_xticklabels(), rotation=45, ha='right')

    fig.tight_layout(rect=[0, 0.03, 1, 0.92]) 
    
    fig.legend(
        all_lines, 
        all_labels, 
        loc='upper center', 
        ncol=len(all_labels), 
        bbox_to_anchor=(0.5, 0.97),
        frameon=False,
        fontsize=10
    )

    os.makedirs('src/img/', exist_ok=True)
    output_file = 'src/img/evolucio_francesc_ferre_tarres.png'
    
    plt.savefig(output_file, dpi=300, bbox_inches='tight')

    print('Figura desada correctament a: {}'.format(output_file))
