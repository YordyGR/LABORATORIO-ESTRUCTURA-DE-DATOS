#-----Arreglos y Matrices:-----

#7) Crea una matriz de números complejos.

# Importar la librería "cmath" para trabajar con números complejos
import cmath

# Crear una matriz de números complejos
matriz = []
for i in range(5):
    fila = []
    for j in range(5):
        fila.append(cmath.rect(2, j))
    matriz.append(fila)

# Imprimir la matriz
for fila in matriz:
    print(fila)