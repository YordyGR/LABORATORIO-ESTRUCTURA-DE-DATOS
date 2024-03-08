#Laboratorio 5
# ejercicio 18

"""Escriba una función que reciba un conjunto de palabras y devuelva un conjunto con las palabras que
contienen una letra determinada y están ordenadas de mayor a menor."""

def palabras_con_letra(words, letter):
    palabras_filtradas = {palabra for palabra in words if letter in palabra}
    return sorted(palabras_filtradas, key=len, reverse=True)

resultado = palabras_con_letra({"gaviota", "adios", "casa", "perro"}, "a")
print(resultado)
