# -*- coding: utf-8 -*-
import numpy as np
import matplotlib.pyplot as plt
import Herramientas as herr
import os as os
import scipy as sci
"""
Parte A: HG VARIANDO T
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
pth = "P1/T/"
ListP2U = np.array(os.listdir(pth))

DataList = []
minList = []
minPos = []

for i in range(len(ListP2U)):
    DataList.append( herr.TTD(pth  + ListP2U[i]))
    # Buscando minimos
    auxMin, auxPosMin = BuscadorMinimos(DataList[i], 800, 0.001)
    minList.append(auxMin)
    minPos.append(auxPosMin)


#%% Diferencia de minimos
minDiff = []
for i in range(len(ListP2U)):
    aux = []
    for j in range(1,len(minList[i])): # Voy por cada diferencia
        aux.append(minPos[i][j]-minPos[i][j-1])
    minDiff.append(aux)
        
    

#%% Graficas
for i in range(len(ListP2U)):
    fig1,ax1 = herr.BasicCanvas(ListP2U[i],"U1 (V)", "I (nA)")
    ax1.plot(DataList[i][0],DataList[i][1])
    ax1.scatter(minPos[i],minList[i])
    fig1.show()
for i in range(len(ListP2U)):        # lo mismo para diferencias 
    fig1,ax1 = herr.BasicCanvas(ListP2U[i] + r": $\Delta U_{min}$","\Delta U_{min} (V)", "")
    ax1.scatter(np.arange(0,len(minDiff[i]),1),minDiff[i])
    fig1.show()