"""
Mòdul auxiliar de l'exercici 3 el qual permet crear subplots.
"""

# Referències:
# * https://matplotlib.org/stable/api/_as_gen/matplotlib.axes.Axes.plot.html
# * https://matplotlib.org/stable/api/_as_gen/matplotlib.axes.Axes.grid.html

import matplotlib.pyplot as plt
import pandas as pd

def create_subplot_with_specific_data(
        axes: plt.Axes,
        df_grouped: pd.DataFrame,
        study_factor: str,
        study_type: list,
        title: str,
        y_label: str,
        x_label: str = ""
) -> dict:
    """
    Funció que permet crear un subplot a través dels paràmetres necessaris per a dur-ho a terme.

    Args:
        axes (plt.Axes): Axes on ha de pintar-se el subplot.
        df_grouped (DataFrame): Dataframe agrupat amb les dades.
        study_factor (str): Factor d'estudi del dataframe, és a dir, la columna a representar.
        study_type (list): Llistat dels tipus d'estudi disponibles.
        title (str): Títol del subplot.
        y_label (str): Etiqueta de l'eix Y del subplot
        x_label (str): Etiqueta de l'eix X del subplot

    Returns:
        dict: {"all_lines": list,"all_labels": list}

    """

    all_lines = []
    all_labels = []
    colors = plt.get_cmap("tab10").colors

    # Per a tots els tipus d'estudi, agafem les dades de la branca d'estudi, les agrupem i les pintem en el gràfic
    # amb un color específic per cada tipus d'estudi, on cada punt apareix amb una rodona i amb un gruix de 2 per la
    # línia representada en el gràfic.
    for i, branca in enumerate(study_type):
        df_plot = df_grouped[df_grouped["Branca"] == branca]
        df_plot = prepare_data_of_plot(df_plot, study_factor)

        line, = axes.plot(
            df_plot["Curs Acadèmic"],
            df_plot[study_factor],
            marker='o',
            linewidth=2,
            label=branca,
            color=colors[i % len(colors)]
        )

        all_lines.append(line)
        all_labels.append(branca)

    # Configurem el títol i les etiquetes dels gràfics en l'eix X i Y
    axes.set_title(title, fontsize=14, pad=15)
    axes.set_ylabel(y_label)
    if x_label:
        axes.set_xlabel(x_label)

    # Activem el grid per millorar la lectura del gràfic.
    axes.grid(True, linestyle='--', alpha=0.7)

    return {
        "all_lines": all_lines,
        "all_labels": all_labels
    }

def prepare_data_of_plot(df_plot: pd.DataFrame, col: str) -> pd.DataFrame:
    """
    Funció que prepara les dades pel subplot.

    Args:
        df_plot (DataFrame): Dataframe amb les dades llest per a ser tractat i posteriorment pintat al subplot.
        col (str): Columna del dataframe a ser pintada sobre la qual es fa la mitjana (punt del gràfic).

    Returns:
        pd.Dataframe: Dataframe preparat per a ser representat en el subplot.
    """

    return df_plot.groupby(["Curs Acadèmic", "Branca"], as_index=False)[col].mean()
