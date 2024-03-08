
#ARREGLOS Y MATRICES
#11) Multiplica una matriz por un número.

# Solicitar al usuario que ingrese un número
numero = float(input("Ingrese un número: "))

# Crear una matriz
matriz = [[1, 2, 3], [4, 5], [6, 7, 8, 9]]

# Inicializar la matriz resultante con ceros
matriz_multiplicada = [[0 for j in range(len(fila))] for fila in matriz]

# Multiplicar la matriz por el número
for i in range(len(matriz)):
    for j in range(len(matriz[0])):
        matriz_multiplicada[i][j] = matriz[i][j] * numero
# Imprimir la matriz resultante
for fila in matriz_multiplicada:
    print(fila)