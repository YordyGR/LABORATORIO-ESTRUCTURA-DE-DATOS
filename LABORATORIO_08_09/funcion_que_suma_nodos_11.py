#Laboratorio 8 y 9
# ejercicio 11
# listas enlazadas
"""11. Implementa una función que sume todos los nodos de una lista enlazada simple"""

class Nodo:
    def __init__(self, dato):
        self.dato = dato
        self.siguiente = None

class ListaEnlazada:
    def __init__(self):
        self.cabeza = None

    def esta_vacia(self):
        return self.cabeza == None

    def agregar(self, dato):
        nuevo_nodo = Nodo(dato)
        if self.esta_vacia():
            self.cabeza = nuevo_nodo
        else:
            nodo_actual = self.cabeza
            while nodo_actual.siguiente:
                nodo_actual = nodo_actual.siguiente
            nodo_actual.siguiente = nuevo_nodo

    def sumar_nodos(self):
        suma = 0
        nodo_actual = self.cabeza
        while nodo_actual:
            suma += nodo_actual.dato
            nodo_actual = nodo_actual.siguiente
        return suma

    def imprimir(self):
        nodo_actual = self.cabeza
        while nodo_actual:
            print(nodo_actual.dato, end= "--->")
            nodo_actual = nodo_actual.siguiente

#agregamos nodos
lista_enlazada = ListaEnlazada()
lista_enlazada.agregar(1)
lista_enlazada.agregar(2)
lista_enlazada.agregar(3)
lista_enlazada.agregar(4)
lista_enlazada.agregar(5)

print("Lista original:")
lista_enlazada.imprimir()

# Función para sumar los nodos de la lista enlazada
def sumar_nodos(lista):
    suma = lista.sumar_nodos()
    return suma

# Llamar a la función para sumar los nodos de la lista enlazada
resultado = sumar_nodos(lista_enlazada)
print("La suma de los nodos de la lista enlazada es:", resultado)
