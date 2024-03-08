#Laboratorio 5
# ejercicio 12

"""Escriba una función que reciba un conjunto de números y devuelva un conjunto con los números que
están ordenados de mayor a menor."""

def ordenar_numeros(numeros):
    numeros_ordenados = sorted(numeros, reverse=True)
    return set(numeros_ordenados)
numeros = {88, 2, 7, 1, 3}
# Llamada a la función
resultado = ordenar_numeros(numeros)
# Imprimir el conjunto de números ordenados de mayor a menor
print(resultado)
