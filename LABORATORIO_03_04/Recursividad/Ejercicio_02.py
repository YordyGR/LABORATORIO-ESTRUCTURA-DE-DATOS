
#2) Ejercicio 2: 
# Escribe una función recursiva que imprima la suma de los números del 1 al n.

def suma_hasta(n):
    if n == 0:
        return 0
    else:
        return n + suma_hasta(n - 1)
# Solicitar al usuario que ingrese un número entero positivo
n = int(input("Ingresa un número entero positivo: "))
# Llamar a la función recursiva
resultado = suma_hasta(n)
# Imprimir el resultado
print("La suma de los números del 1 al", n, "es:", resultado)