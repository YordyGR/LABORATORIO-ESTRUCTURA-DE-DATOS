#Laboratorio 5
# ejercicio 20

"""Escriba una función que reciba un conjunto de palabras y devuelva un conjunto con las palabras que son
palíndromos, tienen una longitud determinada y están ordenadas de menor a mayor."""

def palabras_palindromas_por_longitud(palabras, longitud):
    palindromos = {palabra for palabra in palabras if palabra == palabra[::-1] and len(palabra) == longitud}
    return sorted(palindromos)

resultado = palabras_palindromas_por_longitud({"radar", "oso", "casa", "reconocer"}, 5)
print(resultado)  # Esto imprimirá: {'radar', 'recon'}

