# -*- coding: utf-8 -*-
"""
Calculo errores P1
"""
import numpy as np
import matplotlib.pyplot as plt
"""
Parte A: Determinacion del indice de refraccion de una lamina
"""
dList = np.array([5.82,5.83,5.82])
errD = 0.01 # mm

dRelList = np.array([3.94,3.97,3.95]) 
errDRel = 0.01 # mm

relD = errD/dList
relDrel = errDRel / dRelList

n = np.array([1.48,1.47,1.47])
errN = n * (relD + relDrel)


"""
Parte B
"""