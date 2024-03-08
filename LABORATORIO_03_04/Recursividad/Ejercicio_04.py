#4) Ejercicio 4: 
# Escribe una función recursiva que imprima la pirámide de números invertidos del 1 al n

def piramide_invertida(n, fila=1, espacio=" "):
    if fila > n:
        return
    else:
        print(espacio * (n - fila) + str(fila) * fila)
        piramide_invertida(n, fila + 1)
        print(espacio * (n - fila) + str(fila) * fila)
# Solicitar al usuario que ingrese un número entero positivo
n = int(input("Ingresa un número entero positivo: "))
# Llamar a la función recursiva
piramide_invertida(n)