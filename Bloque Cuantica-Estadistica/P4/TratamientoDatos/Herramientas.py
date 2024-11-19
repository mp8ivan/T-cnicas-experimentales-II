# Librerias
import numpy as np
import os
import matplotlib.pyplot as plt

#%% Trasladar data 
"""
Txt to Data (TTD):
Dado un path relativo a un documento de texto con datos guardados por columnas, asocia a cada columna una lista de datos.
Devuelve una matriz de datos en la que cada fila corresponde a un tipo de dato.
Los datos deben estar separados por una tabulación.

Dato_1.1    Dato_2.1
Dato_2.1    Dato_2.2
etc
"""
def ComasToPuntos(path):
    data = ""
    with open(path, 'r') as file:
        try:
            """
            Apaño para la P4 Cuantica; Me quito las 3 primeras lineas
            
            file.readline()
            file.readline()
            file.readline()
            """
            data = file.read().replace(',', '.')
        except:
            print("No ha podido leer a puntos. Revisa el  path")
            return False
    with open(path, "w") as out_file:
        try:
            out_file.write(data)
        except:
            print("No ha podido escribir a puntos")           
            return False
        
        return True
    
def TTD(path):
    
    file = open(path, "r")
    try:
        cifra = file.readline().replace("\n","") # Leo la primera linea para inizializar la categoria de datos
        cifra.replace(" ","") # Quito tambien los espacios 
        if cifra == "": # Documento vacio
            file.close()
            print("Me has dado un documento vacio // Primea linea vacia")
            return None
        n_datos = len(cifra.split("\t")) # El numero de columnas de datos
        data = [[]]*n_datos
        # Voy leyendo los datos
        while cifra != "" and cifra != "\n":
            aux = cifra.split("\t") # Lista de números
            for i in range(len(aux)): # Voy metiendo cada uno en su lista
                try: 
                    data[i] = data[i] + [(float(aux[i]))]
                except: # No habia dato: Se levantará error de pasar "" a float.
                    pass # Seguimos y listo
            cifra = file.readline().replace("\n","") # Leo la siguiente linea
            cifra.replace(" ", "") # Quito tambien los espacios
        # Cuando haya terminado, paso cada fila a un array:
        for i in range(len(data)):
            data[i] = np.array(data[i], dtype = float)
    except:
        file.close() # Ante todo aseguro que los datos estén bien
        raise # Informo del error
        
    # Cuando he terminado, cierro el fichero y devuelvo data
    file.close()    
    return np.array(data, dtype = object)
#%%
"""
Data To Txt (DTT):
Dado una matriz de datos, escribe cada fila en un txt distinto para poder copiarlo rapidamente a SciDavis.
Los escribe por columnas porque así es como lo lee SciDavis, y cambia los puntos por comas.
"""


def DTT (data):
    # Determinamos el numero de filas necesarias
    n_datos = len(data)
    isMatrix = None
    try: #Veamos si es una matriz intentando acceder a uno de sus elementos 
        data[0][0]
        isMatrix = True
    except: # Si no se ha podido, es que es solo una lista
        isMatrix = False
    
    # Determinamos el path donde guardar los ficheros
    path = os.getcwd() + "\\DTT"
    if not os.path.exists(path): # Si no existe este path, lo creo. 
        os.mkdir(path) # Creo la carpeta
    # Empezamos a escribir
    try:  
        if not isMatrix: # Solo hay un array
            file = open(path + "\\data.txt","w") # Ojo, esto implica que, en caso de que ya exista un fichero con este nombre,
                                                 # lo voy a reescribir. Asegurate de haber guardado los files anteriores en otro
                                                 # sitio si vas a ejecutar DTT varias veces.  
            file.write("Hemos escrito un total de {} datos:\n\n".format(n_datos))
                                                 
            for cifras in data:
                cifras = str(cifras)
                # punto = cifras.find(".")
                if False: # punto != -1:
                    print("nada que ver")
                    # file.write(cifras[:punto] + "," + cifras[punto + 1:])
                else:
                    file.write(cifras) 
                file.write("\n") # Separo las cifras con un salto de linea
            file.close()
        
        else: # Tengo una matriz. Voy fila a fila
            for i in range(n_datos):
                file = open(path + "\\data{}.txt".format(i + 1),"w")
                file.write("Hemos escrito un total de {} datos:\n\n".format(len(data[i])))
                for cifras in data[i]:
                    cifras = str(cifras)
                    # punto = cifras.find(".")
                    if False: # punto != -1:
                        print("nada que ver")
                        #file.write(cifras[:punto] + "," + cifras[punto + 1:])
                    else:
                        file.write(cifras) 
                    file.write("\n") # Separo las cifras con un salto de linea
                file.close()
    except:
            print("Ha ocurrido un error. Abortando...")
            file.close()
            raise
    print("Listo, La información está almacenada en:\n{}".format(path))
    return
#%% Calculo de erroes
"""
errA:
  Calcula el error tipo A de un conjunto de medidas  
"""
def errA (data):
    media = np.sum(data)/len(data)
    error = np.sqrt(np.sum((data-media)**2)/((len(data)-1)*len(data)))
    return error

#%% Graficas

def BasicCanvas(title = "title", xlab = "xlabel", ylab = "ylabel"):
    """
    Basic Canvas devuelve un plot con la siguientes caracteristicas
        1. Grid
        2. Titulo
        3. Labels ejes
    """
    fig, ax = plt.subplots()
    ax.grid()
    fig.suptitle(title)
    ax.set_xlabel(xlab)
    ax.set_ylabel(ylab)
    return fig,ax