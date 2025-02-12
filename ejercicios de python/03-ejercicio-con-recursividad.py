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


def palindrome(string):
    # Caso Base: Cuando la cadena tiene menos de 1 caracter, es palindromo
    if len(string) <= 1:
        return True
    # Caso Recursivo: Comparamos el 1er y ultimo caracter
    # Si son diferentes, no es palindromo
    if string[0] != string[-1]:
        return False
    # De lo contrario, se llama a la funcion con la cadena quitando
    # los caracteres comparados
    return palindrome(string[1:-1])


print(palindrome("casa"))

# 6. Conteo de digitos en un numero


def countDigits(digits, count=1):
    # Caso Base: Si el numero es menor a 10, solo es un digito, regresamos 1
    if digits < 10:
        return 1
    # Caso Recursivo: si tiene mas digitos, lo dividimos entre 10 para ir quitando
    # el ultimo numero y lo agregamos a la funcion
    # Y al contador le agregamos 1 (es lo que retorna en el if)
    digits //= 10
    return count + countDigits(digits)


print(countDigits(12347818))

# 7. Maximo comun divisor (MCD)


def mcd(a, b):
    # Caso Base: Si el segundo numero es 0, devolvemos el valor de a
    # siendo este el maximo comun divisor
    if b == 0:
        return a
    # Caso Recursivo: agregamos a la funcion el valor de b como 1er valor
    # y el residuo de a entre b
    return mcd(b, a % b)


print(mcd(56, 98))

# 8. Imprimir una lista al reves

# 9. Generar combinaciones de parentesis balanceados

# 10. Suma de elementos en una lista
