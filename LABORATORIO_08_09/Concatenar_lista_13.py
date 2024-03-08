#Laboratorio 8 y 9
# ejercicio 13
# listas enlazadas

"""13. Implementa una función que concatene dos listas enlazadas simples."""
    
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

    def concatenar(self, otra_lista):
        if self.cabeza is None:
            self.cabeza = otra_lista.cabeza
        else:
            nodo_actual = self.cabeza
            while nodo_actual.siguiente:
                nodo_actual = nodo_actual.siguiente
            nodo_actual.siguiente = otra_lista.cabeza

#agregamos nodos
lista_enlazada1 = ListaEnlazada()
lista_enlazada1.agregar(1)
lista_enlazada1.agregar(2)
lista_enlazada1.agregar(3)

lista_enlazada2 = ListaEnlazada()
lista_enlazada2.agregar(4)
lista_enlazada2.agregar(5)
lista_enlazada2.agregar(6)

# Función para concatenar dos listas enlazadas
def concatenar_listas(lista1, lista2):
    lista1.concatenar(lista2)

# Llamar a la función para concatenar las dos listas enlazadas
concatenar_listas(lista_enlazada1, lista_enlazada2)

# Imprimir la lista resultante
nodo_actual = lista_enlazada1.cabeza
while nodo_actual:
    print(nodo_actual.dato, end=" ---> ")
    nodo_actual = nodo_actual.siguiente
