# -*- coding: utf-8 -*-
"""
Parte 1: Determinacion de h y funcion de trabajo
"""

import numpy as np
import matplotlib.pyplot as plt
import Herramientas as herr
import scipy.stats as scis
import os as os

plt.close("all")
#%% Llamada a los datos
pth = "Data/Parte 1/"
todosPuntos = herr.TTD(pth +"todosPuntos.txt")
finalPuntos = herr.TTD(pth + "AjusteFinal.txt")
#%% Ajustes
nu = np.array(finalPuntos[0], dtype = float)
V = np.array(finalPuntos[1], dtype = float)
p, cov = np.polyfit(nu, V, 1, cov = True)
errs = np.sqrt(np.diag(cov))
chi = scis.chisquare(np.polyval(p,nu), V) [1] # Esto es chi cuadrado


#%% Graficas
fig,ax = herr.BasicCanvas("Potecial de frenado para distintas frecuencias", r"$\nu \ (Hz)$", "V (Volts)")
ax.scatter(nu,V,s = 8)
ajusteLabel = r"$V(\nu) =({} \pm {} ) + ({} \pm {}) $".format(round(p[0],17), round(errs[0],17),round(p[1],2), round(errs[1],2))
ax.plot(nu, np.polyval(p, nu), color = "red", linestyle = "dashed", label = ajusteLabel)
ax.plot(nu[0],V[0], label = r"$R^2 = {}$".format(chi))
ax.legend()
fig.show()
