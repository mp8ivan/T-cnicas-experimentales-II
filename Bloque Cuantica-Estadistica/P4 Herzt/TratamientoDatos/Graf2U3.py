# -*- coding: utf-8 -*-
import numpy as np
import matplotlib.pyplot as plt
import Herramientas as herr
import os as os
import scipy as sci
plt.rcParams.update({'font.size': 15})
"""
Parte B: NE. Buscandoi las de U3
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
pth = "P2/U3/"
ListP3U = np.array(os.listdir(pth))
U3_25 = herr.TTD(pth  + ListP3U[0])
U3_28 = herr.TTD(pth  + ListP3U[1])
U3_31 = herr.TTD(pth  + ListP3U[2])
U3_34 = herr.TTD(pth  + ListP3U[3])

#%% Suavizando 
window_length = 15 # Potencia del suavizado (cuanto se va a asemejar al polinomio)
polyorder = 1
U3_25[1] = herr.suavizar_savgol(U3_25[1], window_length, polyorder)
U3_28[1] = herr.suavizar_savgol(U3_28[1], window_length, polyorder)
U3_31[1] = herr.suavizar_savgol(U3_31[1], window_length, polyorder)
U3_34[1] = herr.suavizar_savgol(U3_34[1], window_length, polyorder)
#%% Buscando minimos

minU265, posMinU265 = BuscadorMinimos(U3_25, 750, 0) 
minU268, posMinU268 = BuscadorMinimos(U3_28, 750, 0)
minU271, posMinU271 = BuscadorMinimos(U3_31, 600, 0) 
minU274, posMinU274 = BuscadorMinimos(U3_34, 600, 0)
 
#%% Graficas
#%%% U265
fig1,ax1 = herr.BasicCanvas(ListP3U[0],"U1 (V)", "I (nA)")
ax1.plot(U3_25[0],U3_25[1])
ax1.scatter(posMinU265,minU265,s = 8, c = "red")
fig1.show()


#%%% U268
fig2,ax2 = herr.BasicCanvas(ListP3U[1],"U1 (V)", "I (nA)")
ax2.plot(U3_28[0],U3_28[1])
ax2.scatter(posMinU268,minU268,s = 8, c = "red")
fig2.show()

#%%% U271
fig3,ax3 = herr.BasicCanvas(ListP3U[2],"U1 (V)", "Intensidad (nA)")
ax3.plot(U3_31[0],U3_31[1])
ax3.scatter(posMinU271,minU271,s = 8, c = "red")
fig3.show()

#%%% U268
fig4,ax4 = herr.BasicCanvas(ListP3U[3],"U1 (V)", "Intensidad (nA)")
ax4.plot(U3_34[0],U3_34[1])
ax4.scatter(posMinU274,minU274,s = 8, c = "red")
fig4.show()
#%% Calculos numericos

