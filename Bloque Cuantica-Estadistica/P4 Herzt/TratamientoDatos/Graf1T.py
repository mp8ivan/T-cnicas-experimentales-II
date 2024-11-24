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
    auxMin, auxPosMin = BuscadorMinimos(DataList[i], 700, 0.001)
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
    ax1.scatter(minPos[i],minList[i], s = 8, color = "red")
    fig1.show()

for i in range(len(ListP2U)):        # lo mismo para diferencias 
    fig1,ax1 = herr.BasicCanvas(ListP2U[i] + r": $\Delta U_{min}$","\Delta U_{min} (V)", "")
    if():
    ax1.scatter(np.arange(0,len(minDiff[i]),1),minDiff[i])
    fig1.show()
"""
# Finalmente, grafica de U2-U1(T)
secMinT = np.array([4.73,4.76,4.76,4.75,4.72,4.79,4.67]) # Se calculan a mano porque es mas trabajoso el codigo con deteccion de minimos (nos ayudamos con el visualmente)
media = np.mean(secMinT)
fig2, ax2 = herr.BasicCanvas(r"$U_2-U_1 (T)$","T (grados)",r"$\Delta U\ (eV)$")
T = np.arange(145,180,5)
ax2.scatter(T, secMinT, s = 8)
ax2.errorbar(T,secMinT, np.ones(len(secMinT))*0.04, fmt = "none", capsize = 3 )
ax2.set_ylim(4.5,5)

# Vamos a obtener l(T)


l = (secMinT/4.67 - 1) * 1/3 # Por unidad de L (graficamos l/L(T))
Valph = 4.67 # eV
errsecMin = np.ones(len(secMinT))*0.04
fig3, ax3 = herr.BasicCanvas("Longitud de camino medio por unidad de longitud L","T (grados)", "l/L" )
ax3.scatter(T, l, s = 8)
ax3.errorbar(T, l, errsecMin/(3*Valph),np.ones(len(T))*0.1, fmt = "none", capsize = 2 )  # Error calculado por propagacion de errores
# ax3.set_ylim(4.5,5)
"""