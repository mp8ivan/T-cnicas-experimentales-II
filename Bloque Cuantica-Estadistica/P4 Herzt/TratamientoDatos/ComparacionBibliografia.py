# -*- coding: utf-8 -*-
"""
Created on Sun Dec 29 14:06:19 2024

@author: feyra
"""

import numpy as np
import matplotlib.pyplot as plt

plt.rcParams.update({'font.size': 15})
plt.figure()
plt.title("Comparación de las energías de salto")
plt.scatter(0,4.887, s = 20, label = "Valor de la bibliografía" )

plt.scatter(0.1,4.88, s = 20,label = r"<$U_{min}$>")
plt.errorbar(0.1, 4.88, 0.03, fmt = "none", capsize = 8)

plt.scatter(0.2,4.869, s= 20, label = r"$E_a$ de la recta de ajuste")
plt.errorbar(0.2, 4.869, 0.01, fmt = "none", capsize = 8)

plt.scatter(0.5,4.869,s = 0)
plt.grid()
plt.legend()
plt.show()
