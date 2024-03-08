#3) Ejercicio 3: 
# Escribe una función recursiva que imprima la pirámide de números del 1 al n

def piramide(n, fila=1, espacio=" "):
    if fila > n:
        return
    else:
        print(espacio * (n - fila) + str(fila) * fila)
        piramide(n, fila + 1)

# Solicitar al usuario que ingrese un número entero positivo
n = int(input("Ingresa un número entero positivo: "))
# Llamar a la función recursiva
piramide(n)