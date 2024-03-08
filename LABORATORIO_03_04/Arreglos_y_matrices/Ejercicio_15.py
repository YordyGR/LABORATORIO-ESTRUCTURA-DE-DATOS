#matrices
#ejercicio 15

#Escribe una función que encuentre el elemento máximo de una matriz.

# Importar la librería NumPy
import numpy as np

# Función que encuentra el elemento máximo de una matriz
def encontrar_maximo(matriz):
    return np.unravel_index(np.argmax(matriz), matriz.shape)
# Crear una matriz
matriz = np.array([[1, 2, 3], [4, 5], [6, 7, 8, 9]])
# Encontrar el elemento máximo de la matriz
maximo = encontrar_maximo(matriz)
# Imprimir el resultado
print("El elemento máximo de la matriz es:", matriz[maximo])