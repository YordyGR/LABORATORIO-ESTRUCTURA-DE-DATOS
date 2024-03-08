
#Arreglos y Matrices:
#Ejercicio 10) 
# Suma dos matrices de diferentes tamaños.

# Crear dos matrices de diferentes tamaños
matriz1 = [[1, 2, 3], [4, 5]]
matriz2 = [[4, 5, 6], [7, 8], [9, 10, 11]]

# Sumar las matrices
matriz_suma = [[matriz1[i][j] + matriz2[i][j] if i < len(matriz1) and j < len(matriz1[0]) else 0 for j in range(max(len(matriz1[0]), len(matriz2[0]))] if j < len(matriz2[0])] for i in range(max(len(matriz1), len(matriz2))]

# Imprimir la matriz resultante
for fila in matriz_suma:
    print(fila)