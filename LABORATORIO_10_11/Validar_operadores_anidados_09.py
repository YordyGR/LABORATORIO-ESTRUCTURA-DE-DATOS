#Laboratorio 10 y 11
# ejercicio parte 02
# ejercicio 09
# pilas

"""Validar operadores anidados:
9. Verificar si los operadores en una expresión matemática están correctamente anidados utilizando una
pila."""

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

def verificar_operadores_anidados(expresion):
    pila = Pila()
    operadores_abiertos = ['(', '[', '{']
    operadores_cerrados = [')', ']', '}']

    for caracter in expresion:
        if caracter in operadores_abiertos:
            pila.apilar(caracter)
        elif caracter in operadores_cerrados:
            if pila.esta_vacia():
                return False
            operador_abierto = pila.desapilar()
            indice_cerrado = operadores_cerrados.index(caracter)
            if operadores_abiertos.index(operador_abierto) != indice_cerrado:
                return False

    return pila.esta_vacia()

expresion = "(2 + 3) * [5 - {4 / 2}]"
es_valida = verificar_operadores_anidados(expresion)
print("Expresión:", expresion)
if es_valida:
    print("Los operadores están correctamente anidados.")
else:
    print("Los operadores no están correctamente anidados.")

