
#matrices
#ejercicio 16
# Escribe una función que encuentre la submatriz de mayor suma de una matriz

# Importar la librería NumPy
import numpy as np

# Función que encuentra la submatriz de mayor suma de una matriz
def submatriz_mayor_suma(matriz):
    submatriz_mayor_suma = None
    suma_maxima = -np.inf
    for i in range(len(matriz)):
        for j in range(len(matriz)):
            for k in range(i, len(matriz)):
                for l in range(j, len(matriz)):
                    submatriz = matriz[i:k+1, j:l+1]
                    suma = np.sum(submatriz)
                    if suma > suma_maxima:
                        suma_maxima = suma
                        submatriz_mayor_suma = submatriz
    return submatriz_mayor_suma, suma_maxima

# Crear una matriz
matriz = np.array([[1, 2, 3], [4, 5], [6, 7, 8, 9], [10, 11, 12]])

# Encontrar la submatriz de mayor suma de la matriz
submatriz, suma = submatriz_mayor_suma(matriz)

# Imprimir el resultado
print("La submatriz de mayor suma es:", submatriz)
print("La suma de la submatriz es:", suma)