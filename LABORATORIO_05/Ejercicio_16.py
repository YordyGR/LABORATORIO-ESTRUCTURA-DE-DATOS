#Laboratorio 5
# ejercicio 16

"""realiza una función que reciba un conjunto de palabras y devuelva un conjunto con las palabras que son
palíndromos y están ordenadas de menor a mayor"""

def palabras_palindromas(palabras):
    palindromos = set()

    for palabra in palabras:
        if palabra == palabra[::-1]:
            palindromos.add(palabra)

    palindromos_ordenados = sorted(palindromos)
    return set(palindromos_ordenados)

# Conjunto de palabras de ejemplo
palabras = {"ana", "oro", "casa", "radar", "sol", "oso"}

# Llamada a la función
resultado = palabras_palindromas(palabras)

# Imprimir el conjunto de palabras palíndromas ordenadas
print(resultado)
