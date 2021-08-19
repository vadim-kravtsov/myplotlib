import matplotlib as mpl

import matplotlib.colors as colors
import matplotlib.cm as cmx
import matplotlib.pyplot as plt


from matplotlib.ticker import FormatStrFormatter
from matplotlib.ticker import (MultipleLocator, FormatStrFormatter,
                               AutoMinorLocator)

from matplotlib.gridspec import GridSpec

# default parameters are listed below

tickwidth = 1.5

def makefigure(n_rows=1, n_cols=1, figsize=(7, 7), sharex=False):
    fig, axes = plt.subplots(n_rows, n_cols, figsize=figsize, sharex=sharex)

    if n_rows == n_cols == 1:
        axes.xaxis.set_minor_locator(AutoMinorLocator())
        axes.yaxis.set_minor_locator(AutoMinorLocator())
        axes.tick_params(which='major', length=5, width=tickwidth)
        axes.tick_params(which='minor', length=2.5, width=tickwidth)
    elif n_rows == 1 or n_cols == 1:
        for ax in axes:
            ax.xaxis.set_minor_locator(AutoMinorLocator())
            ax.yaxis.set_minor_locator(AutoMinorLocator())
            ax.tick_params(which='major', length=5, width=tickwidth)
            ax.tick_params(which='minor', length=2.5, width=tickwidth)
    else:
        for i in range(n_rows):
            for j in range(n_cols):
                ax = axes[i][j]
                ax.xaxis.set_minor_locator(AutoMinorLocator())
                ax.yaxis.set_minor_locator(AutoMinorLocator())
                ax.tick_params(which='major', length=5, width=tickwidth)
                ax.tick_params(which='minor', length=2.5, width=tickwidth)
    return fig, axes

