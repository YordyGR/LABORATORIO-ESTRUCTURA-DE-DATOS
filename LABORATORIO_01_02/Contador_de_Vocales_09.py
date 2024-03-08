#-----Contador de Vocales:-----
#-----9) Cuenta el número de vocales en una cadena de texto.-----

# Solicitar al usuario que ingrese una cadena de texto
cadena = input("Ingresa una cadena de texto: ")
# Contar el número de vocales en la cadena de texto
vocales = "aeiouAEIOU"
contador = 0
for letra in cadena:
    if letra in vocales:
        contador += 1
# Imprimir el número de vocales en la cadena de texto
print("La cadena de texto tiene", contador, "vocales.")