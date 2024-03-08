#ARREGLOS Y MATRICES
#ejercicio 12
#Calcula la media de los elementos de una matriz.
# Crear una matriz
matriz = [[1, 2, 3], [4, 5], [6, 7, 8, 9]]

# Calcular la media de los elementos de la matriz
media = sum(sum(matriz, [])) / len(matriz) / len(matriz[0])

# Imprimir la media
print("La media de los elementos de la matriz es:", media)