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
    dataList.append(np.array(herr.TTD(pth +dataNames[i]),dtype = float)) # Se han conseguido en orden de alfa creciente
#%% Ajustes
# Hay que obtener I a partir de la V medida de la corriente




# Hay que obtener los errores
#%% Graficas
plt.rcParams.update({'font.size': 15})
for i in range(6):
    V = dataList[i][0]
    I = dataList[i][1]  # * 10E-9 # Revertimos amplificacion y dividimos por R. Al estar en nanos esta listo
    p, cov = np.polyfit(V, I, 1, cov = True)
    chi = scis.chisquare(np.polyval(p,V), I) [1] # Esto es chi cuadrado
    errs = np.sqrt(np.diag(cov))
    ajusteLabel = r"$I(V) =({} \pm {} ) I + ({} \pm {}) $".format(round(p[0]), round(errs[0]),round(p[1]), round(errs[1]))
    fig,ax = herr.BasicCanvas(dataNames[i][:-4], "V (V)", "I (nA)")
    ax.scatter(dataList[i][0], dataList[i][1], s = 10)
    ax.plot(V, np.polyval(p, V), color = "red", linestyle = "dashed", label = ajusteLabel)
    ax.plot(V[0],I[0], linewidth = 0, label = r"$R^2 = {}$".format(round(chi,5)))
    ax.legend()
    fig.show()