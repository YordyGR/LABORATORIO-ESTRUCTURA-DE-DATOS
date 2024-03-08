
#Laboratorio 10 y 11
# ejercicio 02
# listas enlazadas Dobles

"""Crea una lista con al menos 9 nodos, cuenta cuántos nodos tienen un dato par y cuántos tienen un dato
impar e imprime la lista hacia adelante y hacia atrás. """

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

    def contar_pares_impares(self):
        nodo_actual = self.cabeza
        pares = 0
        impares = 0
        while nodo_actual:
            if nodo_actual.dato % 2 == 0:
                pares += 1
            else:
                impares += 1
            nodo_actual = nodo_actual.siguiente
        return pares, impares

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
lista_doble.agregar(7)
lista_doble.agregar(8)
lista_doble.agregar(9)

print("Lista original hacia adelante:")
lista_doble.imprimir_adelante()

print("\nLista original hacia atrás:")
lista_doble.imprimir_atras()

pares, impares = lista_doble.contar_pares_impares()
print("\nCantidad de nodos con dato par:", pares)
print("Cantidad de nodos con dato impar:", impares)
