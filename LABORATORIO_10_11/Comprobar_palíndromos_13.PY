#Laboratorio 10 y 11
# ejercicio parte 02
# ejercicio 13
# pilas

"""Comprobar palíndromos:
13. Utilizar una pila para comprobar si una palabra o frase es un palíndromo."""

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

def es_palindromo(palabra):
    pila = Pila()
    palabra = palabra.lower().replace(" ", "")

    for letra in palabra:
        pila.apilar(letra)

    palabra_invertida = ""
    while not pila.esta_vacia():
        palabra_invertida += pila.desapilar()

    return palabra == palabra_invertida

# Ejemplo de uso
palabra = input("Ingrese una palabra o frase: ")
if es_palindromo(palabra):
    print("La palabra o frase es un palíndromo.")
else:
    print("La palabra o frase no es un palíndromo.")
