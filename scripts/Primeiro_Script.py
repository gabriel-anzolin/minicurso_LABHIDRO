# -*- coding: utf-8 -*-
"""
---------------------------------------------------------------- first script -------------------------------------------------------------------------------------
Primeiro script no Python

@ author: Gabriel Anzolin, 05/02/2026.

"""

import numpy as np
import matplotlib.pyplot as plt

# Função para gerar um plot de séries temporais
def timeSeriesPlot(arr):
    """
    

    Parameters
    ----------
    arr : np.array
        array numpy com a matriz de dados.

    Returns
    -------
    fig : TYPE
        DESCRIPTION
        
    Exemplo de uso
    fig = timeSeriesPlot(arr)
    
    """
    
    arr_average = np.mean(arr, axis = 1)
    fig, ax = plt.subplots(2)
    ax[0].plot(arr_average)
    ax[1].plot(arr)
       
    fig.savefig("C:\\Users\\gabri\\Documents\\GitHub\\minicurso_LABHIDRO\\figuras\\timeSeriesPlot.png", dpi = 300)
    
    return fig
    