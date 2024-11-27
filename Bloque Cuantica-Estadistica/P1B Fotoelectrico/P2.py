"""
Parte 2: Estudio de la intensidad respecto al potencial inducido
"""

import numpy as np
import matplotlib.pyplot as plt
import Herramientas as herr
import scipy.stats as scis
import os as os

plt.close("all")
#%% Llamada a los datos
pth = "Data/Parte 2/"
dataNames = np.array(os.listdir(pth))
dataList = []
for i in range(6):
    dataList.append(herr.TTD(pth +dataNames[i])) # Se han conseguido en orden de alfa creciente
#%% Ajustes
# Hay que obtener I a partir de la V medida de la corriente
"""
nu = np.array(finalPuntos[0], dtype = float)
V = np.array(finalPuntos[1], dtype = float)
p, cov = np.polyfit(nu, V, 1, cov = True)
errs = np.sqrt(np.diag(cov))
chi = scis.chisquare(np.polyval(p,nu), V) [1] # Esto es chi cuadrado
"""
# Hay que obtener los errores
#%% Graficas
for i in range(6):
    fig,ax = herr.BasicCanvas(dataNames[i], "V (V)", "I (nA)")
    ax.scatter(dataList[i][0], dataList[i][1], s = 8)
    fig.show()