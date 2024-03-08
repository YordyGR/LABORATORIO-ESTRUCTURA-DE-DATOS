#Laboratorio 5
# ejercicio 11

"""Escriba una función que reciba un conjunto de números y devuelva un conjunto con los números que
están ordenados de menor a mayor."""

def ordenar_numeros(numeros):
    numeros_ordenados = sorted(numeros)
    return set(numeros_ordenados)

numeros = {5, 2, 8, 1, 3,77}
# Llamada a la función
resultado = ordenar_numeros(numeros)
# Imprimir el conjunto de números ordenados
print(resultado)

