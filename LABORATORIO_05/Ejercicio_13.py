#Laboratorio 5
# ejercicio 13

"""Escriba una función que reciba un conjunto de números y devuelva un conjunto con los números que
están duplicados."""

def encontrar_duplicado(numeros):
    numeros_duplicados = set()
    numeros_vistos = set()
    for numero in numeros:
        if numero in numeros_vistos:
            # Añadir el número al conjunto de números duplicados
            numeros_duplicados.add(numero)
        # Si el número no está en el conjunto de números vistos
        else:
            # Añadir el número al conjunto de números vistos
            numeros_vistos.add(numero)
    return numeros_duplicados

# Ejemplo de uso
numeros = {2, 3, 4, 5, 2, 4, 6}
# Llamada a la función
resultado = encontrar_duplicado(numeros)
# Imprimir el conjunto de números duplicados
print(resultado)
