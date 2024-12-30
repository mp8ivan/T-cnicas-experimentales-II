# -*- coding: utf-8 -*-
"""
Tratamiento de datos del extra
"""

import numpy as np
import matplotlib.pyplot as plt
import Herramientas as herr
import os as os
import scipy as sci

plt.rcParams.update({'font.size': 15})

data = herr.TTD("Extra/data.txt")
errorI = np.ones(len(data[1])) * 0.15 # Tomamos error 0.1 de intensidad porque bailaba mucho
 
f,ax = herr.BasicCanvas("Intensidad respecto al ángulo de polarización",
                        "Ángulo respecto a la vertical","Intensidad (nA)")

ax.scatter(data[0],data[1],s = 12)
ax.errorbar(data[0],data[1], errorI, fmt = "none", capsize = 8)
