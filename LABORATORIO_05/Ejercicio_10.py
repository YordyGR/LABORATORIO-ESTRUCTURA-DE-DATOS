#Laboratorio 5
# ejercicio 10

"""Escriba una función que reciba un conjunto de palabras y devuelva un conjunto con las palabras que
contienen una letra determinada"""

def obtener_palabras_por_letra(palabras, letra):
    palabras_filtradas = set()
    for palabra in palabras:
        if letra in palabra:
            palabras_filtradas.add(palabra)
    return palabras_filtradas

# Conjunto de palabras de ejemplo
palabras = {"lunes", "mesa", "casa", "perro", "gato", "burro"}
# Letra deseada
letra_deseada = "o"
# Llamada a la función
resultado = obtener_palabras_por_letra(palabras, letra_deseada)
# Imprimir el conjunto de palabras filtradas
print(resultado)


