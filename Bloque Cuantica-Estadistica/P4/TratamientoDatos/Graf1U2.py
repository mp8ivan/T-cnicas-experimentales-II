# -*- coding: utf-8 -*-
import numpy as np
import matplotlib.pyplot as plt
import Herramientas as herr
import os as os
import scipy as sci
"""
Parte A: HG VARIANDO UH
"""

def BuscadorMinimos(data, startIndex = 0, required_width = 0):
    
    yCortado = data[1][startIndex:]
    xCortado = data[0][startIndex:]

    indexMinimos = sci.signal.find_peaks(-yCortado,distance = 120,width = required_width)[0]
    minimos = np.zeros(len(indexMinimos))
    minDiff = np.zeros(len(indexMinimos)-1)
    posMinimos = np.zeros(len(indexMinimos))
    for i in range(len(indexMinimos)):
        posMinimos[i] = xCortado[indexMinimos[i]]
        minimos[i] = yCortado[indexMinimos[i]]
        if i != 0: minDiff[i-1] = posMinimos[i]-posMinimos[i-1]
    return minimos,posMinimos        
plt.close("all")
#%% Llamada a los datos
#%%% Parte 1.1: Determinar delta U1 para distintos U2
pth = "P1/U/"
ListP2U = np.array(os.listdir(pth))
U2_1 = herr.TTD(pth  + ListP2U[0])
U2_15 = herr.TTD(pth  + ListP2U[1])
U2_2 = herr.TTD(pth  + ListP2U[2])

errV = 0.01 # V, error de medida
errMin = 0.01 # V, error de determinacion de minimos (se ha visto con un promedio
              # de cuanto se separan algunos minimos numericos de lo que nosotros determinariamos visualmente)
errDiffMin = (errV + errMin) * 2 # Prop. errores. se suman y se multiplica por dos por restar dos variables con mismo error
errI = 0.01 # nA
#%% Buscando minimos

minU265, posMinU265 = BuscadorMinimos(U2_1, 800, 0) 
minU268, posMinU268 = BuscadorMinimos(U2_15,800, 0)
minU271, posMinU271 = BuscadorMinimos(U2_2, 800, 0) 
 
#%% Graficas
#%%% U265
fig1,ax1 = herr.BasicCanvas(ListP2U[0],"U1 (V)", "I (nA)")
ax1.plot(U2_1[0],U2_1[1])
ax1.scatter(posMinU265,minU265, s= 8, color = "red")
fig1.show()


#%%% U268
fig2,ax2 = herr.BasicCanvas(ListP2U[1],"U1 (V)", "I (nA)")
ax2.plot(U2_15[0],U2_15[1])
ax2.scatter(posMinU268,minU268, s = 8, color = "red")
fig2.show()

#%%% U271
fig3,ax3 = herr.BasicCanvas(ListP2U[2],"U1 (V)", "Intensidad (nA)")
ax3.plot(U2_2[0],U2_2[1])
ax3.scatter(posMinU271,minU271, s = 8, color = "red")
fig3.show()

#%% Calculos numericos

