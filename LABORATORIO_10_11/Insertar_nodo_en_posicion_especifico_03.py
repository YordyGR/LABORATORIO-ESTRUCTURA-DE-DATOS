#Laboratorio 10 y 11
# ejercicio 03
# listas enlazadas Dobles

"""Crea una lista con al menos 5 nodos, inserta un nuevo nodo con el dato 15 en la posición 3 e imprime la
lista hacia adelante y hacia atrás."""

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

    def insertar_en_posicion(self, dato, posicion):
        nuevo_nodo = NodoDoble(dato)
        if posicion == 1:
            nuevo_nodo.siguiente = self.cabeza
            self.cabeza.anterior = nuevo_nodo
            self.cabeza = nuevo_nodo
        else:
            nodo_actual = self.cabeza
            contador = 1
            while nodo_actual and contador < posicion:
                nodo_anterior = nodo_actual
                nodo_actual = nodo_actual.siguiente
                contador += 1
            nuevo_nodo.siguiente = nodo_actual
            nuevo_nodo.anterior = nodo_anterior
            nodo_anterior.siguiente = nuevo_nodo
            if nodo_actual:
                nodo_actual.anterior = nuevo_nodo

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

print("Lista original hacia adelante:")
lista_doble.imprimir_adelante()

print("\nLista original hacia atrás:")
lista_doble.imprimir_atras()

lista_doble.insertar_en_posicion(15, 3)

print("\nLista después de insertar el nodo 15 en la posición 3 hacia adelante:")
lista_doble.imprimir_adelante()

print("\nLista después de insertar el nodo 15 en la posición 3 hacia atrás:")
lista_doble.imprimir_atras()

