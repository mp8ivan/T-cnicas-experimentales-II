# -*- coding: utf-8 -*-
"""
Created on Mon Nov 11 09:08:05 2024

@author: Lucas
"""
import numpy as np
import matplotlib.pyplot as plt


def Fermi (eps):
    n = 1/(np.exp((eps-mu)/k*T)+1)
    return n

def DFermi(eps):
    return -np.exp((eps-mu)/(k*T))/Fermi(eps)**2/(k*T)


k = 1.38E-23 # J / Kelvin
T = 300; #Kelvin
eps = np.linspace(0,1,10000)
mu = np.mean(eps)

plt.plot(eps,Fermi(eps))
plt.title("Fermi")
plt.show()

plt.figure()
plt.title("DFermi")
plt.plot(eps,DFermi(eps))
plt.show()
