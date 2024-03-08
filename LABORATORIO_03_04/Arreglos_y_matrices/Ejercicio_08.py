#Arreglos y Matrices:
#8) Crea una matriz de matrices.

matriz = [[[1, 2, 3], [4, 5, 6], [7, 8, 9]] for i in range(3)]

# Imprimir la matriz
for fila in matriz:
    for sub_matriz in fila:
        print(sub_matriz)
    print()