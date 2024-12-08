# -*- coding: utf-8 -*-
import Herramientas as herr
import numpy as np
import matplotlib.pyplot as plt

"""
Analisis de los datos para solo dos polarizadores

20% Calidad tecnica
20% Complicacion del experimento
60% Cuanto profundizas en los experimentos
"""

def PasoAIntensidad(Voltaje):
    R = 10**4
    Amp = 10**2
    return Voltaje/R/Amp *10**6 # Lo devuelve en microAmperios

plt.close("all")
#%% Datos

pth = "Data/Dos/"
Prueba1 = herr.TTD(pth + "P2Intento1.txt")
Prueba2 = herr.TTD(pth + "P2Intento2.txt")

A1 = np.array(Prueba1[0],dtype = float)
V1 = np.array(Prueba1[1], dtype = float)

# Ley de Ohm V = IR --> I = V/R / Amp
errV = 0.01
errI = 0.01 #Suponemos sin error el dispositivo experimental. Asi el cambio es directo
errAlf = 1
errA1 = np.ones(len(A1))

I1 = PasoAIntensidad(V1) # mA (microAmperios)
errI1 = np.ones(len(I1))*0.01 # Suma de errores relativos

A2 = np.array(Prueba2[0], dtype = float)
V2 = np.array(Prueba2[1], dtype = float)

I2 = PasoAIntensidad(V2)# mA
errI2 = np.ones(len(I2))*0.01
errA2 = np.ones(len(A2))

I1SinP = PasoAIntensidad(12.84)
I2SinP = PasoAIntensidad(12.93)

Imax1 = np.max(I1)
Imin1 = np.min(I1)

Imax2 = np.max(I2)
Imin2 = np.min(I2)

I1P =I1/Imax1
I2P = I2/Imax2
#%% Graficos
fig, ax = herr.BasicCanvas("Intento1", r"$\alpha$ (grados)", r"$I\ (\mu A)$")
ax.scatter(A1,I1, s = 8)
ax.errorbar(A1,I1, errI1,errA1, fmt = "none", capsize = 5)
fig.show()

fig2, ax2 = herr.BasicCanvas("Intento2", r"$\alpha$ (grados)", r"$I\ (\mu A)$")
ax2.scatter(A2,I2, s = 8)
ax2.errorbar(A2,I2, errI2,errA2, fmt = "none", capsize = 5)
fig.show()

# Figuras cociente
f3,ax3 = herr.BasicCanvas()