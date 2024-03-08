#Laboratorio 5
# ejercicio 15

"""15. Escriba una función que reciba un conjunto de números y devuelva un conjunto con los números que
son primos y están ordenados de menor a mayor."""

def numeros_primos(numeros):
    primos = set()

    for numero in numeros:
        if numero > 1:
            es_primo = True
            for i in range(2, numero):
                if numero % i == 0:
                    es_primo = False
                    break
            if es_primo:
                primos.add(numero)

    primos_ordenados = sorted(primos)
    return set(primos_ordenados)

# Conjunto de números de ejemplo
numeros = {2, 3, 4, 5, 6, 7, 8, 9, 10}

# Llamada a la función
resultado = numeros_primos(numeros)

# Imprimir el conjunto de números primos ordenados
print(resultado)
