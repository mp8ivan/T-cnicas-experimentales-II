# -*- coding: utf-8 -*-
import numpy as np
import os as os
from Herramientas import ComasToPuntos
"""
Pasando los datos a puntos
"""
os.chdir('C:/Users/feyra/Desktop/UNI/UNI-Alicante/3er Año/Tecnicas Experimentales II/Cuantica/P4/TratamientoDatos/')
# 1: Leemos todos los datos de la carpeta
names = np.array(os.listdir("APuntos/"));

for i in range(len(names)):
    ComasToPuntos("APuntos/" + names[i])
    os.rename("APuntos/" + names[i], "YaPuntos/" + names[i])

