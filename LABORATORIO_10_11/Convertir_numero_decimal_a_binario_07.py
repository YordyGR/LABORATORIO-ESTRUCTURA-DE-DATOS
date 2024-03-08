#Laboratorio 10 y 11
# ejercicio parte 02
# ejercicio 07
# pilas

"""Convertir número decimal a binario:
7. Implementar un programa que convierta un número decimal a su representación en sistema binario
utilizando una pila."""

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

def decimal_a_binario(decimal):
    pila = Pila()
    while decimal > 0:
        residuo = decimal % 2
        pila.apilar(residuo)
        decimal = decimal // 2
    binario = ""
    while not pila.esta_vacia():
        binario += str(pila.desapilar())
    return binario


numero_decimal = 55
numero_binario = decimal_a_binario(numero_decimal)
print("Número decimal:", numero_decimal)
print("Número binario:", numero_binario)
