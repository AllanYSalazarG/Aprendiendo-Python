"""Ejercicios con sentencia FOR"""

# 1. Escribe un programa que imprima la tabla de multiplicar del 5.

for item in range(1, 11):
    res = item * 5
    print(f"{item} x 5 = {res}")

# 2. Genera los primeros 10 números de la serie de Fibonacci.

item1 = 0
item2 = 1
for item in range(1, 11):
    res = item1 + item2
    print(res)
    item1 = item2
    item2 = res

# 3. Recorre una lista de números y cuenta cuántos son pares y cuántos son impares.

numeros = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10,
           11, 12, 13, 14, 15, 16, 17, 18, 19, 20]
pares = 0
impares = 0
for numero in numeros:
    if numero % 2 == 0:
        pares += 1
    else:
        impares += 1

print(f"En la lista {"numeros"} hay {pares} pares | {impares} impares")

# 4. Crea un programa que calcule el factorial de un número usando un bucle FOR.

numero = int(input("Ingresa un numero entero: "))
factorial = 1
mostrarNumero = numero
for item in range(1, numero):
    factorial *= numero
    numero -= 1

print(f"El factorial de {mostrarNumero} es {factorial}")

# 5. Haz un programa que sume los dígitos de un número ingresado por el usuario.

numeros = str(input("Ingresa un numero entero: "))
res = 0
for numero in numeros:
    res += int(numero)

print(f"El resultado de {numeros} es {res}")

# 6. Dada una lista de palabras, imprime las palabras con más de 5 caracteres.

lista = ["hola", "como", "estas", "amigo",
         "querido", "hermano", "topo", "cinco", "tres"]

for palabra in lista:
    if len(palabra) >= 5:
        print(palabra)

# 7. Escribe un programa que recorra un rango de números
#    y muestre aquellos que sean divisibles por 4 pero no por 6.

for numero in range(100):
    if numero % 4 == 0 and numero % 6 != 0:
        print(numero, end=", ")

# 8. Crea un programa que genere una lista de cuadrados de números del 1 al 20.

cuadrados = []

# Usando for
for item in range(1, 20):
    cuadrados.append(item ** 2)

print(cuadrados)

# Usando comprensión de listas
cuadrados = [item ** 2 for item in range(1, 20)]

print(cuadrados)

# 9. Diseña un programa que recorra un diccionario e imprima sus claves y valores.

usuarios = {"id": 1,
            "name": "Allan",
            "lastName": "Salazar",
            "age": 29,
            "BD-day": 20,
            "BD-month": 9,
            "BD-year": 1995}


# Recorriendo e imprimiendo la clave y valor del diccionario "usuarios"
for clave, valor in usuarios.items():
    print(clave, valor)


# Recorriendo e imprimiendo el item completo del diccionario "usuario". NOTA: Regresa una tupla por cada item encontrado
for item in usuarios.items():
    print(item)

# 10. Genera las combinaciones posibles de dos listas (Ej.: [1,2] y ['a','b']).

lista1 = [1, 2]
lista2 = ['a', 'b']
combinaciones = []
for item in lista1:
    for item2 in lista2:
        combinaciones.append((item, item2))

print(combinaciones)
