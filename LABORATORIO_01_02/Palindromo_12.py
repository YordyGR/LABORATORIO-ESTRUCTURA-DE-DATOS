#-----Palíndromo:----
#-----12) Verifica si una palabra ingresada por el usuario es un palíndromo.-----

# Solicitar al usuario que ingrese una palabra
palabra = input("Ingresa una palabra: ")
# Quitar los espacios en blanco y convertir la palabra a minúsculas
palabra = palabra.strip().lower()
# Verificar si la palabra es un palíndromo
if palabra == palabra[::-1]:
    print(palabra, "es un palíndromo.")
else:
    print(palabra, "no es un palíndromo.")