#Laboratorio 10 y 11
# ejercicio 05
# listas enlazadas Dobles

"""Crea una lista con al menos 6 nodos, invierte el orden de la lista (el último elemento se convierte en el
primero y viceversa) e imprime la lista hacia adelante y hacia atrás."""

class NodoDoble:
    def __init__(self, dato):
        self.dato = dato
        self.siguiente = None
        self.anterior = None

class ListaEnlazadaDoble:
    def __init__(self):
        self.cabeza = None

    def agregar(self, dato):
        nuevo_nodo = NodoDoble(dato)
        if self.cabeza is None:
            self.cabeza = nuevo_nodo
        else:
            nodo_actual = self.cabeza
            while nodo_actual.siguiente:
                nodo_actual = nodo_actual.siguiente
            nodo_actual.siguiente = nuevo_nodo
            nuevo_nodo.anterior = nodo_actual

    def invertir_lista(self):
        nodo_actual = self.cabeza
        while nodo_actual.siguiente:
            nodo_actual = nodo_actual.siguiente
        self.cabeza = nodo_actual
        while nodo_actual:
            nodo_actual.siguiente, nodo_actual.anterior = nodo_actual.anterior, nodo_actual.siguiente
            nodo_actual = nodo_actual.siguiente

    def imprimir_adelante(self):
        nodo_actual = self.cabeza
        while nodo_actual:
            print(nodo_actual.dato, end=" <--> ")
            nodo_actual = nodo_actual.siguiente
        print("None")

    def imprimir_atras(self):
        nodo_actual = self.cabeza
        while nodo_actual.siguiente:
            nodo_actual = nodo_actual.siguiente
        while nodo_actual:
            print(nodo_actual.dato, end=" <--> ")
            nodo_actual = nodo_actual.anterior
        print("None")


lista_doble = ListaEnlazadaDoble()
lista_doble.agregar(1)
lista_doble.agregar(2)
lista_doble.agregar(3)
lista_doble.agregar(4)
lista_doble.agregar(5)
lista_doble.agregar(6)

print("Lista original hacia adelante:")
lista_doble.imprimir_adelante()

print("\nLista original hacia atrás:")
lista_doble.imprimir_atras()

lista_doble.invertir_lista()

print("\nLista después de invertir el orden hacia adelante:")
lista_doble.imprimir_adelante()

print("\nLista después de invertir el orden hacia atrás:")
lista_doble.imprimir_atras()
