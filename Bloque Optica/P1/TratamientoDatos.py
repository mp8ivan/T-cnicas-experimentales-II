# -*- coding: utf-8 -*-
"""
Calculo errores P1
"""
import numpy as np
import matplotlib.pyplot as plt
import os as os
import Herramientas as herr

plt.close("all")
"""
Parte A: Determinacion del indice de refraccion de una lamina
"""
dList = np.array([5.82,5.83,5.82])
errD = 0.01 # mm

dRelList = np.array([3.94,3.97,3.95]) 
errDRel = 0.01 # mm

relD = errD/dList
relDrel = errDRel / dRelList

n = np.array([1.48,1.47,1.47])
errN = n * (relD + relDrel)


"""
Parte B
"""
# Coloco el directorio donde esta el script
abspath = os.path.abspath(__file__)
dname = os.path.dirname(abspath)
os.chdir(dname)

data = herr.TTD("Prisma/data.txt")
epsi = data[0]
delta = data[1]

fig,ax = herr.BasicCanvas(r"Angulo de desviación($\delta$) respecto al incidente ($\epsilon$)", r"$\epsilon$ (grados)", r"$\delta$ (grados)")

ax.errorbar(epsi,delta,np.ones(len(epsi)) * 0.5, np.ones(len(epsi)) * 0.5, fmt = "o", color = "black", elinewidth = 0.7, capsize = 3)
fig.show()

deltaMin = np.min(delta)
deltaMin = deltaMin * np.pi/180 # Radianes
errDeltaMin = 0.5 * np.pi/180
alpha = 60 * np.pi/180

errNb = 1/2 * 1/np.sin(alpha/2)*np.cos((deltaMin + alpha)/2)*errDeltaMin
nB = np.sin((deltaMin + alpha)/2)/np.sin(alpha/2)
print("Indice de refraccion:", nB, "+-", errNb)
