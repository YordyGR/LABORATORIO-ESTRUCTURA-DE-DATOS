#-----Cálculo del Área de un Círculo:-----
#-----14) Pide el radio de un círculo al usuario y calcula su área.-----

#importamos la biblioteca math
import math
# Solicitar al usuario que ingrese el radio o el diámetro de un círculo
opcion = int(input("Ingresa 1 para ingresar el radio o 2 para ingresar el diámetro: "))
if opcion == 1:
    radio = float(input("Ingresa el radio de un círculo: "))
    diametro = radio * 2
    circunferencia = math.pi * diametro
    area = math.pi * radio ** 2
    print("El diámetro es:", diametro)
    print("La circunferencia es:", circunferencia)
    print("El área es:", area)
elif opcion == 2:
    diametro = float(input("Ingresa el diámetro de un círculo: "))
    radio = diametro / 2
    circunferencia = math.pi * diametro
    area = math.pi * radio ** 2
    print("El radio es:", radio)
    print("La circunferencia es:", circunferencia)
    print("El área es:", area)
else:
    print("Opción inválida.")