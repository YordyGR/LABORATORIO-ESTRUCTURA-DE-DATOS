#Laboratorio 12 y 13
# ejercicio parte 01 - colas
# ejercicio 01

"""Verificar si una palabra es palíndroma
1. Implementa una función que determine si una palabra es palíndroma o no. Utiliza una cola para
comparar los caracteres de la palabra en orden original y reverso. """

from collections import deque

def es_palindromo(palabra):
    cola_original = deque()
    cola_reversa = deque()

    for letra in palabra:
        cola_original.append(letra)
        cola_reversa.appendleft(letra)

    es_palindromo = True
    while len(cola_original) > 0 and es_palindromo:
        letra_original = cola_original.popleft()
        letra_reversa = cola_reversa.popleft()
        if letra_original != letra_reversa:
            es_palindromo = False

    return es_palindromo

palabra = "ana"
resultado = es_palindromo(palabra)
print(f"La palabra {palabra} es palíndroma: {resultado}")
