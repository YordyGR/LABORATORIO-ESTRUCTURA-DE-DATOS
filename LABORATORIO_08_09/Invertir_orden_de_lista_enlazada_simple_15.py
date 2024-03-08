#Laboratorio 8 y 9
# ejercicio 15
# listas enlazadas

"""15. Implementa una función que invierta el orden de una lista enlazada simple."""

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

    def invertir(self):
        nodo_actual = self.cabeza
        nodo_anterior = None

        while nodo_actual:
            siguiente_nodo = nodo_actual.siguiente
            nodo_actual.siguiente = nodo_anterior
            nodo_anterior = nodo_actual
            nodo_actual = siguiente_nodo

        self.cabeza = nodo_anterior

    def imprimir(self):
        nodo_actual = self.cabeza
        while nodo_actual:
            print(nodo_actual.dato, end=" ---> ")
            nodo_actual = nodo_actual.siguiente

lista_enlazada = ListaEnlazada()
lista_enlazada.agregar(1)
lista_enlazada.agregar(2)
lista_enlazada.agregar(3)
lista_enlazada.agregar(4)
lista_enlazada.agregar(5)

print("Lista original:")
lista_enlazada.imprimir()

lista_enlazada.invertir()

print("\nLista invertida:")
lista_enlazada.imprimir()
