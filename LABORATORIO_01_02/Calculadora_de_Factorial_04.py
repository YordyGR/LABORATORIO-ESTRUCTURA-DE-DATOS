#-----Calculadora de Factorial:-----
#-----4) Crea una función que calcule la factorial de un número-----

#Calcula el factorial de un número entero.
def factorial(n):  
    if n == 0:
        return 1
    else:
        return n * factorial(n-1)
# Solicitar al usuario que ingrese un número entero
numero = int(input("Ingresa un número entero: "))
# Calcular el factorial del número
factorial_numero = factorial(numero)
# Imprimir el factorial del número
print("El número factorial de", numero, "es:", factorial_numero)