#Laboratorio 5
# ejercicio 19

"""Escriba una función que reciba un conjunto de números y devuelva un conjunto con los números que
están ordenados de menor a mayor y que no están duplicados."""

def numeros_ordenados_sin_duplicados(numeros):
    numeros_ordenados = sorted(set(numeros))
    return numeros_ordenados

resultado = numeros_ordenados_sin_duplicados({3, 1, 2, 2, 4, 4, 5})
print(resultado)

