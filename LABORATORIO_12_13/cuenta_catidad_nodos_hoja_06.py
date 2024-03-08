#Laboratorio 12 y 13
# ejercicio parte 02 - Arboles
# ejercicio 06

"""
contar nodos
6. Implementar una función que cuente la cantidad de nodos hoja (que no tienen hijos). """

class Nodo:
    def __init__(self, valor):
        self.valor = valor
        self.izquierdo = None
        self.derecho = None

def contar_nodos_hoja(arbol):
    if arbol is None:
        return 0
    if arbol.izquierdo is None and arbol.derecho is None:
        return 1
    return contar_nodos_hoja(arbol.izquierdo) + contar_nodos_hoja(arbol.derecho)

# Crear un árbol de ejemplo
raiz = Nodo(1)
raiz.izquierdo = Nodo(2)
raiz.derecho = Nodo(3)
raiz.izquierdo.izquierdo = Nodo(4)
raiz.izquierdo.derecho = Nodo(5)

# Contar la cantidad de nodos hoja en el árbol
cantidad_nodos_hoja = contar_nodos_hoja(raiz)
print(f"La cantidad de nodos hoja en el árbol es: {cantidad_nodos_hoja}")
