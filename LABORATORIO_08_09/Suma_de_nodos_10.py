#Laboratorio 8 y 9
# ejercicio 10
# listas enlazadas

"""10. Desarrollar el código de buscar nodo en la lista enlazada simple."""

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

    def buscar_nodo(self, dato): # funcion para buscar el nodo en la lista
        actual = self.cabeza
        encontrado = False

        while actual is not None and not encontrado:
            if actual.dato == dato:
                encontrado = True
            else:
                actual = actual.siguiente

        return encontrado

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

# Función para buscar un nodo en la lista enlazada
def buscar_nodo(lista, dato):
    encontrado = lista.buscar_nodo(dato)

    if encontrado:
        print("El nodo con el dato", dato, "se encontró en la lista.")
    else:
        print("El nodo con el dato", dato, "no se encontró en la lista.")

# Llamar a la función para buscar un nodo en la lista enlazada
dato_buscado = 5
buscar_nodo(lista_enlazada, dato_buscado)
