#Laboratorio 8 y 9
# ejercicio 02

"""Verificar el tipo de dato de una variable"""

def verificar_tipo(variable):
    assert isinstance(variable, (int, float, str, list, tuple, dict)), f"El tipo de dato {type(variable).__name__} no es válido"
    return type(variable).__name__

# Ejemplo de uso
numero = 1
cadena = "Hola"
lista = [1, 2, 3]
tupla = (1, 2, 3)
diccionario = {"clave": "valor"}

print(verificar_tipo(numero))  # Debería imprimir 'int'
print(verificar_tipo(cadena))  # Debería imprimir 'str'
print(verificar_tipo(lista))  # Debería imprimir 'list'
print(verificar_tipo(tupla))  # Debería imprimir 'tuple'
print(verificar_tipo(diccionario))  # Debería imprimir 'dict'