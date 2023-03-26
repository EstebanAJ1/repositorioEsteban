########### Ejercicio 1 ##############
import numpy as np

#1 Crear una matriz de ceros de tipo entero 3x4.
#2 Crear una matriz de ceros de tipo entero 3x4 excepto la primera fila que será uno.
#3 Crear una matriz de ceros de tipo entero 3x4 excepto la última fila que será el rango entre 5 y 8.

#1
print("\t"+"----Ejercicio 1----")
a = np.zeros((3,4), dtype=int)
print(a)
print("="*20)
#2
x = np.ones((1,4), dtype=int)
y = np.zeros((2,4), dtype=int)
print(np.concatenate((x,y)))
print("="*20)
#3
x = np.zeros((4), dtype=int)
y = np.zeros((4), dtype=int)
z = np.arange(5,9, dtype=int)
print(np.concatenate((x,y,z)).reshape(3,4))
print("\n")

########### Ejercicio 2 ##############
#1 Crea un vector de 10 elementos, siendo los índices impares unos y los índices pares dos.
#2 Crea un «tablero de ajedrez», con unos en las casillas negras y ceros en las blancas.

#1
print("\t"+"----Ejercicio 2----")

b = np.ones((2,5), dtype=int)
b[::2, ::2] = 2
b[1::2, ::2] = 2

print(b)
print("="*20)

#2
t = np.zeros((8,8), dtype=int)
t[::2, 1::2] = 1
t[1::2, ::2 ] = 1
print(t)
print("\n")






########### Ejercicio 3 ##############
#1 Crea  una  matriz  aleatoria  5x5  y  halla  los  valores mínimo y máximo.
#2 Normalizar la matriz anterior

#1
print("\t"+"----Ejercicio 3----")
np.random.seed(0)
d = np.random.rand(5,5)
print(d)
max = np.max(d)
min = np.min(d)
print("\n"+"Valor máximo: ",max, "-----","Valor mínimo: ", min)
m = (d - min) / (max - min)
print("="*20)
print(m)
