#Laboratorio 10 y 11
# ejercicio parte 02
# ejercicio 14
# pilas

"""Simular el proceso de deshacer (undo):
14. Implementar un sistema simple de "deshacer" utilizando dos pilas, una para las acciones y otra para los
deshaceres."""

class Pila:
    def __init__(self):
        self.items = []

    def esta_vacia(self):
        return len(self.items) == 0

    def apilar(self, elemento):
        self.items.append(elemento)

    def desapilar(self):
        if self.esta_vacia():
            return None
        return self.items.pop()

def deshacer(accion, pila_acciones, pila_deshacer):
    pila_acciones.apilar(accion)

def rehacer(pila_acciones, pila_deshacer):
    if pila_deshacer.esta_vacia():
        print("No hay acciones para rehacer.")
        return

    accion = pila_deshacer.desapilar()
    pila_acciones.apilar(accion)
    print("Acción rehecha:", accion)

def deshacer_accion(pila_acciones, pila_deshacer):
    if pila_acciones.esta_vacia():
        print("No hay acciones para deshacer.")
        return

    accion = pila_acciones.desapilar()
    pila_deshacer.apilar(accion)
    print("Acción deshecha:", accion)

pila_acciones = Pila()
pila_deshacer = Pila()

deshacer("Accion 1", pila_acciones, pila_deshacer)
deshacer("Accion 2", pila_acciones, pila_deshacer)
deshacer("Accion 3", pila_acciones, pila_deshacer)

deshacer_accion(pila_acciones, pila_deshacer)
deshacer_accion(pila_acciones, pila_deshacer)

rehacer(pila_acciones, pila_deshacer)
