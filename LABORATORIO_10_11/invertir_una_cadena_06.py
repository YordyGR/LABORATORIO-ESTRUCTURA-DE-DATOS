#Laboratorio 10 y 11
# ejercicio parte 02
# ejercicio 06
# pilas

"""Invertir una cadena:
6. Utilizar una pila para invertir el orden de los caracteres de una cadena. """

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

    def cima(self):
        if self.esta_vacia():
            return None
        return self.items[-1]

def invertir_cadena(cadena):
    pila = Pila()
    resultado = ""
    for caracter in cadena:
        pila.apilar(caracter)
    while not pila.esta_vacia():
        resultado += pila.desapilar()
    return resultado

cadena = "Estructura"
pila = Pila()
for caracter in cadena:
    pila.apilar(caracter)

cadena_invertida = invertir_cadena(cadena)
print("Cadena original:", cadena)
print("Cadena invertida:", cadena_invertida)
