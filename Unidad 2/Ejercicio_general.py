# EJERCICIO 
import pandas as pd 
import numpy as np
import os 
import glob

current = os.getcwd()
file = glob.glob(current+"/*.csv")
file2 = glob.glob(current+"/*.xlsx")

mmse = pd.read_csv(file[0], sep = ';')
mmse2 = pd.read_excel(file2[0])
eval_med = pd.read_excel(file2[1])
#print(mmse)

#print("="*40)
mmse_edad = mmse.sort_values(["Edad en la visita"])
mmse_org = mmse_edad.reset_index()
del mmse_org["index"]
print(mmse_org)
#print(file2)
print("="*40)
#print(mmse2)

conc = pd.concat([mmse, eval_med])
print(conc)


