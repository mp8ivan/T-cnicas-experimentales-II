# -*- coding: utf-8 -*-
"""
Graficador
A partir de los txt de la carpeta APuntos, hace distintas graficas
"""

import numpy as np
import matplotlib.pyplot as plt
from Herramientas import TTD
import os as os
import scipy as sci

os.chdir('C:/Users/feyra/Desktop/UNI/UNI-Alicante/3er Año/Tecnicas Experimentales II/Cuantica/P4/TratamientoDatos/')
fileNames = np.array(os.listdir("P1/T/"))

#%% Parte 1
# Escoge una grafica (estan en el orden que ponga en la carpeta // Alfabetico)
currentFileIndex = 3
currentFileName =fileNames[currentFileIndex] 
graf1 = TTD("P1/T/" + currentFileName)



# Ajusta que consideras minimo
startIndex = 600
required_width = 5
#------------------
yCortado = graf1[1][startIndex:]
xCortado = graf1[0][startIndex:]

indexMinimos = sci.signal.find_peaks(-yCortado,distance = 120,width = required_width)[0]
minimos = np.zeros(len(indexMinimos))
minDiff = np.zeros(len(indexMinimos)-1)
posMinimos = np.zeros(len(indexMinimos))
for i in range(len(indexMinimos)):
    posMinimos[i] = xCortado[indexMinimos[i]]
    minimos[i] = yCortado[indexMinimos[i]]
    if i != 0: minDiff[i-1] = posMinimos[i]-posMinimos[i-1]
        
    


#%%% Grafico
fig,ax = plt.subplots()
fig.suptitle(currentFileName)
ax.set_xlabel("Voltaje (V)")
ax.set_ylabel(r"$I_A (nA)$")
ax.grid()
ax.plot(graf1[0],graf1[1])
ax.scatter(posMinimos,minimos)
plt.show()