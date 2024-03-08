#Laboratorio 8 y 9
# ejercicio 07

"""Asegurar que una función retorna un valor específico."""

def funcion_ejemplo():
    # Código de la función
    resultado = 50
    return resultado

# Validar que la función retorne un valor específico
assert funcion_ejemplo() == 50, "La función no retornó el valor esperado"
