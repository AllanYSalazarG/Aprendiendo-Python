def suma(*numeros):
    resultado = 0
    for numero in numeros:
        resultado += numero
    print(resultado)


suma(2, 3)
suma(2, 3, 4)
suma(2, 3, 4, 5)
