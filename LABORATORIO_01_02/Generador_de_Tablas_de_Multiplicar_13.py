#-----Generador de Tablas de Multiplicar:-----
#-----13) Crea un programa que genere la tabla de multiplicar de un número ingresado por el usuario-----

# Solicitar al usuario que ingrese un número
numero = int(input("Ingresa un número: "))

# Generar la tabla de multiplicar del número
for i in range(1, 11):
    print(numero, "x", i, "=", numero * i)