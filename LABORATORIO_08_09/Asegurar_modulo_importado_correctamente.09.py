#Laboratorio 8 y 9
# ejercicio 09

"""Asegurar que un módulo se ha importado correctamente"""

try:
    import modulo
except ImportError:
    assert False, "No se pudo importar el módulo correctamente"

