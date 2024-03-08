#-----Suma de Números Pares:-----
#-----7) Calcula la suma de los números pares en un rango especificado por el usuario.-----

# Solicitar al usuario que ingrese el rango
menor = int(input("Ingresa el número menor del rango: "))
mayor = int(input("Ingresa el número mayor del rango: "))
# Calcular la suma de los números pares en el rango
suma = 0
for i in range(menor, mayor + 1):
    if i % 2 == 0:
        suma += i
# Imprimir la suma de los números pares
print("La suma de los números pares en el rango", menor, "a", mayor, "es:", suma)