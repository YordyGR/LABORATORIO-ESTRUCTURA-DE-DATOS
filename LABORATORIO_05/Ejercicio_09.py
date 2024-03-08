#Laboratorio 5
# ejercicio 9

"""Escriba una función que reciba un conjunto de palabras y devuelva un conjunto con las palabras que
tienen una longitud determinada."""

def obtener_palabras_por_longitud(palabras, longitud):
    palabras_filtradas = set()
    for palabra in palabras:
        if len(palabra) == longitud:
            palabras_filtradas.add(palabra)
    return palabras_filtradas

# Conjunto de palabras de ejemplo
palabras = {"lunes", "mesa", "casa", "perro", "gato", "burro"}

# Longitud deseada
longitud_deseada = 4
# Llamada a la función
resultado = obtener_palabras_por_longitud(palabras, longitud_deseada)
# Imprimir el conjunto de palabras filtradas
print(resultado)

