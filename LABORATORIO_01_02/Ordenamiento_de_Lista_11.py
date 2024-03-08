#-----Ordenamiento de Lista:-----
#-----11) Ordena una lista de números ingresados por el usuario de menor a mayor.-----

# Solicitar al usuario que ingrese una lista de números separados por comas
numeros = [int(x) for x in input("Ingresa una lista de números separados por comas: ").split(',')]

# Ordenar la lista de números de menor a mayor
numeros.sort()

# Imprimir la lista de números ordenada
print("La lista de números ordenada de menor a mayor es:", numeros)