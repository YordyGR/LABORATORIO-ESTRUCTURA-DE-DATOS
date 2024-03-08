#Laboratorio 5
# ejercicio 17

"""Escriba una función que reciba un conjunto de palabras y devuelva un conjunto con las palabras que
tienen una longitud determinada y están ordenadas de menor a mayor"""

def palabras_por_longitud(frase, longitud):
    palabras = frase.split()
    palabras_filtradas = [palabra for palabra in palabras if len(palabra) == longitud]
    return sorted(palabras_filtradas, key=len)

resultado = palabras_por_longitud("Yo estoy estudiando programacion", 5)
print(resultado)  # Esto imprimirá: ['estoy']
