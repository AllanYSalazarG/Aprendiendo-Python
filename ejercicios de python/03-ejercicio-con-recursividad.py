""" Practicando con recursividad """

# 1. Suma de los primeros N numeros naturales


def sumNumbers(number):
    # Caso Base: cuando number vale cero
    if number == 0:
        return 0
    # Caso Revursivo: suma los numeros hasta llegar a cero
    return number + sumNumbers(number - 1)


print(sumNumbers(3))

# 2. Inversión de una cadena de texto


def reverseString(string):
    # Caso Base: valida si la cadena tiene al menos un caracter
    if len(string) <= 1:
        return string
    # Caso Recursivo: va agregando la nueva cadena quitando el primer elemento
    return reverseString(string[1:]) + string[0]


print(reverseString("hola"))

# 3. Suma de los digitos de un numero


def sumDigits(digit):
    # Caso Base: El digito solo tiene un valor
    if digit < 10:
        return digit
    # Caso Recursivo: dejamos el ultimo numero y agregamos el resto a la funcion
    return digit % 10 + sumDigits(digit // 10)


print(sumDigits(345))

# 4. Potencia de un numero


def powerNumber(base, exp):
    # Caso Base: Validamos que el exponente sea 0
    if exp == 0:
        return 1
    # Caso Recursivo: vamos restando 1 al exponente,
    # multiplicando la base las veces que entre a la funcion
    return base * powerNumber(base, exp - 1)


print(powerNumber(5, 2))

# 5. Verificar si una palabra es palindromo

# 6. Conteo de digitos en un numero

# 7. Maximo comun divisor (MCD)

# 8. Imprimir una lista al reves

# 9. Generar combinaciones de parentesis balanceados

# 10. Suma de elementos en una lista
