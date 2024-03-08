#-----Números de la Serie Fibonacci:-----
#-----10) Genera los primeros 10 números de la serie Fibonacci.-----

# Generar los primeros 10 números de la serie Fibonacci
a, b = 0, 1
for _ in range(10):
    print(a)
    a, b = b, a + b