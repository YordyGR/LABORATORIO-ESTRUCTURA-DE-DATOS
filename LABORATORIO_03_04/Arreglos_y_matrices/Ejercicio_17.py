#matrices
#ejercicio 16

#Escribe una función que encuentre la matriz de covarianza de dos matrices.

# Importar la librería NumPy
import numpy as np

# Función que encuentra la matriz de covarianza de dos matrices
def matriz_covarianza(matriz1, matriz2):
    matriz_concatenada = np.concatenate((matriz1, matriz2))
    matriz_covarianza = np.cov(matriz_concatenada.T, rowvar=1).T
    return matriz_covarianza

# Crear dos matrices
matriz1 = np.array([[1, 2, 3], [4, 5], [6, 7, 8, 9]])
matriz2 = np.array([[10, 11], [12, 13], [14, 15], [16, 17]])

# Encontrar la matriz de covarianza de las dos matrices
matriz_covarianza = matriz_covarianza(matriz1, matriz2)

# Imprimir el resultado
print("La matriz de covarianza es:", matriz_covarianza)