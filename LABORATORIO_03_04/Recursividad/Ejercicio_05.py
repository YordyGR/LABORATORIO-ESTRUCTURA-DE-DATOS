#5) Ejercicio 5: 
# Escribe una función recursiva que imprima la tabla de multiplicar del n.

def tabla_multiplicar(n, i = 1):
    if i <= 10:
        print(n, "x", i, "=", n * i)
        tabla_multiplicar(n, i + 1)

n = float(input("Ingrese un número: "))
tabla_multiplicar(n)

