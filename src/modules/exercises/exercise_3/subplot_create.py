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
        axes (plt.Axes): <- Per aqui.
    """

    all_lines = []
    all_labels = []
    colors = plt.cm.tab10.colors

    for i, branca in enumerate(study_type):
        df_plot = df_grouped[df_grouped['Branca'] == branca]
        df_plot = prepare_data_of_plot(df_plot, study_factor)

        line, = axes.plot(
            df_plot['Curs Acadèmic'],
            df_plot[study_factor],
            marker='o',
            linewidth=2,
            label=branca,
            color=colors[i % len(colors)]
        )

        all_lines.append(line)
        all_labels.append(branca)

    axes.set_title(title, fontsize=14, pad=15)
    axes.set_ylabel(y_label)
    if x_label:
        axes.set_xlabel(x_label)

    axes.grid(True, linestyle='--', alpha=0.7)

    return {
        'all_lines': all_lines,
        'all_labels': all_labels
    }

def prepare_data_of_plot(df_plot: pd.DataFrame, col: str) -> pd.DataFrame:
    """

    :param df_plot:
    :return:
    """
    return df_plot.groupby(['Curs Acadèmic', 'Branca'], as_index=False)[col].mean()
