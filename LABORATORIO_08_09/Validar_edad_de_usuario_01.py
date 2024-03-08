
#Laboratorio 8 y 9
# ejercicio 01

#1. Validar la edad de un usuario

def validar_edad():
    nacimiento = int(input("Ingrese su año de nacimiento: "))
    actual = int(input("Ingrese el año actual: "))
    edad = actual - nacimiento
    assert edad >= 0, "La fecha de nacimiento no puede ser en el futuro"
    assert edad < 150, "La edad parece ser demasiado grande"
    return "El usuario tiene {} años".format(edad)

# Llamada a la función con aserciones
try:
    resultado = validar_edad()
    print(resultado)
except AssertionError as error:
    print("Error de validación:", error)

