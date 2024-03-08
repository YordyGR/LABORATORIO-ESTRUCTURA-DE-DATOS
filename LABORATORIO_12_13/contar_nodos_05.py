#Laboratorio 12 y 13
# ejercicio parte 02 - Arboles
# ejercicio 05

"""Contar nodos:
5. Implementar una función que cuente la cantidad de nodos en el árbol. """

class Nodo:
    def __init__(self, valor):
        self.valor = valor
        self.izquierdo = None
        self.derecho = None

def contar_nodos(arbol):
    if arbol is None:
        return 0
    return 1 + contar_nodos(arbol.izquierdo) + contar_nodos(arbol.derecho)

# Crear un árbol de ejemplo
raiz = Nodo(1)
raiz.izquierdo = Nodo(2)
raiz.derecho = Nodo(3)
raiz.izquierdo.izquierdo = Nodo(4)
raiz.izquierdo.derecho = Nodo(5)

# Contar la cantidad de nodos en el árbol
cantidad_nodos = contar_nodos(raiz)
print(f"La cantidad de nodos en el árbol es: {cantidad_nodos}")
