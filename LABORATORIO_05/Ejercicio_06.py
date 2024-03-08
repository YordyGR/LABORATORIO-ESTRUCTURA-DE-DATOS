#Laboratorio 5
# ejercicio 6

"""Escriba una función que reciba dos conjuntos de números y devuelva un conjunto con los números que
están en el segundo conjunto pero no en el primero."""

# Función que devuelve un conjunto con los números que están en el segundo conjunto pero no en el primero
def diferencia_conjuntos(conjunto1, conjunto2):
    return conjunto2.difference(conjunto1)

# Ejemplo de uso
conjunto1 = {1, 2, 3, 4, 5}
conjunto2 = {4, 5, 6, 7, 8}

# Encontrar los números que están en el segundo conjunto pero no en el primero
diferencia = diferencia_conjuntos(conjunto1, conjunto2)

# Imprimir el resultado
print("Los números que están en el segundo conjunto pero no en el primero son:", diferencia)