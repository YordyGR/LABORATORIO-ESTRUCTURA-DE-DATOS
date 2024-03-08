#Laboratorio 5
# ejercicio 7

"""Escriba una función que reciba dos conjuntos de números y devuelva un conjunto con los números que
están en el segundo conjunto pero no en el primero."""

# Función que devuelve un conjunto con las palabras que son anagramas
def anagramas(conjunto):
    anagramas = set()
    for palabra in conjunto:
        # Crear una lista de caracteres de la palabra
        caracteres = list(palabra)
        # Ordenar la lista de caracteres
        caracteres.sort()
        # Convertir la lista ordenada de caracteres en una cadena
        cadena_ordenada = ''.join(caracteres)
        # Crear un conjunto de palabras que son anagramas de la palabra actual
        anagramas_palabra = {palabra2 for palabra2 in conjunto if sorted(palabra2) == cadena_ordenada and palabra2 != palabra}
        # Añadir el conjunto de palabras que son anagramas de la palabra actual al conjunto de anagramas
        anagramas.update(anagramas_palabra)
    return anagramas

# Ejemplo de uso
conjunto = {"ana", "naan", "cabeza", "cabecera", "cabra", "racab", "rac", "car", "arc", "caracol", "caracola"}
anagrama = anagramas(conjunto)
print(anagrama)