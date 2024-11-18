# -*- coding: utf-8 -*-
"""
Procesamiento de data de la P6
"""
import numpy as np
import matplotlib.pyplot as plt
import Herramientas as Herr
import pandas as pd

"""
sheet_A = pd.read_excel("P6A.xlsx")
sheet_B = pd.read_excel("P6B.xlsx")

print(sheet_A)
"""

dataDesf = Herr.TTD("Data_Desf.txt")
alfGrad = np.array(dataDesf[0],dtype = float)
alfRad =  np.array(dataDesf[1],dtype = float)
sin2 = np.array(dataDesf[2],dtype = float)
Inorm = np.array(dataDesf[4],dtype = float)


#%% GRAFICO I SIN2
# De excel
x = np.linspace(-0.1,1.1, 200)
#y_ajuste = 0.536*x + 0.0007

# De numpy
b,a = np.polyfit(sin2,Inorm, deg=1);
y_np = b*x + a

fig, ax = plt.subplots()
ax.set_xlabel(r"$\sin^2 ()$")
ax.set_ylabel(r"$I_{norm}\ (mW)$")
fig.suptitle("Ajuste lineal para $\delta$")
ax.scatter(sin2,Inorm)
#ax.plot(x,y_ajuste, c= "brown")
ax.plot(x,y_np, c = "green")
ax.grid()
fig.show()