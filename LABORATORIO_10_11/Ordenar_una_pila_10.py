
#Laboratorio 10 y 11
# ejercicio parte 02
# ejercicio 10
# pilas
"""Ordenar una pila:
10. Ordenar los elementos de una pila de manera ascendente utilizando estructuras adicionales"""

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

def ordenar_pila_ascendente(pila):
    pila_ordenada = Pila()
    while not pila.esta_vacia():
        temp = pila.desapilar()
        while not pila_ordenada.esta_vacia() and pila_ordenada.items[-1] > temp:
            pila.apilar(pila_ordenada.desapilar())
        pila_ordenada.apilar(temp)
    return pila_ordenada


mi_pila = Pila()
mi_pila.apilar(5)
mi_pila.apilar(3)
mi_pila.apilar(8)
mi_pila.apilar(2)

pila_ordenada = ordenar_pila_ascendente(mi_pila)

print("Pila original:", [elemento for elemento in mi_pila.items[::-1]])
print("Pila ordenada de manera ascendente:", [elemento for elemento in pila_ordenada.items])
