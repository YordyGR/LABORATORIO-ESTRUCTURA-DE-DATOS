#Laboratorio 10 y 11
# ejercicio parte 02
# ejercicio 11
# pilas

"""Eliminar duplicados:
11. Eliminar los elementos duplicados de una pila """

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

def eliminar_duplicados_pila(pila):
    pila_sin_duplicados = Pila()
    elementos_vistos = set()

    while not pila.esta_vacia():
        elemento = pila.desapilar()
        if elemento not in elementos_vistos:
            pila_sin_duplicados.apilar(elemento)
            elementos_vistos.add(elemento)

    return pila_sin_duplicados

mi_pila = Pila()
mi_pila.apilar(5)
mi_pila.apilar(3)
mi_pila.apilar(8)
mi_pila.apilar(3)
mi_pila.apilar(5)

pila_sin_duplicados = eliminar_duplicados_pila(mi_pila)

print("Pila original:", [elemento for elemento in mi_pila.items[::-1]])
print("Pila sin duplicados:", [elemento for elemento in pila_sin_duplicados.items[::-1]])
