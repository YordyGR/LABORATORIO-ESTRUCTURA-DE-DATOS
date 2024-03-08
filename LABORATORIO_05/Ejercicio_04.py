#Laboratorio 5
# ejercicio 4
"""Escriba una función que reciba dos conjuntos de números y devuelva un conjunto con los números que están en ambos conjuntos"""

# Función que devuelve un conjunto con los números que están en ambos conjuntos
def interseccion_conjuntos(conjunto1, conjunto2):
    return conjunto1.intersection(conjunto2)
# Ejemplo de uso
conjunto1 = {5, 2, 3, 4, 5}
conjunto2 = {4, 5, 3, 7, 7}
# Encontrar los números que están en ambos conjuntos
interseccion = interseccion_conjuntos(conjunto1, conjunto2)
# Imprimir el resultado
print("Los números que están en ambos conjuntos son:", interseccion)