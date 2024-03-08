#-----Recursividad:-----
#-----1) Ejercicio 1: 
# Escribe una función recursiva que imprima los números pares del 1 al 100.

# Función recursiva que imprime los números pares del 1 al 100
def imprimir_pares_hasta(n, numero=1):
    if numero <= n:
        if numero % 2 == 0:
            print(numero)
        imprimir_pares_hasta(n, numero + 1)
n = 100
# Llamar a la función recursiva
imprimir_pares_hasta(n)