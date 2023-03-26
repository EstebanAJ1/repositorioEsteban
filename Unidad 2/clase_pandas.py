import pandas as pd 
import numpy as np
import os 
import glob 

s = pd.Series(np.random.randn(5), index=["a","b","c","d","e"])
s.index
print(s)
print(s.index)

 # Por defecto me ordena los indices
d = {"b":1,"a":0,"c":2}
s = pd.Series(d)
print(s)

# Se pone el orden en el que quiero que aparezca
d = {"a":0.0,"b":1.0,"c":2.0}
s = pd.Series(d,index=["b","c","d","a"])
print(s)
print("="*50)



current = os.getcwd() # Toma la direccion de la carpeta actual
#print(current) para ver en donde esta buscando el archivo (la direccion)
file = glob.glob(current+'/*.csv') # obtiene una lista con todos los .csv
#print(file)
#mmse_0 = pd.read_csv(file[0])
#print(mmse_0)
mmse = pd.read_csv(file[0], sep = ';') # Para que me separe los ';' y me lo organice
print(mmse)
print("="*50)
print(mmse["Escolaridad"].describe())
print("="*50)
# CARGAR UN ARCHIVO
# Axis = 1 me representa las columnas, y Axis = 0 me representa las filas
mmse_copy = mmse.copy()
mmse_copy = mmse_copy.assign(falseindex = np.random.rand(23))
mmse_copy = mmse_copy.set_index("Codigo")
print(mmse_copy)
print("="*50)
print(mmse_copy.loc["CTR_007"]) # Obtiene filas y/o columnas con posiciones particulares
print(mmse_copy.iloc[0])  # Obtiene filas y/o columnas en posiciones enteras (con la posicion)

print("="*50)
