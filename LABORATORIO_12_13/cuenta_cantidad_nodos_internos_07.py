#Laboratorio 12 y 13
# ejercicio parte 02 - Arboles
# ejercicio 07

"""
contar nodos
7. Implementar una función que cuente la cantidad de nodos internos (que tienen al menos un hijo)."""

class Nodo:
    def __init__(self, valor):
        self.valor = valor
        self.izquierdo = None
        self.derecho = None

def contar_nodos_internos(arbol):
    if arbol is None or (arbol.izquierdo is None and arbol.derecho is None):
        return 0
    return 1 + contar_nodos_internos(arbol.izquierdo) + contar_nodos_internos(arbol.derecho)

# Ejemplo de uso
# Crear un árbol de ejemplo
raiz = Nodo(1)
raiz.izquierdo = Nodo(2)
raiz.derecho = Nodo(3)
raiz.izquierdo.izquierdo = Nodo(4)
raiz.izquierdo.derecho = Nodo(5)

# Contar la cantidad de nodos internos en el árbol
cantidad_nodos_internos = contar_nodos_internos(raiz)
print(f"La cantidad de nodos internos en el árbol es: {cantidad_nodos_internos}")
