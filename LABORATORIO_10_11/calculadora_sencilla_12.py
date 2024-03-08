#Laboratorio 10 y 11
# ejercicio parte 02
# ejercicio 12
# pilas

"""Implementar una calculadora sencilla:
12. Crear una calculadora que pueda realizar operaciones básicas (+, -, *, /) utilizando una pila para evaluar
expresiones. """

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

def calcular(operacion, x, y):
    if operacion == '+':
        return x + y
    elif operacion == '-':
        return x - y
    elif operacion == '*':
        return x * y
    elif operacion == '/':
        return x / y
    else:
        return None

def calculadora():
    pila = Pila()

    while True:
        expresion = input("Ingrese una expresión (operación x y): ")
        if expresion == 'salir':
            break

        tokens = expresion.split()
        if len(tokens) != 3:
            print("Expresión inválida.")
            continue

        operacion = tokens[0]
        if operacion not in ['+', '-', '*', '/']:
            print("Operación inválida.")
            continue

        try:
            x = float(tokens[1])
            y = float(tokens[2])
        except ValueError:
            print("Valores inválidos.")
            continue

        resultado = calcular(operacion, x, y)
        if resultado is None:
            print("Operación no soportada.")
            continue

        pila.apilar(resultado)
        print("Resultado:", resultado)

    print("Calculadora finalizada.")

# Ejemplo de uso
calculadora()
