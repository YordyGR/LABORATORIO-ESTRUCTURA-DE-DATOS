#Laboratorio 5
# ejercicio 2

"""Escriba una función que reciba un conjunto de palabras y devuelva un conjunto con las palabras que
comienzan con una letra determinada"""

# Función que devuelve un conjunto con las palabras que comienzan con una letra determinada
def palabras_que_comienzan_con(conjunto_palabras, letra):
    return {palabra for palabra in conjunto_palabras if palabra[0].lower() == letra.lower()}
# Ejemplo de uso
conjunto_palabras = {"Lima", "Loreto", "Ayacucho", "Arequipa"}
letra = "A"
# Encontrar las palabras que comienzan con la letra "P"
palabras = palabras_que_comienzan_con(conjunto_palabras, letra)
# Imprimir el resultado
print("Las palabras que comienzan con la letra '", letra, "' son:", palabras)