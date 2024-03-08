#Laboratorio 8 y 9
# ejercicio 12
# listas enlazadas

"""12. Crea una función que devuelva la longitud de una lista enlazada simple"""

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

    def longitud(self):
        contador = 0
        nodo_actual = self.cabeza
        while nodo_actual:
            contador += 1
            nodo_actual = nodo_actual.siguiente
        return contador

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

print("Lista original:")
lista_enlazada.imprimir()

# Función para obtener la longitud de la lista enlazada
def obtener_longitud(lista):
    longitud = lista.longitud()
    return longitud

# Llamar a la función para obtener la longitud de la lista enlazada
resultado = obtener_longitud(lista_enlazada)
print("La longitud de la lista enlazada es:", resultado)