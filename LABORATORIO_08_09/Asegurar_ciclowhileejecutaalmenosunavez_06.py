#Laboratorio 8 y 9
# ejercicio 06

"""Asegurar que un ciclo while se ejecuta al menos una vez"""

contador = 0

while True:
    # Código dentro del ciclo while
    contador += 1
    if contador == 5:
        break

assert contador > 0, "El ciclo while no se ejecutó al menos una vez"
print("se ejecuta mas de una vez")
