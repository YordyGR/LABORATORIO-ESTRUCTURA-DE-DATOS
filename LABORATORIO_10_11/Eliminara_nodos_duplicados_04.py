#Laboratorio 10 y 11
# ejercicio 04
# listas enlazadas Dobles

"""Crea una lista con nodos que contengan datos duplicados, elimina todos los nodos duplicados, dejando
solo una instancia de cada dato e imprime la lista hacia adelante y hacia atrás."""

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

    def eliminar_duplicados(self):
        nodos_vistos = set()
        nodo_actual = self.cabeza
        while nodo_actual:
            if nodo_actual.dato in nodos_vistos:
                nodo_anterior = nodo_actual.anterior
                nodo_siguiente = nodo_actual.siguiente
                if nodo_anterior:
                    nodo_anterior.siguiente = nodo_siguiente
                if nodo_siguiente:
                    nodo_siguiente.anterior = nodo_anterior
            else:
                nodos_vistos.add(nodo_actual.dato)
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
lista_doble.agregar(2)
lista_doble.agregar(4)
lista_doble.agregar(4)
lista_doble.agregar(4)
lista_doble.agregar(3)
lista_doble.agregar(5)

print("Lista original hacia adelante:")
lista_doble.imprimir_adelante()

print("\nLista original hacia atrás:")
lista_doble.imprimir_atras()

lista_doble.eliminar_duplicados()

print("\nLista después de eliminar los nodos duplicados hacia adelante:")
lista_doble.imprimir_adelante()

print("\nLista después de eliminar los nodos duplicados hacia atrás:")
lista_doble.imprimir_atras()
