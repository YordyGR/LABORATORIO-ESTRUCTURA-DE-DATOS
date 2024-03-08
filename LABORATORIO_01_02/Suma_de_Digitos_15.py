#-----Suma de Dígitos:-----
#-----15) Toma un número entero y calcula la suma de sus dígitos.-----

# Solicitar al usuario que ingrese un número entero
numero = int(input("Ingresa un número entero: "))
# Calcular la suma de los dígitos del número
suma_digitos = 0
numero_original = numero
while numero > 0:
    suma_digitos += numero % 10
    numero //= 10
# Imprimir el resultado
print("La suma de los dígitos de", numero_original, "es:", suma_digitos)