#Laboratorio 8 y 9
# ejercicio 03
"""Validar el rango de una calificación"""

def validar_calificacion(calificacion):
    assert 0 <= calificacion <= 100, f"La calificación {calificacion} no está en el rango válido (0-100)"
    return calificacion

# Ejemplo de uso
calificacion_valida = 85
#calificacion_invalida = 120

print(validar_calificacion(calificacion_valida)) 
#print(validar_calificacion(calificacion_invalida))