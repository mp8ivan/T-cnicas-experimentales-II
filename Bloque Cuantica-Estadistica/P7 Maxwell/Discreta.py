# -*- coding: utf-8 -*-

import Herramientas as herr
import matplotlib.pyplot as plt
import numpy as np
"""
Ploteo de P(v) discreto
"""
plt.close("all")
Data = herr.TTD("Data.txt")
g = 9.81
y = 80E-3
nComp = np.array(Data[0],dtype = float)
xAsoc = np.array(Data[1],dtype = float)
vAsoc = np.array(Data[2], dtype = float)
nFav = np.array(Data[3], dtype = float)
pV = Data[4]
errV = np.sqrt(g/(2*y)*0.01**2 + 1/4 * g/2*y**3 * 0.01**2)
errpV = 0.05 # De momento. Habria que pensar mejor cuanto error ha aportado el pesado
nT = np.sum(nFav)

fig,ax = herr.BasicCanvas("P(v) discreto","v (m/s)","P(v)")
ax.scatter(vAsoc,pV, s = 8)
ax.errorbar(vAsoc,pV, np.zeros(len(vAsoc)), np.ones(len(vAsoc))*errV, fmt = "none", capsize = 10)
fig.grid()
fig.show()