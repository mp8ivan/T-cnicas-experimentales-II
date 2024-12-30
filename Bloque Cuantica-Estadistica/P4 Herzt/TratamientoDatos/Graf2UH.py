# -*- coding: utf-8 -*-
import numpy as np
import matplotlib.pyplot as plt
import Herramientas as herr
import os as os
import scipy as sci
plt.rcParams.update({'font.size': 15})
"""
Parte B: NE. Buscando las de U3
"""
     
plt.close("all")

#%% Llamada a los datos
#%%% Parte 1.1: Determinar delta U1 para distintos U2
pth = "P2/UH/"
ListP3U = np.array(os.listdir(pth))
UH6 = herr.TTD(pth  + ListP3U[0])
UH7 = herr.TTD(pth  + ListP3U[1])

#%% Suavizando
window_length = 35 # Potencia del suavizado (cuanto se va a asemejar al polinomio)
polyorder = 1
UH6[1] = herr.suavizar_savgol(UH6[1], window_length, polyorder)
UH7[1] = herr.suavizar_savgol(UH7[1], window_length, polyorder)
#%% Buscando minimos

minU265, posMinU265, diffUH6 = herr.BuscadorMinimos(UH6, 600, minimun_height=(-49,-0.2)) 
minU268, posMinU268, diffUH7 = herr.BuscadorMinimos(UH7, 600, minimun_height=(-49,-0.2))

# Concretamente obtenemos la diff de minimos en UH6
diffMin = np.zeros(len(posMinU265))
for i in range (1,len(posMinU265)):
    diffMin[i] = posMinU265[i] - posMinU265[i-1]
#%% Graficas
#%%% UH6
fig1,ax1 = herr.BasicCanvas(ListP3U[0],"U1 (V)", "I (nA)")
ax1.plot(UH6[0],UH6[1])
ax1.scatter(posMinU265,minU265,s = 8, c = "red")
fig1.show()


#%%% UH7
fig2,ax2 = herr.BasicCanvas(ListP3U[1],"U1 (V)", "I (nA)")
ax2.plot(UH7[0],UH7[1])
ax2.scatter(posMinU268,minU268,s = 8, c = "red")
fig2.show()

#%%% Diff U6
"""
fig3,ax3 = herr.BasicCanvas(r"$\Delta U_{min}(n)$", "min_n-min_{n-1}","$\Delta U_min (V)$")
ax3.scatter(np.linspace(0,len(diffMin), 1),diffMin)
fig3.show()
"""
#%% Calculos numericos

