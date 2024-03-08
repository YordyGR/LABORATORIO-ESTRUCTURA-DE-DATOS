#-----Número Primo:-----
#-----5) Verifica si un número ingresado por el usuario es primo o no-----

#Verifica si un número entero es primo o no.
def es_primo(n):
    if n < 2:
        return False
    elif n == 2:
        return True
    elif n % 2 == 0:
        return False
    else:
        i = 3
        while i * i <= n:
            if n % i == 0:
                return False
            i += 2
        return True
    
# Solicitar al usuario que ingrese un número entero
numero = int(input("Ingresa un número entero: "))

# Verificar si el número es primo o no
if es_primo(numero):
    print(numero, "es un número primo.")
else:
    print(numero, "no es un número primo.")