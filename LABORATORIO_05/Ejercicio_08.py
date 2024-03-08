#Laboratorio 5
# ejercicio 8

"""Escriba una función que reciba un conjunto de palabras y devuelva un conjunto con las palabras que son
palíndromos."""

def obtener_palindromos(palabras):
    palindromos = set()
    for palabra in palabras:
        palabra = palabra.lower()  # Convertir a minúsculas para ignorar mayúsculas
        palabra_invertida = palabra[::-1]  # Invertir la palabra
        if palabra == palabra_invertida:
            palindromos.add(palabra)
    return palindromos
# Conjunto de palabras de ejemplo
palabras = {"reconocer", "casa", "radar", "perro", "ana"}
# Llamada a la función
resultado = obtener_palindromos(palabras)
# Imprimir el conjunto de palabras palíndromas
print(resultado)
