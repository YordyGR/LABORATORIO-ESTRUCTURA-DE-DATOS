#Laboratorio 8 y 9
# ejercicio 04
"""Asegurar que una lista no esté vacía."""

def verificar_lista(lista):
    assert len(lista) > 0, "La lista está vacía"
    print("La lista no está vacía")

# Ejemplo de uso
mi_lista = [1, 2, 3]
verificar_lista(mi_lista)
