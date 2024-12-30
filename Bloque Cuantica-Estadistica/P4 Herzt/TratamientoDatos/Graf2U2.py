# -*- coding: utf-8 -*-
import numpy as np
import matplotlib.pyplot as plt
import Herramientas as herr
import os as os
import scipy as sci
plt.rcParams.update({'font.size': 15})
"""
Parte B: NE
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
pth = "P2/U2/"
ListP2U = np.array(os.listdir(pth))
U2_65 = herr.TTD(pth  + ListP2U[0])
U2_68 = herr.TTD(pth  + ListP2U[1])
U2_71 = herr.TTD(pth  + ListP2U[2])
U2_74 = herr.TTD(pth  + ListP2U[3])

#%% Buscando minimos
#%%% Suavizando las graficas

window_length = 15 # Potencia del suavizado (cuanto se va a asemejar al polinomio)
polyorder = 1
U2_65[1] = herr.suavizar_savgol(U2_65[1], window_length, polyorder)
U2_68[1] = herr.suavizar_savgol(U2_68[1], window_length, polyorder)
U2_71[1] = herr.suavizar_savgol(U2_71[1], window_length, polyorder)
U2_74[1] = herr.suavizar_savgol(U2_74[1], window_length, polyorder)

#%%% Calculo de minimos
minU265, posMinU265 = BuscadorMinimos(U2_65, 600, 0) 
minU268, posMinU268 = BuscadorMinimos(U2_68, 600, 0)
minU271, posMinU271 = BuscadorMinimos(U2_71, 600, 0) 
minU274, posMinU274 = BuscadorMinimos(U2_74, 600, 0)
 
#%% Graficas
#%%% U265
fig1,ax1 = herr.BasicCanvas(ListP2U[0],"U1 (V)", "I (nA)")
ax1.plot(U2_65[0],U2_65[1])
ax1.scatter(posMinU265,minU265, s = 15, c = "red")
fig1.show()


#%%% U268
fig2,ax2 = herr.BasicCanvas(ListP2U[1],"U1 (V)", "I (nA)")
ax2.plot(U2_68[0],U2_68[1])
ax2.scatter(posMinU268,minU268,s = 15, c = "red")
fig2.show()

#%%% U271
fig3,ax3 = herr.BasicCanvas(ListP2U[2],"U1 (V)", "Intensidad (nA)")
ax3.plot(U2_71[0],U2_71[1])
ax3.scatter(posMinU271,minU271,s = 15, c = "red")
fig3.show()

#%%% U268
fig4,ax4 = herr.BasicCanvas(ListP2U[3],"U1 (V)", "Intensidad (nA)")
ax4.plot(U2_74[0],U2_74[1])
ax4.scatter(posMinU274,minU274,s = 15, c = "red")
fig4.show()
#%% Calculos numericos

