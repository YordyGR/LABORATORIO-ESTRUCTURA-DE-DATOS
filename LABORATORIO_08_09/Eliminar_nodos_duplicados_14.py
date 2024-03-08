#Laboratorio 8 y 9
# ejercicio 14
# listas enlazadas

"""14. Crea una función que elimine los nodos duplicados de una lista enlazada simple."""

class Nodo:
    def __init__(self, dato):
        self.dato = dato
        self.siguiente = None

class ListaEnlazada:
    def __init__(self):
        self.cabeza = None

    def agregar(self, dato):
        nuevo_nodo = Nodo(dato)
        if self.cabeza is None:
            self.cabeza = nuevo_nodo
        else:
            nodo_actual = self.cabeza
            while nodo_actual.siguiente:
                nodo_actual = nodo_actual.siguiente
            nodo_actual.siguiente = nuevo_nodo

    def eliminar_duplicados(self):
        if self.cabeza is None:
            return

        nodos_vistos = set()
        nodos_vistos.add(self.cabeza.dato)

        nodo_actual = self.cabeza
        while nodo_actual.siguiente:
            if nodo_actual.siguiente.dato in nodos_vistos:
                nodo_actual.siguiente = nodo_actual.siguiente.siguiente
            else:
                nodos_vistos.add(nodo_actual.siguiente.dato)
                nodo_actual = nodo_actual.siguiente

    def imprimir(self):
        nodo_actual = self.cabeza
        while nodo_actual:
            print(nodo_actual.dato, end=" ---> ")
            nodo_actual = nodo_actual.siguiente

#agregamos nodos
lista_enlazada = ListaEnlazada()
lista_enlazada.agregar(1)
lista_enlazada.agregar(2)
lista_enlazada.agregar(3)
lista_enlazada.agregar(2)
lista_enlazada.agregar(4)
lista_enlazada.agregar(3)

print("Lista original:")
lista_enlazada.imprimir()

lista_enlazada.eliminar_duplicados()

print("\nLista sin nodos duplicados:")
lista_enlazada.imprimir()
