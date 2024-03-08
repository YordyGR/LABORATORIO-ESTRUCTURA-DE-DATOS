
#Laboratorio 8 y 9
# ejercicio 05
"""Validar la igualdad de dos objetos."""

def validar_igualdad(objeto1, objeto2):
    assert objeto1 == objeto2, "Los objetos no son iguales"
    print("son iguales")
# Ejemplo de uso
objeto1 = "Hola"
objeto2 = "Hola"
validar_igualdad(objeto1, objeto2)
