#Verificación de Número Par o Impar:
#2) Solicita un número al usuario y determina si es par o impar

# Solicitar al usuario que ingrese un número
numero = int(input("Ingresa un número entero: "))

# Verificar si el número es par o impar
def verificar_par_impar(numero):
    if numero % 2 == 0:
        print("El número", numero, "es par.")
    else:
        print("El número", numero, "es impar.")

verificar_par_impar(numero)