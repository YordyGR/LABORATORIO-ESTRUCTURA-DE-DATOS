#Laboratorio 10 y 11
# ejercicio parte 02
# ejercicio 08
# pilas

"""Evaluar expresión posfija:
8. Crear un programa que evalúe una expresión matemática en notación posfija utilizando una pila."""

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

def evaluar_expresion_posfija(expresion):
    pila = Pila()
    operadores = {'+': lambda x, y: x + y,
                  '-': lambda x, y: x - y,
                  '*': lambda x, y: x * y,
                  '/': lambda x, y: x / y}

    for token in expresion.split():
        if token.isdigit():
            pila.apilar(int(token))
        elif token in operadores:
            segundo_operando = pila.desapilar()
            primer_operando = pila.desapilar()
            resultado = operadores[token](primer_operando, segundo_operando)
            pila.apilar(resultado)

    return pila.desapilar()

expresion_posfija = "5 3 + 8 *"
resultado = evaluar_expresion_posfija(expresion_posfija)
print("Expresión posfija:", expresion_posfija)
print("Resultado:", resultado)
