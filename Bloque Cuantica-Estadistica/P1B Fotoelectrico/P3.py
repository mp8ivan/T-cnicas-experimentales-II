# -*- coding: utf-8 -*-
"""
Parte 3: Estudio del filtro en las graficas I-V
"""
import numpy as np
import matplotlib.pyplot as plt
import Herramientas as herr
import scipy.stats as scis
import os as os

plt.close("all")
#%% Llamada a los datos
pth = "Data/Parte 3/"
dataNames = np.array(os.listdir(pth))
dataList = []
for i in range(3):
    dataList.append(np.array(herr.TTD(pth + dataNames[i]),dtype = float)) # Se han conseguido en orden de alfa creciente

#%% Graficas
plt.rcParams.update({'font.size': 15})
for i in range(6):
    V = dataList[i][0]
    I = dataList[i][1]
    p, cov = np.polyfit(V, I, 1, cov = True)
    chi = scis.chisquare(np.polyval(p,V), I) [1] # Esto es chi cuadrado
    errs = np.sqrt(np.diag(cov))
    ajusteLabel = r"$I(V) =({} \pm {} ) I + ({} \pm {}) $".format(round(p[0]), round(errs[0]),round(p[1]), round(errs[1]))
    fig,ax = herr.BasicCanvas(dataNames[i][:-4], "V (V)", "I (nA)")
    ax.scatter(dataList[i][0], dataList[i][1], s = 15)
    #ax.plot(V, np.polyval(p, V), color = "red", linestyle = "dashed", label = ajusteLabel)
    #ax.plot(V[0],I[0], linewidth = 0, label = r"$R^2 = {}$".format(round(chi,5)))
    ax.legend()
    fig.show()