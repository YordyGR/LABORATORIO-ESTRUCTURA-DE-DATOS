#matrices
#ejercicio 14
#Calcula la media, la mediana y la desviación estándar de los elementos de una matriz.

# Importar la librería NumPy
import numpy as np
# Crear una matriz
matriz = np.array([[1, 2, 3], [4, 5], [6, 7, 8, 9]])
# Calcular la media de los elementos de la matriz
media = np.mean(matriz)
# Calcular la mediana de los elementos de la matriz
mediana = np.median(matriz)
# Calcular la desviación estándar de los elementos de la matriz
desviacion_estandar = np.std(matriz)
# Imprimir los resultados
print("La media de los elementos de la matriz es:", media)
print("La mediana de los elementos de la matriz es:", mediana)
print("La desviación estándar de los elementos de la matriz es:", desviacion_estandar)